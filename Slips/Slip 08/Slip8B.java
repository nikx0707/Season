import java.io.File;

class Slip8B {

    public static void main(String[] args) {

        File file = new File("C:\\Users\\Saurabh_Sapkal\\Desktop\\ln\\java\\Slips");

        String[] fileList = file.list();

        for(String str : fileList) {

            if(str.endsWith(".txt")){

                System.out.println(str);

            }

        }

    }

}