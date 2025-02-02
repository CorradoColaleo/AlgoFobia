import math 

def function(p, q, r, s, t, u, x):    
    y = p * math.exp(-1 * x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * math.pow(x, 2) + u
    return y

def find_x(p, q, r, s, t, u, start=0, end=1):
    
    punto_medio = (start + end) / 2
    y_media = function(p, q, r, s, t, u, punto_medio)
    
    # Aggiungi stampe di debug
    print(f"Start: {start}, End: {end}")
    print(f"Punto Medio: {punto_medio}")
    print(f"y({punto_medio}) = {y_media}")
    print("-" * 40)
    
    # Controllo se il valore è vicino a zero
    if round(y_media, 4) == 0:
        print("Trovato un punto con y ~ 0")
        return punto_medio  # Restituisci il valore di x che rende y quasi zero
    elif round(y_media, 4) > 0:
        return find_x(p, q, r, s, t, u, start=punto_medio + 0.0001, end=end)
    else:
        return find_x(p, q, r, s, t, u, start=start, end=punto_medio - 0.0001)

if __name__ == "__main__":
    p, q, r, s, t, u = map(int, input("Inserisci i valori di p, q, r, s, t, u separati da uno spazio: ").split())
    try:
        risultato = find_x(p, q, r, s, t, u)
    except RecursionError:
        risultato = None
    print(f"Il valore di x trovato è: {risultato}")
