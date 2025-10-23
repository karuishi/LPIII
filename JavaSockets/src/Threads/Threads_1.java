package Threads;

public class Threads_1 {
    public static void main(String[] args){
        // 1. Crie uma instância da sua tarefa
        Runnable tarefa = new MeuRunnable();

        // 2. Crie um "trabalhador" (Thread) e entregue a tarefa para ele
        Thread t1 = new Thread(tarefa);

        // 3. Inicie o trabalhador (Thread) começar
        t1.start();

        // Atalho para "new MeuRunnable()"
        Runnable tarefaLambda = () -> System.out.println("LP-III");

        Thread t2 = new Thread(tarefaLambda);
        t2.start();
    }
}
