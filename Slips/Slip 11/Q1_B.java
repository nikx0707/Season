import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
class Q1_B extends Applet implements KeyListener
{
    public void init()
    {
	setBackground(Color.white);
	addKeyListener(this);
    }
 
    public void keyPressed(KeyEvent e)
    {
	if(e.getKeyCode()==KeyEvent.VK_CONTROL)
	{
  	    int R = (int)(Math.random()*100) % 255;
	    int G = (int)(Math.random()*100) % 255;
	    int B = (int)(Math.random()*100) % 255;
	    Color mycolor = new Color(R,G,B);
	    this.setBackground(mycolor);
	}
    }

    public void keyReleased(KeyEvent e)
    {
    }
 
    public void keyTyped(KeyEvent e)
    {
    }
}