package Exercicios;
import java.io.*;
import java.net.*;
import java.util.concurrent.atomic.AtomicBoolean;

public class ChatCliente {
    private static final String HOST = "127.0.0.1";
    private static final int PORT = 12345;

    public static void main(String[] args){
        System.out.println("Conectando em " + HOST + ":" + PORT + "...");
        try(
            Socket cliente = new Socket(HOST, PORT);
            BufferedReader serverIn = new BufferedReader(new InputStreamReader(cliente.getInputStream()));
            PrintWriter serverOut = new PrintWriter(cliente.getOutputStream(), true);
            BufferedReader userIn = new BufferedReader(new InputStreamReader(System.in))
        ) {
            AtomicBoolean running = new AtomicBoolean(true);
            //thread para ler mensagens do servidor
            Thread reader = new Thread(() -> {
                try {
                    String line;
                    while((line = serverIn.readLine()) != null){
                        System.out.println(line);
                    }
                } catch (Exception e) {
                    // servidor pode fechar; encerrar leitor
                }finally{
                    running.set(false);
                }
            });
            reader.start();
            // Loop de envio (stdin -> servidor)
            String userLine;
            while(running.get() && (userLine = userIn.readLine()) != null){
                //TODO [Aluno]: enviar a linha ao servidor
                serverOut.println(userLine);
                if("exit".equalsIgnoreCase(userLine.trim())){
                    break;
                }
            }
            //encerrar conexão
            try{reader.join(500);} catch(InterruptedException ignore){}
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
