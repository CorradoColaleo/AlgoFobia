def zero_matrix(a):
    n = len(a)
    m = len(a[0])

    ans = 0
    d = [-1] * m
    d1 = [0] * m
    d2 = [0] * m
    st = []

    for i in range(n):
        # Aggiorna la lista `d` per tenere traccia delle righe più vicine con un valore 1
        for j in range(m):
            if a[i][j] == 1:
                d[j] = i

        # Trova il limite sinistro per ogni colonna
        for j in range(m):
            while st and d[st[-1]] <= d[j]:
                st.pop()
            d1[j] = -1 if not st else st[-1]
            st.append(j)
        st.clear()

        # Trova il limite destro per ogni colonna
        for j in range(m - 1, -1, -1):
            while st and d[st[-1]] <= d[j]:
                st.pop()
            d2[j] = m if not st else st[-1]
            st.append(j)
        st.clear()

        # Calcola l'area massima del rettangolo possibile
        for j in range(m):
            height = i - d[j]  # Altezza del rettangolo
            width = d2[j] - d1[j] - 1  # Larghezza del rettangolo
            ans = max(ans, height * width)

    return ans



print(zero_matrix([[0,1,1,0,1,1,0],[0,0,0,0,0,1,0],[1,0,0,0,0,0,1],[0,1,0,0,0,0,1],[1,1,0,0,0,1,0],[1,1,0,1,1,0,0]]))