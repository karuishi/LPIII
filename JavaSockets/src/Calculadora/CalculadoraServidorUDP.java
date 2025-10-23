package Calculadora;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import javax.swing.JOptionPane;

public class CalculadoraServidorUDP {
    public static void main(String[] args) {
            if(args.length != 5){
            System.out.println("Uso correto: <Nome da máquina> <Porta> <Mensagem>");
            System.exit(0);
        }
        try {
            int port = Integer.parseInt(args[0]);
            DatagramSocket ds = new DatagramSocket(port);
            System.out.println("ouvindo a porta: " + port);
            byte[] msg = new byte[256];

            DatagramPacket pkg = new DatagramPacket(msg, msg.length);
            ds.receive(pkg);
            JOptionPane.showMessageDialog(null, new String(pkg.getData()).trim(), "Resultado", 1);
            ds.close();
            
        } catch (IOException ioe) {
        }
    }
}
