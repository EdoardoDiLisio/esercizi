# Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. 
# Pertanto, data l'area specifica di una pagina Web rettangolare, il tuo compito ora è progettare una pagina Web rettangolare, 
# la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:
# 1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
# 2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
# 3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

# Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

# Esempio:

# construct_rectangle(4)

# L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
# Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. 
# Quindi la lunghezza L è 2 e la larghezza W è 2.

def construct_rectangle(area: float) -> list[float]:
    min_diff = area - 1  
    result = [area, 1]   
    
    for i in range(2, int(area**0.5) + 1):
        if area % i == 0:
            j = area // i
            if j >= i and j - i < min_diff:
                min_diff = j - i
                result = [j, i]

    return result
