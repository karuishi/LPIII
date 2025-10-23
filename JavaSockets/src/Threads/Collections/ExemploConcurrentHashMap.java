package Threads.Collections;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ExemploConcurrentHashMap {
    public static void main(String[] args) throws InterruptedException {
        
        // Crie o mapa que já é thread-safe 
        Map<String, Integer> mapa = new ConcurrentHashMap<>();

        ExecutorService executor = Executors.newFixedThreadPool(2);

        // Tarefa 1: Escreve em chaves "A"
        Runnable tarefa1 = () -> {
            for (int i = 0; i < 1000; i++) {
                mapa.put("A-" + i, i);
            }
        };
        
        // Tarefa 2: Escreve em chaves "B"
        Runnable tarefa2 = () -> {
            for (int i = 0; i < 1000; i++) {
                mapa.put("B-" + i, i);
            }
        };

        // Tarefa1 e Tarefa2 podem rodar *quase* em paralelo total,
        // pois estão mexendo em partes diferentes do mapa.
        executor.submit(tarefa1);
        executor.submit(tarefa2);

        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.MINUTES);

        // O resultado será sempre 2000.
        System.out.println("Tamanho final (ConcurrentHashMap): " + mapa.size());
    }
}