package LeetCode;
import java.util.ArrayList;
import java.util.Arrays;

class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        // Usa un ArrayList per collezionare i valori della lista collegata
        ArrayList<Integer> list = new ArrayList<>();

        ListNode current = head;

        // Trasferisci tutti i valori della lista collegata nell'ArrayList
        while (current != null) {
            list.add(current.val);
            current = current.next;
        }

        // Converti l'ArrayList in un array
        int[] nums = list.stream().mapToInt(i -> i).toArray();

        // Usa il metodo sortedArrayToBST per costruire l'albero
        return sortedArrayToBST(nums);
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        // Caso base: se l'array è vuoto, restituisci null
        if (nums.length == 0) {
            return null;
        }

        // Trova l'indice del "mid" (l'elemento radice del sottoalbero)
        int q = nums.length / 2;

        // Crea gli array per la parte sinistra e destra
        int[] leftArray = Arrays.copyOfRange(nums, 0, q);
        int[] rightArray = Arrays.copyOfRange(nums, q + 1, nums.length);

        // Chiamata ricorsiva per il sottoalbero sinistro e destro
        TreeNode left = sortedArrayToBST(leftArray);
        TreeNode right = sortedArrayToBST(rightArray);

        // Crea il nodo radice con il valore nums[q] e i sottoalberi
        return new TreeNode(nums[q], left, right);
    }
}
