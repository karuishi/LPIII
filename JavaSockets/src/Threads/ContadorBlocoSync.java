package Threads;

public class ContadorBlocoSync {
    private int contador = 0;

    public void incrementar(){
        // Você poderia ter outro código aqui que não precisa de lock...
        // SOLUÇÃO: Tranca o objeto 'this' (cont) apenas durante a operação crítica.
        synchronized (this) {
            contador++;
        }
    }
    // ... e outro código aqui.
    public static void main(String[] args) throws InterruptedException {
        ContadorBlocoSync cont = new ContadorBlocoSync();
        
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
            
        // O resultado aqui também será sempre 5000.
        System.out.println("Resultado final (Bloco Sync): " + cont.contador);
    }
}
