package Exercicios.Q06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicInteger;

public class VotacaoServidorTCP {
    private static final int PORT = 12345;
    // Recursos compartilhados
    private List<PrintWriter> clientWriters = new CopyOnWriteArrayList<>();
    private Map<Integer, String> candidatos = new ConcurrentHashMap<>();
    private Map<Integer, AtomicInteger> contagemVotos = new ConcurrentHashMap<>();
    // Gerador de ID
    private AtomicInteger nextClientID = new  AtomicInteger(1);

    public static void main(String[] args){
        VotacaoServidorTCP servidorTCP = new VotacaoServidorTCP();
        servidorTCP.iniciarServidor();
    }

    public void iniciarServidor(){
        System.out.println("[Servidor] Ouvindo na porta" + PORT + "...");
        inicializarCandidatos();
        try(ServerSocket serverSocket = new ServerSocket(PORT)){
            while(true){
                Socket clientSocket = serverSocket.accept();
                int clientId = nextClientID.getAndIncrement();
                System.out.println("[Servidor] Cliente " + clientId + " conectou de : " + clientSocket.getInetAddress().getHostAddress());
                new Thread(new ClientHandler(clientSocket, this, clientId)).start();
            }
        } catch(IOException e){
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public class ClientHandler implements Runnable{
        private final Socket client;
        private final VotacaoServidorTCP servidorTCP;
        private final int clientId;

        private ClientHandler(Socket client, VotacaoServidorTCP servidorTCP, int clientId){
            this.client = client;
            this.servidorTCP = servidorTCP;
            this.clientId = clientId;
        }

        @Override public void run(){
            PrintWriter out = null;
            try{
                out = new PrintWriter(client.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));

                servidorTCP.addClient(out);
                out.println("--- Opções de Votação ---");
                for(Map.Entry<Integer, String> entry : servidorTCP.candidatos.entrySet()){
                    Integer num = entry.getKey();
                    String nome = entry.getValue();
                    out.println("vote " + num + " para " + nome);
                }
                out.println("-------------------------");
                out.println("Digite o número do seu candidato:");

                String linhaCliente;
                while((linhaCliente = in.readLine()) != null){
                    if("exit".equalsIgnoreCase(linhaCliente.trim())){
                        out.println("Você saiu do chat. Até logo!");
                        break;
                    }

                    try{
                        int voto = Integer.parseInt(linhaCliente);
                        String checkVoto = candidatos.get(voto);
                        if(checkVoto == null){
                            out.println("Opção de voto não encontrada!");
                        } else {
                            servidorTCP.contagemVotos.get(voto).incrementAndGet();
                            out.println("Voto computado com sucesso!");
                            broadcastResultados();
                        }
                    }catch(NumberFormatException e){
                        out.println("Entrada inválida. Por favor, digite uma opção válida.");
                    }
                }
            }catch(IOException e){
                System.out.println("[Handler] Cliente desconectado: " + e.getMessage());
            }finally{
                if(out != null){
                    servidorTCP.removeClient(out);
                    System.out.println("[Servidor] Cliente " + clientId + " desconectou.");
                }
                try {
                    client.close();
                } catch (Exception e) {
                }
            }
        }
    }

    // Inicia os candidatos disponiveis
    public void inicializarCandidatos(){
        candidatos.put(13, "Lula");
        contagemVotos.put(13, new AtomicInteger(0));
        candidatos.put(22, "Bolsonaro");
        contagemVotos.put(22, new AtomicInteger(0));
        candidatos.put(17, "Chupetinha");
        contagemVotos.put(17, new AtomicInteger(0));
        candidatos.put(56, "Flordelis");
        contagemVotos.put(56, new AtomicInteger(0));
    }

    // Adiciona um novo cliente à lista
    public void addClient(PrintWriter writer){
        clientWriters.add(writer);
    }

    // Remove um cliente da lista
    public void removeClient(PrintWriter writer){
        clientWriters.remove(writer);
    }

    // Contabiliza os votos e notifica aos clientes
    private void broadcastResultados() {
        // 1. Usamos StringBuilder para construir a mensagem
        StringBuilder placar = new StringBuilder();
        placar.append("\n--- Placar Atual ---\n");

        // 2. Iteramos pelo mapa de nomes (candidatos)
        for (Map.Entry<Integer, String> entry : candidatos.entrySet()) {
            Integer numeroCandidato = entry.getKey();
            String nomeCandidato = entry.getValue();
            
            // 3. Pegamos a contagem de votos do *outro* mapa
            int contagem = contagemVotos.get(numeroCandidato).get();
            
            // 4. Adicionamos ao placar
            placar.append(nomeCandidato)
                  .append(" (")
                  .append(numeroCandidato)
                  .append("): ")
                  .append(contagem)
                  .append(" votos\n");
        }
        placar.append("--------------------");

        // 5. Convertemos o placar para String
        String mensagemPlacar = placar.toString();

        // 6. Envia a mensagem para os clientes
        for(PrintWriter pw : clientWriters){
            pw.println(mensagemPlacar);
        }
    }
}
