public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        Persona p1 = new Persona("Mauricio", 15);
        System.out.println(p1.getEdad());
        System.out.println(p1.getNombre());
        //p1.setedad(20)
        System.out.println(p1.getEdad());
        p1.setNombre("Hernan");
        System.out.println(p1.getNombre());

    }
}
