package Exercicios.Q05;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class LeilaoClienteTCP {
    private static final String HOST = "127.0.0.1";
    private static final int PORT = 12345;

    public static void main(String[] args){
        System.out.println("Conectando em " + HOST + ":" + PORT + "...");
        try {
            Socket client = new Socket(HOST, PORT);
            BufferedReader serverIn = new BufferedReader(new InputStreamReader(client.getInputStream()));
            PrintWriter serverOut = new PrintWriter(client.getOutputStream(), true);
            BufferedReader userIn = new BufferedReader(new InputStreamReader(System.in));

            //thread para ler mensagens do servidor
            Thread reader = new Thread(() -> {
                try {
                    String line;
                    while((line = serverIn.readLine()) != null){
                        System.out.println(line);
                    }
                } catch (Exception e) {
                }
            });
            reader.start();

            // Loop de envio (stdin -> servidor)
            String userLine;
            while((userLine = userIn.readLine()) != null){
                serverOut.println(userLine);
                if("exit".equalsIgnoreCase(userLine.trim())){
                    break;
                }
            }
        } catch (Exception e) {
        }
    }
}
