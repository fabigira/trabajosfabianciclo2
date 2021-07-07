public class Persona {

    //Atributos
    private String nombre;
    private int edad;

    //metodos
    public int getEdad() {
        return edad;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;

        //constructor
        public Persona(String nombre, int edad){
        this.nombre = nombre;
        this.edad = edad;
        
    }
    



    
}
