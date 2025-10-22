package Exercicios.Q03;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class DicionarioServidorTCP {
    static Map<String, String> dicionario = new HashMap<>();
    
    public static void main(String[] args){
        try {
            ServerSocket servidor = new ServerSocket(12345);
            System.out.println("Servidor do dicionário ouvindo da porta 12345");
            dicionario.put("casa", "lugar de moradia");
            dicionario.put("java", "Uma linguagem de programação e plataforma de software");
            dicionario.put("socket", "Um ponto final em uma comunicação de rede");
            while (true){
                Socket cliente = servidor.accept();
                System.out.println("Cliente conectado: " + cliente.getInetAddress().getHostAddress());
                
                ObjectInputStream palavra = new ObjectInputStream(cliente.getInputStream());
                ObjectOutputStream saida = new ObjectOutputStream(cliente.getOutputStream());
                
                while(true){
                    try{
                        String palavraAtual = (String)palavra.readObject();
                        String significado = dicionario.get(palavraAtual);
                        
                        if(significado == null) saida.writeObject("Palavra não encontrada!");
                        saida.writeObject(significado);
                        saida.flush();
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
