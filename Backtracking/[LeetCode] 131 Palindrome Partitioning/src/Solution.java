import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        List<String> current = new ArrayList<>();
        backatracking(result, current, s);
        return result;
    }

    public boolean areAllPalindromes(List<String> current) {
        for (String str : current) {
            if (!isPalindrome(str)) {
                return false; // Se una stringa non è palindroma, restituisci false
            }
        }
        return true; // Tutte le stringhe sono palindromi
    }
    
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false; // Se i caratteri non corrispondono, non è un palindromo
            }
            left++;
            right--;
        }
        return true; // La stringa è un palindromo
    }

    public void process_solution(List<List<String>> result, List<String> current){
        List<String> copy = new ArrayList<>(current);
        result.add(copy);
    }

    public void construct_candidates(List<String> current, String s, String[] c, AtomicInteger n) {
        boolean[] used = new boolean[s.length()];
        List<Character> characterList = new ArrayList<>();
    
        // Creiamo una lista di caratteri basata sulla lista corrente
        for (String str : current) {
            for (char character : str.toCharArray()) {
                characterList.add(character);
            }
        }
    
        // Riempiamo l'array used in base ai caratteri già utilizzati
        for (int i = 0; i < characterList.size(); i++) {
            if (s.charAt(i) == characterList.get(i)) {
                used[i] = true;
            }
        }
    
        int index = 0;
        for (int i = 0; i < used.length; i++) {
            if (!used[i]) {
                c[index] = String.valueOf(s.charAt(i));
                index++;
                n.set(n.get() + 1);
                
                // Assicuriamoci che non superiamo i limiti dell'array
                if (i < used.length - 1 && !used[i + 1]) {
                    c[index] = String.valueOf(s.charAt(i)) + String.valueOf(s.charAt(i + 1));
                    n.set(n.get() + 1);
                    index++;
                    
                    // Usando un ciclo mentre con controllo adeguato
                    int u = 2; // Puoi cambiare il valore di u a seconda delle tue necessità
                    while (i + u < used.length && !used[i + u]) {
                        c[index] = c[index - 1] + String.valueOf(s.charAt(i + u));
                        n.set(n.get() + 1);
                        index++;
                        u++; // Incrementiamo u per allargare la sottostringa
                    }
                }
                break; // Uscire dal ciclo for una volta che abbiamo trovato un indice non utilizzato
            }
        }
    }
    
    
    public boolean is_finished(List<String> current,int n){
        // Verifica se la lunghezza della lista 'current' è stata riempita e se i caratteri in essa
        // corrispondono alla lunghezza della stringa originale 's'.
        // Controlla che la somma delle lunghezze delle sottostringhe in current sia uguale a n.
        int totalLength = 0;
        for (String str : current) {
            totalLength += str.length(); // Somma le lunghezze delle sottostringhe
        }
        // Se la lunghezza totale delle sottostringhe in 'current' è uguale a 'n', ritorna true.
        return totalLength == n;
    }
    
    public void backatracking(List<List<String>> result, List<String> current, String s){
        if (is_finished(current, s.length())){
            if (areAllPalindromes(current)){
                process_solution(result, current);
            }
        } else {
            String[] c = new String[s.length()];
            AtomicInteger nc = new AtomicInteger();
            construct_candidates(current, s, c, nc);
            for (int i=0;i<nc.get();i++){
                current.add(c[i]);
                backatracking(result, current, s);
                current.remove(current.size()-1);
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "AABB";  // Puoi cambiare la stringa qui per testare altre stringhe
        // Chiamata al metodo partition per ottenere le partizioni palindromiche.
        List<List<String>> partitions = solution.partition(s);
        // Stampa il risultato.
        System.out.println("Partizioni palindromiche di \"" + s + "\":");
        for (List<String> partition : partitions) {
            System.out.println(partition);
        }
    }

}
