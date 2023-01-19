import java.awt.*;
import java.awt.event.*;
class Slip14B extends Frame implements ActionListener
{
      Label l1,l2,l3,l;
      TextField txt1,txt2,txt3;
      Button submit,clear;
      Panel p1;
            Slip24()
      {
            l=new Label("EMPLOYEE INFORMTION");
            l1=new Label("Name ");
            l2=new Label("Address ");
            l3=new Label("Salary ");
                        txt1=new TextField(20);
            txt2=new TextField(20);
            txt3=new TextField(20);
            submit=new Button("submit"); 
            submit.addActionListener(this);
            clear=new Button("Clear");   
            clear.addActionListener(this);
                        p1=new Panel();
            //p1.setLayout(new GridLayout(6,2));
            p1.add(l1);
                  p1.add(txt1);
            p1.add(l2);
                  p1.add(txt2);
            p1.add(l3);
                  p1.add(txt3);
            p1.add(submit);
            p1.add(clear
            add(p1);
            setVisible(true);
            setSize(400,400);
      }      
      public void actionPerformed(ActionEvent ae)
      {
            if(ae.getSource()==submit)
            {
                                    new Employee_Detail(txt1.getText(),txt2.getText(),txt3.getText());
            }
            if(ae.getSource()==clear)
            {
                  txt1.setText("");
                  txt2.setText("");
                  txt3.setText("");
            }
      }
 public static void  main(String args[])
 {
      new Slip14B();
 }
}
