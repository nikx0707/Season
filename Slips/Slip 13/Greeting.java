  public class Greeting {
      
       /*  This program asks the user's name and then
           greets the user by name.  This program depends
           on the non-standard class, TextIO.
       */
    
       public static void main(String[] args) {
       
           String usersName;      // The user's name, as entered by the user.
           String upperCaseName;  // The user's name, converted to uppercase letters.
           
           TextIO.put("Please enter your name: ");
           usersName = TextIO.getln();
           
           upperCaseName = usersName.toUpperCase();
           
           TextIO.putln("Hello, " + upperCaseName + ", nice to meet you!");
       
       }  // end main()

    }  // end class