package Threads;

public class MeuRunnable implements Runnable{
    // Este é o método obrigatório do "contrato" Runnable
    @Override
    public void run(){
        // Tudo o que estiver aqui dentro será executado pela nova thread
        System.out.println("Olá Mundo!");

        String name = Thread.currentThread().getName();
        System.out.println("Eu estou rodando na thread: " + name);
    }
}
