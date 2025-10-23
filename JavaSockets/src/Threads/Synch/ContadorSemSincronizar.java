package Threads.Synch;

public class ContadorSemSincronizar {
    private int contador = 0;

    public void incrementar(){
        // 1. Ler o valor de 'contador' (ex: 10)
        // 2. Calcular o novo valor (ex: 10 + 1 = 11)
        // 3. Salvar o novo valor em 'contador' (ex: 11)
        contador++;
    }

    public static void main(String[] args) throws InterruptedException{
        ContadorSemSincronizar cont = new ContadorSemSincronizar();

        // Tarefa executada por cada thread
        Runnable tarefa = () -> {
            for(int i = 0; i < 1000; i++){
                cont.incrementar();
            }
        };

        // Criar e iniciar 5 threads
        Thread t1 = new Thread(tarefa);
        Thread t2 = new Thread(tarefa);
        Thread t3 = new Thread(tarefa);
        Thread t4 = new Thread(tarefa);
        Thread t5 = new Thread(tarefa);

        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();

        // Esperar todas as threads terminarem
        t1.join();
        t2.join();
        t3.join();
        t4.join();
        t5.join();

        System.out.println("Resultado final (sem sincronizar): " + cont.contador);
    }
}
