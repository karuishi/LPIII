package Threads.Collections;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ExemploArrayList {
    public static void main(String[] args) throws InterruptedException {
        // A lista que será compartilhada
        List<String> lista = new ArrayList<>();

        ExecutorService executor = Executors.newFixedThreadPool(5);

        // Tarefa: Adicionar 1000 itens à lista
        Runnable tarefa = () -> {
            for (int i = 0; i < 1000; i++) {
                lista.add("item");
            }
        };

        // Enviar a tarefa para 5 threads executarem...
        executor.submit(tarefa);
        executor.submit(tarefa);
        executor.submit(tarefa);
        executor.submit(tarefa);
        executor.submit(tarefa);

        // Esperar elas terminarem
        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.MINUTES);

        // O resultado esperado era 5000.
        // Mas, ao rodar, o resultado será inconsistente (ex: 4827, 4912)
        // ou pode até dar uma exceção (ArrayIndexOutOfBoundsException).
        System.out.println("Tamanho final (ArrayList): " + lista.size());
    }
}