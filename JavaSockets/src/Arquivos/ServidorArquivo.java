package Arquivos;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class ServidorArquivo {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Uso: java ServidorArquivo <porta>");
            System.exit(0);
        }
        try {
            int porta = Integer.parseInt(args[0]);
            // Instancia o ServerSocket ouvindo a porta 12345
            ServerSocket servidor = new ServerSocket(porta);
            System.out.println("Servidor ouvindo na porta " + porta);
            while (true) {
                // O método accept() bloqueia a execução até que o servidor receba um
                // pedido de conexão
                Socket cliente = servidor.accept();
                System.out.println("Cliente conectado: " + cliente.getInetAddress().getHostAddress());
                // Cria e inicia a thread para tratar o cliente
                ThreadCliente thread = new ThreadCliente(cliente);
                thread.start();
            }
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }
}

class ThreadCliente extends Thread {

    private Socket cliente;

    public ThreadCliente(Socket cliente) {
        this.cliente = cliente;
    }

    public void run() {
        try {
            // ObjectInputStream para receber o nome do arquivo
            ObjectInputStream entrada = new ObjectInputStream(cliente.getInputStream());
            DataOutputStream saida = new DataOutputStream(cliente.getOutputStream());
            // Recebe o nome do arquivo
            String arquivo = (String) entrada.readObject();

            File file = new File(arquivo);
            FileInputStream arq = new FileInputStream(file);

            // Buffer de leitura dos bytes do arquivo
            byte buffer[] = new byte[512];

            saida.flush();
            int leitura = arq.read(buffer);
            // Lendo os bytes do arquivo e enviando para o socket

            while (leitura != -1) {
                saida.write(buffer, 0, leitura);
                leitura = arq.read(buffer);
            }

            System.out.println("Cliente atendido com sucesso: " + arquivo + " " + cliente.getRemoteSocketAddress().toString());
            entrada.close();
            saida.close();
            arq.close();
            cliente.close();
        }

        catch (IOException | ClassNotFoundException ioe) {
            System.out.println("Excecao ocorrida na thread: " + ioe.getMessage());
            try {
                cliente.close();
            } catch (Exception ec) {
            }
        }
    }
}