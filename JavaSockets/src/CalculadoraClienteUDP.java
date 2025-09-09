
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class CalculadoraClienteUDP {
    Calculadora calculadora = new Calculadora();
    public static void main(String[] args){
         if(args.length != 3){
            System.out.println("Uso correto: <Nome da máquina> <Porta> <Valor1> <Valor2> <Operação>");
            System.exit(0);
        }

        try {
            InetAddress addr = InetAddress.getByName(args[0]);
            int port = Integer.parseInt(args[1]);
            float num1 = Float.parseFloat(args[2]);
            float num2 = Float.parseFloat(args[3]);
            byte[] op = args[4].getBytes();

            byte[] dados = calculadora.calcular().getBytes();

            DatagramPacket pkg = new DatagramPacket(dados, dados.length, addr, port);
            DatagramSocket ds = new DatagramSocket();

            ds.send(pkg);
            System.out.println();
            ds.close();
            
        } catch (IOException ioe) {
        }
    }
}
