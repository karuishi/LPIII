package Threads.Synch;

public class ContadorMetodoSync {
    private int contador = 0;

    // SOLUÇÃO: Apenas uma thread pode executar este método por vez no mesmo objeto 'cont'
    public synchronized void incrementar(){
        contador++;
    }

    public static void main(String[] args) throws InterruptedException{
        ContadorMetodoSync cont = new ContadorMetodoSync();

        Runnable tarefa = () -> {
            for(int i = 0; i < 1000; i++){
                cont.incrementar();
            }
        };

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

        t1.join();
        t2.join();
        t3.join();
        t4.join();
        t5.join();

        System.out.println("Resultado final (Método Sync): " + cont.contador);
    }
}
