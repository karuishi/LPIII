package Threads.Collections;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ExemploSynchronizedList {
    public static void main(String[] args) throws InterruptedException {
        
        // 1. Crie a lista normal
        List<String> listaComum = new ArrayList<>();
        
        // 2. "Embrulhe" a lista para torná-la thread-safe 
        List<String> listaSincronizada = Collections.synchronizedList(listaComum);

        ExecutorService executor = Executors.newFixedThreadPool(5);

        Runnable tarefa = () -> {
            for (int i = 0; i < 1000; i++) {
                listaSincronizada.add("item"); // Agora é seguro
            }
        };

        executor.submit(tarefa);
        executor.submit(tarefa);
        executor.submit(tarefa);
        executor.submit(tarefa);
        executor.submit(tarefa);

        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.MINUTES);

        // O resultado aqui será sempre 5000.
        // Desvantagem: Só uma thread pode acessar a lista por vez,
        // mesmo que seja apenas para ler (get).
        System.out.println("Tamanho final (SynchronizedList): " + listaSincronizada.size());
    }
}