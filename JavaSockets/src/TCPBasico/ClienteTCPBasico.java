package TCPBasico;

import java.io.ObjectInputStream;
import java.net.Socket;
import java.util.Date;
import javax.swing.JOptionPane;

public class ClienteTCPBasico {
    public static void main(String[] args) {
        try {
            Socket cliente = new Socket("localhost",12345);
            ObjectInputStream entrada = new ObjectInputStream(cliente.getInputStream());
            Date dataAtual = (Date)entrada.readObject();
            JOptionPane.showMessageDialog(null, "Data recebida do servidor:" + dataAtual.toString());
            entrada.close();
            System.out.println("Conexão encerrada");
        }
        catch(Exception e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }
}
