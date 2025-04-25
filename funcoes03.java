import java.time.LocalTime;
import java.util.Scanner;

public class funcoes03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        String saudacao = obterSaudacao(); 

        System.out.println(saudacao + nome + "!");
        scanner.close();
    }

    public static String obterSaudacao() {
        int horaAtual = LocalTime.now().getHour();

        if (horaAtual >= 5 && horaAtual <= 12) {
            return "Bom dia, ";
        } else if (horaAtual >= 12 && horaAtual <= 18) {
            return "Boa tarde, ";
        } else if (horaAtual >= 18 && horaAtual <= 24) {
            return "Boa noite, ";
        } else {
            return "Vai dormir, ";
        }
    }
}