class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Lista di tuple per memorizzare il numero e il suo indice
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # Array per memorizzare i risultati
        result = [0] * len(nums)

        # Funzione di merge che conta gli elementi più piccoli a destra
        def merge_and_count(arr, temp_arr, left, mid, right):
            i = left    # Indice per la parte sinistra
            j = mid + 1 # Indice per la parte destra
            k = left    # Indice per l'array temporaneo
            count = 0   # Conteggio degli elementi più piccoli

            while i <= mid and j <= right:
                if arr[i][0] <= arr[j][0]:
                    temp_arr[k] = arr[i]
                    result[arr[i][1]] += count  # Aggiorna il risultato per il numero di elementi a sinistra
                    i += 1
                else:
                    temp_arr[k] = arr[j]
                    count += 1 # Elemento a destra è più piccolo
                    j += 1
                k += 1

            # Copia gli elementi rimanenti
            while i <= mid:
                temp_arr[k] = arr[i]
                result[arr[i][1]] += count  # Aggiorna il risultato per il numero di elementi a sinistra
                i += 1
                k += 1

            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1

            # Copia l'array temporaneo nell'array originale
            for i in range(left, right + 1):
                arr[i] = temp_arr[i]

        def merge_sort_and_count(arr, temp_arr, left, right):
            if left < right:
                mid = (left + right) // 2

                # Chiama ricorsivamente per la parte sinistra e destra
                merge_sort_and_count(arr, temp_arr, left, mid)
                merge_sort_and_count(arr, temp_arr, mid + 1, right)

                # Merge le due parti e conta gli elementi
                merge_and_count(arr, temp_arr, left, mid, right)

        # Array temporaneo
        temp_arr = [0] * len(nums)
        merge_sort_and_count(indexed_nums, temp_arr, 0, len(nums) - 1)

        return result
