public class challenge {
    
    public static String sayHello(String name) {
        if(name != null) {
            System.out.println("Hello, " + name + "!");
            return "Hello, " + name + "!";
        } else {
            System.out.println("Hello there!");
            return "Hello there!";
        }
    }
}
