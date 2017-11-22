import cn.Email;
import cn.Person;

import java.io.*;
import java.util.Arrays;
import java.util.regex.Pattern;

public class a {
    public static void main(final String[] args) throws IOException {
        FileInputStream fis=new FileInputStream("d://a.java");
        FileOutputStream fos=new FileOutputStream("d://a.txt");
        byte[] b=new byte[1024];
        while ((fis.read(b))!=-1){
            fos.write(b);
        }
        fis.close();
        fos.close();
    }
}
