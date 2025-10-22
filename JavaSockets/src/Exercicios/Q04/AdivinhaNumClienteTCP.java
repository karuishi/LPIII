package Exercicios.Q04;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class AdivinhaNumClienteTCP {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        try {
            Socket cliente = new Socket("localhost", 12345);

            ObjectOutputStream numeroSaida = new ObjectOutputStream(cliente.getOutputStream());
            ObjectInputStream numeroEntrada = new ObjectInputStream(cliente.getInputStream());

            while(true){
                try {
                    System.out.print("Informe um número: ");
                    int numeroDigitado = scanner.nextInt();
                    scanner.nextLine();

                    numeroSaida.writeObject(numeroDigitado);
                    String resultado = (String)numeroEntrada.readObject();
                    System.out.println(resultado);

                    if(resultado.startsWith("Parabéns")){
                        break;
                    }
                } catch (Exception e) {
                    System.out.println("Cliente desconectado: " + cliente.getInetAddress().getHostAddress());
                    break;
                }
            }
        } catch (Exception e) {
        }
    }
}
