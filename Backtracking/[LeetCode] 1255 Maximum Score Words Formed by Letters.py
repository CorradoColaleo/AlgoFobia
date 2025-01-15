import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int numTilePossibilities(String tiles) {
        Set<String> result = new HashSet<>(); // Usa un Set per evitare duplicati
        backtracking(result, tiles, "", new boolean[tiles.length()]);
        return result.size();
    }

    public void backtracking(Set<String> result, String tiles, String temp, boolean[] used) {
        if (!temp.isEmpty()) {
            System.out.println(temp);
            result.add(temp); // Aggiungi al set se `temp` non è vuoto
        }

        for (int i = 0; i < tiles.length(); i++) {
            if (used[i]) {
                continue; // Salta se la lettera è già stata usata in questa permutazione
            }
            // Salta duplicati consecutivi (necessario solo se i caratteri sono ordinati)
            if (i > 0 && tiles.charAt(i) == tiles.charAt(i - 1) && !used[i - 1]) {
                continue;
            }

            used[i] = true; // Marca come usato
            backtracking(result, tiles, temp + tiles.charAt(i), used); // Aggiungi lettera
            used[i] = false; // Ripristina stato per il backtracking
        }
    }
}
