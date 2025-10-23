package Exercicios.Q05;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

public class LeilaoServidorTCP {
    private static final int PORT = 12345;
    // Recursos compartilhados
    private List<PrintWriter> clientWriters = new CopyOnWriteArrayList<>();
    private double lanceMaxAtual = 0.0;
    // Objetos Locks separados para cada recurso
    private final Object bidLock = new Object();
    
    public static void main(String[] args){
        LeilaoServidorTCP servidorTCP = new LeilaoServidorTCP();
        servidorTCP.iniciarServidor();
    }

    public void iniciarServidor(){
        System.out.println("[Servidor] Ouvindo na porta " + PORT + "...");

        try(ServerSocket serverSocket = new ServerSocket(PORT)){
            while(true){
                Socket clientSocket = serverSocket.accept();
                System.out.println("[Servidor] Conexão de: " + clientSocket.getInetAddress().getHostAddress());
                //O ClientHandler (que está rodando em sua própria thread) tem tudo o que precisa:
                //1. client: Para ler os lances que este cliente envia.
                //2. servidorTCP: Para chamar os métodos compartilhados como addClient e broadcastNewBid.
                new Thread(new ClientHandler(clientSocket, this)).start();
            }
        }catch(IOException e){
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public class ClientHandler implements Runnable{
        private final Socket client;
        private final LeilaoServidorTCP servidorTCP;
        
        private ClientHandler(Socket client, LeilaoServidorTCP servidorTCP){
            this.client = client;
            this.servidorTCP = servidorTCP;
        }

        @Override public void run(){
            PrintWriter out = null;
            try{
                // Usar PrintWriter para texto é mais fácil que ObjectOutputStream
                out = new PrintWriter(client.getOutputStream(), true); // 'true' para autoFlush
                // BufferedReader para ler linhas de texto
                BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));

                servidorTCP.addClient(out); // Adiciona cliente na lista, assim que é conectado
                String linhaCliente;
                while((linhaCliente = in.readLine()) != null){ // Captura a entrada do teclado do cliente
                    try {
                        double lance = Double.parseDouble(linhaCliente);
                        broadcastNewBid(lance);
                    } catch (NumberFormatException e) { // Captura o erro específico e notifica apenas ao cliente que cometeu o erro
                        out.println("Entrada inválida. Por favor, digite um número.");
                    }
                }
                
            } catch (IOException e){
                System.out.println("[Handler] Cliente desconectado: " + e.getMessage());
            } finally{
                if(out != null){
                    servidorTCP.removeClient(out);
                }
                try {
                    client.close();
                } catch (Exception e) {
                }
            }
        }
        
    }
    
    // Adiciona um novo cliente à lista (thread-safe)
    public void addClient(PrintWriter writer){
       clientWriters.add(writer);
    }

    // Remove um cliente da lista 
    public void removeClient(PrintWriter writer){
       clientWriters.remove(writer);
    }

    // Atualiza o lance máximo e notifica todos os clientes
    private void broadcastNewBid(double novoLance){
        synchronized(bidLock){
            if(novoLance > lanceMaxAtual) lanceMaxAtual = novoLance;
        }

        for(PrintWriter pw : clientWriters){
            pw.println("Novo lance: " + novoLance);
        }
    }
}
