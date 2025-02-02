def minimal_sum_of_distances_for_single_case(relatives):
    # Ordiniamo gli indirizzi per trovare la mediana
    relatives.sort()

    # Troviamo la mediana (indice centrale)
    r = len(relatives)
    median = relatives[r // 2]

    # Calcoliamo la somma delle distanze dalla mediana
    total_distance = sum(abs(median - s) for s in relatives)

    # Restituiamo la distanza minima
    return f"mediana:{median}, distanza minima: {total_distance}"

print(minimal_sum_of_distances_for_single_case([4,6]))
print(minimal_sum_of_distances_for_single_case([1,1,3,5,7]))
print(minimal_sum_of_distances_for_single_case([10,20,30,40,50]))
print(minimal_sum_of_distances_for_single_case([5,5,5]))
print(minimal_sum_of_distances_for_single_case([1,2,2,3,3,100]))



