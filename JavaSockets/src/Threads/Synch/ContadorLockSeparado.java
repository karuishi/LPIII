package Threads.Synch;

import java.util.ArrayList;
import java.util.List;

public class ContadorLockSeparado {
    private int contador = 0;

    // SOLUÇÃO: Criamos um objeto que serve APENAS de  "cadeado"
    private final Object cadeadoDoContador = new Object();

    public void incrementar(){
        // Trancamos apenas o 'cadeadoDoContador', não o objeto 'cont' (this) inteiro.
        synchronized(cadeadoDoContador){
            contador++;
        }
    }

    // Se tivéssemos outra variável, ex: 'lista'
    private List<String> lista = new ArrayList<>();
    private final Object cadeadoDaLista = new Object();

    public void adicionarNaLista(String item) {
    synchronized (cadeadoDaLista) {
        lista.add(item);
    }
    }
    // Agora, uma thread pode 'incrementar()' ao MESMO TEMPO que outra thread chama 'adicionarNaLista()', 
    // pois elas usam cadeados diferentes!

    public static void main(String[] args) throws InterruptedException {
    ContadorLockSeparado cont = new ContadorLockSeparado();

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

        System.out.println("Resultado final (Lock Separado): " + cont.contador);
    }
}
