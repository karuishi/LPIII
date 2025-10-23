package Threads.Collections;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ExemploCopyOnWrite {
    public static void main(String[] args) throws InterruptedException {
        
        // Crie a lista que já é thread-safe 
        List<String> lista = new CopyOnWriteArrayList<>();

        ExecutorService executor = Executors.newFixedThreadPool(5);

        Runnable tarefa = () -> {
            for (int i = 0; i < 1000; i++) {
                lista.add("item");
            }
        };

        executor.submit(tarefa);
        executor.submit(tarefa);
        
        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.MINUTES);

        // O resultado será sempre 2000.
        // Vantagem: Leituras (get) são muito rápidas e nunca bloqueiam.
        // Desvantagem: Escritas (add/remove) são "caras", pois
        // copiam a lista inteira a cada mudança.
        System.out.println("Tamanho final (CopyOnWriteArrayList): " + lista.size());
    }
}