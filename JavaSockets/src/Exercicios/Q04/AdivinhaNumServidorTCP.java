package Exercicios.Q04;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

public class AdivinhaNumServidorTCP {
    public static void main(String[] args){
        try{
            ServerSocket servidor = new ServerSocket(12345);
            System.out.println("Servidor do Adivinha número ouvindo da porta 12345");

            while(true){
                Socket cliente = servidor.accept();
                System.out.println("Cliente conectado: " + cliente.getInetAddress().getHostAddress());

                Random gerador = new Random();
                int numero = gerador.nextInt(100);

                ObjectInputStream numeroEntrada = new ObjectInputStream(cliente.getInputStream());
                ObjectOutputStream numeroSaida = new ObjectOutputStream(cliente.getOutputStream());

                while(true){
                    try {
                        int numeroDigitado = (int)numeroEntrada.readObject();

                        if(numeroDigitado > numero) numeroSaida.writeObject("Tente um número menor!");
                        if(numeroDigitado < numero) numeroSaida.writeObject("Tente um número maior!");
                        if(numeroDigitado == numero) {
                            numeroSaida.writeObject("Parabéns! Você acertou!");
                            numeroSaida.flush();
                            break;
                        }

                    } catch (Exception e) {
                        System.out.println("Cliente desconectado: " + cliente.getInetAddress().getHostAddress());
                        break;
                    }
                }
            }
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }
}
