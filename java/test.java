// import java.io.*;
// import java.util.*;
// import java.util.List;
// import java.util.ArrayList;
// import java.time.temporal.ValueRange;
// class App_3 {
//     public static void main(String[] args){
//         int[] array = new int[] {1,2,3,4,5};
//         System.out.println("456");
//         List<Integer> listA = new ArrayList<Integer>();
//         listA.add(2);

//         ValueRange rang = ValueRange.of(0, 10);
//         System.out.println(rang);
//         // List<Integer> listB = (List) rang;
//         // for (int i:rang){

//         // }

//         // array[0] = 9;
//         System.out.println(listA);
//     }
// }


import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;  
 
public class test {



	public static void main(String[] args) {
        // main_2();
        // String a = Integer.toBinaryString('п');
        // System.out.println(a);
        System.out.println(getBinaryFromText("тест"));
    }
    public static String getBinaryFromText(String secretText) {
        byte[] bytes = secretText.getBytes(StandardCharsets.UTF_8);
        StringBuilder binary = new StringBuilder();
        for (byte b : bytes) {
            int val = b;
            for (int i = 0; i < 8; i++) {
                binary.append((val & 128) == 0 ? 0 : 1);
                val <<= 1;
            }
        }

        return binary.toString();
    }
    public static void main_2(){

        String s = "Some String";
        byte[] bytes = s.getBytes();
        StringBuilder binary = new StringBuilder();
        for(byte b:bytes){
            int val =b;
            for(int i=0;i<=s.length();i++){
                binary.append((val & 128) == 0 ? 0 : 1);
                val<<=1;
            }
            }
        
        System.out.println(" "+s+ "to binary" +binary);
    }
    public static void main_1(){
 
		Scanner sc = new Scanner(System.in);
		System.out.println("Введите информацию: ");
		String phrase1 = sc.nextLine();
        ArrayList<Object> array = new ArrayList<Object>();
        // for (String i: phrase1.toCharArray());
        //     System.out.println();
        String string = "Techie Delight";
        List<Character> chars = new ArrayList<>();
 
        for (char ch: phrase1.toCharArray()) {
            chars.add(ch);
        }
 
        System.out.println(chars);
		System.out.println(phrase1);
	}
}