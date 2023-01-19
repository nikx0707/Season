
import javax.swing.*;
import java.awt.*;

public class Q1_A {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Text with Label");
        frame.setSize(400, 400);
        frame.setBackground(Color.RED);

        JLabel label = new JLabel("Dr. D Y Patil College");
        label.setFont(new Font("Serif", Font.BOLD, 20));

        frame.add(label);
        frame.setVisible(true);
    }
}