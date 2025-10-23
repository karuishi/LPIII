package Threads.Collections;
import java.util.Random;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Executors;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class ExemploBlockingQueue {
    
    // Criamos a fila[cite: 439]. Podemos dar um limite (ex: 10)
    private static BlockingQueue<Integer> fila = new LinkedBlockingQueue<>(10);
    private static Random random = new Random();

    public static void main(String[] args) {
        
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(2);

        // Tarefa PRODUTOR: Gera números e coloca na fila
        Runnable produtor = () -> {
            try {
                int numero = random.nextInt(100);
                System.out.println("Produzindo: " + numero);
                fila.put(numero); // Espera se a fila estiver CHEIA
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        };

        // Tarefa CONSUMIDOR: Pega números da fila e processa
        Runnable consumidor = () -> {
            try {
                Integer numero = fila.take(); // Espera se a fila estiver VAZIA
                System.out.println("--- Consumindo: " + numero);
                Thread.sleep(100); // Simula processamento
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        };

        // Roda o produtor a cada 50ms
        executor.scheduleWithFixedDelay(produtor, 0, 50, TimeUnit.MILLISECONDS);
        // Roda o consumidor a cada 200ms
        executor.scheduleWithFixedDelay(consumidor, 0, 200, TimeUnit.MILLISECONDS);
        
        // Deixe rodando por 10 segundos para ver o console
        try { TimeUnit.SECONDS.sleep(10); } catch (Exception e) {}
        executor.shutdownNow();
    }
}
