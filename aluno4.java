import java.util.ArrayList;
import java.util.Scanner;

public class aluno4 {
    private String nome;
    private int idade;
    private String curso;
    private ArrayList<String> aulasAssistidas;

    /**
     * Construtor da classe Aluno que inicializa os atributos do aluno.
     * @param nome Nome do aluno.
     * @param idade Idade do aluno.
     * @param curso Curso que o aluno está matriculado.
     */
    public aluno4(String nome, int idade, String curso) {
        this.nome = nome;
        this.idade = idade;
        this.curso = curso;
        this.aulasAssistidas = new ArrayList<>();
    }

    /**
     * Método que retorna uma saudação personalizada.
     * @param nome Nome da pessoa que será saudada.
     * @return Mensagem de saudação.
     */
    public String saudacao(String nome) {
        return "Olá, " + nome + "! Seja bem-vindo!";
    }

    /**
     * Método que adiciona uma aula à lista de aulas assistidas pelo aluno.
     * @param aula Nome da aula assistida.
     */
    public void assistindoAula(String aula) {
        this.aulasAssistidas.add(aula);
    }

    /**
     * Método que retorna a relação de aulas assistidas pelo aluno.
     * @return String contendo a lista de aulas separadas por vírgula.
     */
    public String relacaoAulas() {
        return String.join(", ", this.aulasAssistidas);
    }

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Informe o nome:");
        String nome = leitor.next();

        System.out.println("Informe a idade:");
        int idade = leitor.nextInt();

        System.out.println("Informe o curso:");
        String curso = leitor.next();

        aluno4 aluno = new aluno4(nome, idade, curso);

        aluno.assistindoAula("Java");
        System.out.println("Informe o nome de quem cumprimenta:");
        String nomeCumprimento = leitor.next();

        System.out.println(aluno.saudacao(nomeCumprimento));

        aluno.assistindoAula("POO");
        aluno.assistindoAula("Java");
        aluno.assistindoAula("HTML");

        System.out.println("Aulas assistidas: " + aluno.relacaoAulas());

        leitor.close(); // Fechando o Scanner para evitar desperdício de recursos
    }
}
