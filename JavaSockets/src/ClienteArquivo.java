import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.DataInputStream;
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import javax.swing.*;

public class ClienteArquivo extends JFrame {

    private JTextField txtServidor, txtPorta, txtArquivo, txtSaida;
    private JButton btnBuscar;
    private JLabel lblImagem;

    public ClienteArquivo() {
        super("Cliente de Arquivos");

        // Painel de entrada de dados
        JPanel panelInput = new JPanel(new GridLayout(5, 2, 5, 5));
        panelInput.add(new JLabel("Servidor:"));
        txtServidor = new JTextField("localhost");
        panelInput.add(txtServidor);

        panelInput.add(new JLabel("Porta:"));
        txtPorta = new JTextField("1234");
        panelInput.add(txtPorta);

        panelInput.add(new JLabel("Arquivo no Servidor (ex: foto.jpg):"));
        txtArquivo = new JTextField();
        panelInput.add(txtArquivo);
        
        panelInput.add(new JLabel("Salvar como (ex: foto_recebida.jpg):"));
        txtSaida = new JTextField();
        panelInput.add(txtSaida);

        btnBuscar = new JButton("Buscar Arquivo");
        panelInput.add(new JLabel()); // Espaço em branco
        panelInput.add(btnBuscar);

        // Painel para exibir a imagem
        JPanel panelImage = new JPanel(new BorderLayout());
        lblImagem = new JLabel("A imagem recebida aparecerá aqui", SwingConstants.CENTER);
        panelImage.add(new JScrollPane(lblImagem), BorderLayout.CENTER);

        // Adiciona os painéis à janela principal
        add(panelInput, BorderLayout.NORTH);
        add(panelImage, BorderLayout.CENTER);

        // Ação do botão
        btnBuscar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                btnBuscarActionPerformed(e);
            }
        });

        // Configurações da janela
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(500, 500);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void btnBuscarActionPerformed(ActionEvent evt) {
        try {
            // Cria o Socket para conectar ao servidor
            Socket rec = new Socket(txtServidor.getText(), Integer.parseInt(txtPorta.getText()));

            // Enviando o nome do arquivo a ser baixado do servidor
            ObjectOutputStream saida = new ObjectOutputStream(rec.getOutputStream());
            saida.writeObject(txtArquivo.getText());

            // DataInputStream para processar os bytes recebidos
            DataInputStream entrada = new DataInputStream(rec.getInputStream());
            // FileOutputStream para salvar o arquivo recebido
            FileOutputStream sarq = new FileOutputStream(txtSaida.getText());
            
            byte[] br = new byte[4096];
            int leitura;
            while ((leitura = entrada.read(br)) != -1) {
                sarq.write(br, 0, leitura);
            }

            // Fecha os recursos
            saida.close();
            entrada.close();
            sarq.close();
            rec.close();

            // Exibe a imagem no JLabel
            ImageIcon img = new ImageIcon(txtSaida.getText());
            lblImagem.setText("");
            lblImagem.setIcon(img);
            
            JOptionPane.showMessageDialog(null, "Arquivo recebido com sucesso!");

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Exceção: " + e.getMessage(), "Erro", JOptionPane.ERROR_MESSAGE);
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // Roda a interface gráfica
        SwingUtilities.invokeLater(() -> new ClienteArquivo());
    }
}