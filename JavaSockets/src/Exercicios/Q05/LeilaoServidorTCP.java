package Exercicios.Q05;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class LeilaoServidorTCP {
    private static final int PORT = 12345;

    // Recursos compartilhados
    private List<PrintWriter> clientWriters = new ArrayList<>();
    private double lanceMaxAtual = 0.0;

    // Objetos Locks separados para cada recurso
    private final Object listLock = new Object();
    private final Object bidLock = new Object();
    
    public static void main(String[] args){
        System.out.println("[Servidor] Ouvindo na porta " + PORT + "...");

        try(ServerSocket server = new ServerSocket(PORT)){
            while(true){
                Socket client = server.accept();
                System.out.println("[Servidor] Conexão de: " + client.getInetAddress().getHostAddress());
                new Thread(new ClientHandler(client)).start();
            }
        } catch(IOException e){
            System.out.println("Erro: " + e.getMessage());
        }

    }
    
    // Adiciona um novo cliente à lista (thread-safe)
    public void addClient(PrintWriter writer){
        synchronized(listLock){
            clientWriters.add(writer);
        }
    }

    // Remove um cliente da lista 
    public void removeClient(PrintWriter writer){
        synchronized(listLock){
            clientWriters.remove(writer);
        }
    }

    // Atualiza o lance máximo e notifica todos os clientes
    private void broadcastNewBid(double novoLance){
        synchronized(bidLock){
            lanceMaxAtual = novoLance;
        }

        synchronized(listLock){
            for(PrintWriter pw : clientWriters){
                pw.println("Novo lance: " + novoLance);
            }
        }
    }
}
