def raiz_r(n,r):
    raiz_nova = (r + n/r) /2
    if abs (raiz_nova - r) < 0.001:
        raiz_casas = f"{raiz_nova:.3f}"
        return raiz_nova
    else:
        return raiz_r(n, nova_raiz)

def raiz(n):
    return raiz_r(n, n)
