// import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
// import java.util.concurrent.TimeUnit;




// class App_2 {
//     public static void main(String[] args) {
//         int v[] = {267,568,2489,6926};
//         // ArrayList<Integer> c = new ArrayList<Integer>();
//         // is_string_to_list
        
//         for (int b = 0; b < v.length; b++){
//             // System.out.println(b);
//             System.out.println(v[b]);

//             String z = Integer.toString(v[b]);

//             List<String> tokens = Arrays.asList(z.split("\\s*,\\s*"));
//             System.out.println(tokens);

//             //разделяем строку z на список 
//             List<Character> chars = new ArrayList<>();
     
//             for (char ch: z.toCharArray()) {
//                 chars.add(ch);
//             // int q[] = is_string_to_list(z);
    
//             // int result = z[0] * z[1];
//             // c.add(result);
//             // int z = c[0] * ;
//             // int i = Integer.parseInt(z.trim());
//             // System.out.print(z.toCharArray());
            
//             // c[c.length+1] = v[b];
//                 }
//                 System.out.println(chars);
//                 for (int i ; chars)
//                 // int a = chars[0];
                
//                 // System.out.println(chars[0]*chars[-1]);

//         // System.out.println(c);
//     }
// //     public static is_string_to_list(String string) {
// //         // Преобразование строки в список символов
// //             List<Character> chars = new ArrayList<>();
     
// //             for (char ch: string.toCharArray()) {
// //                 chars.add(ch);
               
// //             } 
// //             // return chars;
            
//         }

        
// }


class App {
    
    public static void main(String[] args) {
        // programm_2();
        System.out.println(-1073741824*4);
        System.out.println("123");
    }
    static void programm_1(){
        int v[] = {267,568,2489,6926};
        // ArrayList<Integer> c = new ArrayList<Integer>();
        // is_string_to_list
        long startTime = System.nanoTime(); //Старт замера времени
        for (int b = 0; b < v.length; b++){

            String z = Integer.toString(v[b]);

            List<String> tokens = Arrays.asList(z.split(""));
            int result = 0;
            int a = 0;
            for (String i: tokens){
                System.out.println(tokens.get(0));
                
                if (a == tokens.size()-1){
                    System.out.println("й");
                    System.out.println(i);
                    int iz = Integer.parseInt(i.trim());

                    result = result + (int) Math.pow(iz, 2) ;
                }
                else if (a == 0){
                    System.out.println("ц");
                    System.out.println(i);
                    int iz = Integer.parseInt(i.trim());
                    result = result + (int) Math.pow(iz, 2) ;
                }
                a = a+1;
            }
            System.out.println(result);


            System.out.println(tokens);
        }
        long endTime = System.nanoTime();
        long timeElapsed = endTime - startTime;
        System.out.println("Execution time in nanoseconds: " + timeElapsed);
        System.out.println("Execution time in milliseconds: " + timeElapsed / 1000000);
    }

    static void programm_2(){
        int a = 1;
        for (int i = 0; i<100; i++){
            
            a = a *4;
            a = a/2;
            System.out.println(a);
            // System.out.println("wer");
        }


    }

}

