package Exercicios.Q03;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class DicionarioClienteTCP {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        try {
            Socket cliente = new Socket("localhost", 12345);
           
            ObjectOutputStream saida = new ObjectOutputStream(cliente.getOutputStream());
            ObjectInputStream entrada = new ObjectInputStream(cliente.getInputStream());
           
            while (true) { 
                try {
                    System.out.print("Informe a palavra: ");
                    String palavra = scanner.nextLine();
                
                    saida.writeObject(palavra);
                    String significado = (String)entrada.readObject();
                    System.out.println(significado);

                    System.out.print("Deseja continuar (s/n): ");
                    String sair = scanner.nextLine();
                    if(sair.equalsIgnoreCase("N")) break;
                } catch (Exception e){
                    System.out.println("Cliente desconectado: " + cliente.getInetAddress().getHostAddress());
                    break;
                }
            }
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }
}
