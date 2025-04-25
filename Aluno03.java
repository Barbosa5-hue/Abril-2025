import java.util.ArrayList; 
import java.util.Scanner;

public class Aluno{
String nome;
int idade;
String curso;
ArraryList<String>aualsAsssistidas

/**
 * O metodo construtor de alunoque serve para construir o aluno * e o aluno é construido
 * acrecantada de acordo com as aulas que ele assite * preciso nem explicar afinal
 * @param nome o nome é 
 * @param idade a idade inteira
 * @param curso não é meio obvio pra você
 */

 public Aluno(string nome,int idade, string curso){
    this.nome = nome;
    this.idade = idade;
    this.curso = curso;
    aualsAsssistidas = new ArraryList<>();
 }
/**
 * um metodo que respode a alguem que vos falar
 * @param nome o nome de quem fala com você
 */
public string saudação (String nome){
    return "Ola" + nome;
}

  /**
   * Um metodo que respoende alguem que ele assiste
   * @param aula qual aula ele assite
   */
public void assistindoAulas(String aula){
   this.aulaAsistidas.add(aula);
}

/**
 * 
 * @param a relação em formato string das aulas que assistiu
 */




 public String relacaoAulas(){
   Strig aula = "";
   for (String elemento: this.aualsAsssistidas){
      aulas += elementos+ "";
   }

   return aulas;
 } 
 Captura de tela de 2025-04-09 08-17-36
public static void main (String[]args){
   Scanner leitor = new Scanner(System.in);


System.out.println(x:"informe a idade");
String nome = leitor.next().


System.out.println(x:"Informe a idade");
int idade = leitor.next.Int();

System.out.println(x:"informe o curso");
String curso = leitor.next();

Aluno amora = new Aluno(nome:"ana", idade"12", curso"enfer");

 amora.assistindoaula(aula:"Java");
 System.out.println(x: "informe o nome de quem cumprimenta");
 String nome = leitor.next();

 System.out.println(amora.saudacao(nome));

amora.assistindoAula(aula: "POO");
amora.assistindoAula(aula: "Java");
amora.assistindoAula(aula: "HTMl");

System.out.println(amora.relacaoaulas());
}
}