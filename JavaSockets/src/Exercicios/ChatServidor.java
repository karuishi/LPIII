package Exercicios;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

public class ChatServidor {
    private static final int PORT = 12345;
    private static final List<PrintWriter> clients = new CopyOnWriteArrayList<>();

    public static void main(String[] args){
        System.out.println("[Servidor] Ouvindo na porta " + PORT + "...");

        try (ServerSocket servidor = new ServerSocket(PORT)){
            while (true) {
                Socket cliente = servidor.accept();
                System.out.println("[Servidor] Conexão de: " + cliente.getInetAddress().getHostAddress());
                new Thread(new ClientHandler(cliente)).start();
            }
        } catch (IOException e) {
            System.out.println("[Servidor] Erro: " + e.getMessage());
        }
    }

    private static class ClientHandler implements Runnable{
        private final Socket cliente;
        private PrintWriter out;

        public ClientHandler(Socket cliente) {
            this.cliente = cliente;
        }

        @Override public void run(){
            try(BufferedReader in = new BufferedReader(new InputStreamReader(cliente.getInputStream()));){
                out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(cliente.getOutputStream())), true);
                // 1) registrar cliente
                clients.add(out);
                // 2) dar boas-vindas
                out.println("Bem-vindo! Digite mensagens. Use 'exit' para sair.");
                //3) laço principal de leitura
                String line;
                while((line = in.readLine()) != null){
                    // TODO [Aluno]: se a linha for "exit", encerrar este cliente graciosamente (remover da lista e fechar socket).
                    // TODO [Aluno]: fazer broadcast da mensagem para TODOS os outros clientes.
                    //   - dica: itere sobre 'clients' e chame println(...)
                    //   - não envie de volta para o próprio 'out' (opcional)
                    if("exit".equalsIgnoreCase(line.trim())){
                        out.println("Você saiu do chat. Até logo!");
                        break;
                    }
                    broadcast("[" + cliente.getInetAddress().getHostAddress() + "]" + line, out);
                } 
            } catch(IOException e ){
                // queda de cliente é comum; logar e seguir
                System.out.println("Cliente desconectou: " + e.getMessage());
            }finally {
                //4) garantir limpeza
                //TODO [Aluno]: remover o PrintWriter deste cliente de 'clients'
                clients.remove(out);
                try{cliente.close();} catch (IOException ignore){}
            }
        }

        private void broadcast(String msg, PrintWriter sender){
            // TODO [Aluno]: enviar 'msg 'para todos em 'clientes'
            for(PrintWriter pw : clients){
                if(pw != sender){
                    pw.println(msg);
                }
            } 
        }
    }
}
