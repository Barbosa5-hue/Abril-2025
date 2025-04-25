import java.util.ArrayList;
import java.util.Scanner;

public class Aluno {
String nome;
int idade;
String curso;
ArrayList<String> aulasAssistidas;

/**
 * o método costrutor de aluno que serve para construir o aluno * e o aluno é construido 
 * acrescentada de acordo com as aulas que ele assiste * preciso nem explicar afinal
 * @param nome o nome é
 * @param idade a idade inteiraulasAssistidas
 * @param curso não é meio óbvio pra você
 */

public Aluno(String nome,int idade,String curso) {
this.nome = nome;
this.idade = idade;
this.curso = curso;
aulasAssistidas = new ArrayList<>();
}
/**
 * um método que responde a alguém que vos falar
 * @param nome o nome de quem fala com você
*/
public String saudacao(String nome){
    return "Olá" + nome;
}

/**
 * Um método que responde a alguém que ele assiste
 * @param aula qual aula ele assiste
 */
public void assistindoAula(String aula){
    this.aulasAssistidas.add(aula);
}

/**
 *
 * @param a relação em formato string das aulas que se assistiu
 */




public String relacaoAulas(){
    String aulas = "";
    for (String elemento:this.aulasAssistidas){
        aulas += elemento+ ", ";
}

    return aulas;
}

public static void main (String[] args) {
    Scanner leitor = new Scanner(System.in);


System.out.println("Informe o nome");
String nome = leitor.next();

System.out.println("Informe a idade");
int idade = leitor.nextInt();

System.out.println("Informe o curso");
String curso = leitor.next();

Aluno cicila = new Aluno(nome, idade, curso);



cicila.assistindoAula("Java");
System.out.println("Informe o nome de quem cumprimenta");
nome = leitor.next();

System.out.println(cicila.saudacao(nome));

cicila.assistindoAula("POO");
cicila.assistindoAula("Java");
cicila.assistindoAula("HTML");

System.out.println(cicila.relacaoAulas());
}
}