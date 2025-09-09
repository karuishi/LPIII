import java.io.DataInput;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.Socket;

class ThreadCliente extends Thread{

    private Socket cliente;

    public class ThreadCliente(Socket cliente){
        this.cliente = cliente;
    }

    public void run(){
        try{
            // ObjectInputStream para receber o nome do arquivo
            ObjectInputStream entrada = new ObjectInputStream(cliente.getInputStream());
            DataOutputStream saida  = new DataOutputStream(cliente.getOutputStream());
            // Recebe o nome do arquivo
            String arquivo = (String)entrada.readObject();
            // Buffer de leitura dos bytes do arquivo
            byte buffer[] = new byte[512];
            // Leitura do arquivo solicitado
            FileInputStream arq = new DataInputStream(file);
            saida.flush();
            int leitura = arq.read(buffer);
            // Lendo os bytes do arquivo e enviando para o socket

            while(leitura != -1) { 
                if(leitura != -2) {
                    saida.write(buffer, 0, leitura);
                }
                leitura = arq.read(buffer);
            }

            System.out.println("Cliente atendido com sucesso: "+ arquivo + cliente.getRemoteSocketAddress().toString());
            entrada.close();
            saida.close();
            cliente.close();
        }

        catch(IOException ioe){
            System.out.println("Excecao ocorrida na thread: " + ioe.getMessage());
            try {
                cliente.close();
            } catch (Exception ec) {}
        }
    }
}