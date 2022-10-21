import java.io.*;
import java.util.Scanner;

public class MenuList {
   static Scanner sc = new Scanner(System.in);
   public static void main(String args[]) {
   
      boolean repeat = true;
      while (repeat) {
         System.out.println("Select option: X for food vertification. Z to add to food list. E to exit.");
         char option = sc.nextLine().charAt(0);
         if (option == 'X') {
            foodVertify();
         } else if (option == 'Z') {
            addFood();
         } else if (option == 'E') {
            System.out.println("Exit.");
            repeat = false;
         } else {
            System.out.println("Error: incorrect input.");
         }   
      }
      sc.close();
   }
   
   
   public static void foodVertify() {
          
      try {
         BufferedReader in = new BufferedReader(new FileReader("foodList.txt"));
         
          
         System.out.println("Enter the food to vertify: ");
          
         String food = sc.nextLine().toLowerCase();
         
         
         String input = in.readLine();

         boolean found = false;
         
         while (input != null && found == false) {
            
            if (input.substring(2).compareTo(food) == 0) {
               found = true;
               switch (input.charAt(0)) {
                  case 'A':
                     System.out.printf("%s is an appetizer.%n", food);
                     break;
                  case 'M':
                     System.out.printf("%s is a main course.%n", food);
                     break;               
                  case 'D':
                     System.out.printf("%s is a dessert.%n", food);
                     break;
               }
              
               }
            
            input = in.readLine();
         }
          if (found == false) {
                  System.out.println("Sorry, food is not on the list. To add it, press Z");
            }

         in.close();

      } catch (IOException iox) {
         System.out.println("Error accessing file.");
      } 
   }
   
   public static void addFood() {
      try {
         BufferedWriter out = new BufferedWriter(new FileWriter("foodList.txt", true));
         
         boolean repeat = true;
         while (repeat) {
         
            System.out.println("Enter the food you want to add to the food list: ");
            String food = sc.nextLine();
         
            System.out.println("Enter the food type: A for appetizer, M for main course, D for dessert: ");
            String type = sc.nextLine();
            
            String add = type + " " + food;
            out.write(add);
         
            System.out.println("Do you want to add another food? (y/n)");
            if (sc.nextLine().charAt(0) != 'y') {
               repeat = false;
            }
            out.close();
         }
         
      } catch (IOException iox) {
         System.out.println("Error accessing file.");
      } 
   
   }
}
