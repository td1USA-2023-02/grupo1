print("hola tengo que leer")
def bernoulli(n):
    if n == 0:
        return 1
    elif n == 1:
        return -0.5
    else:
        b = [0] * (n + 1)
        b[0] = 1
        for m in range(1, n + 1):
            b[m] = 0
            for k in range(m):
                b[m] -= (comb(m, k) * b[k]) / (m - k + 1)
        return b[n]

def comb(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    else:
        result = 1
        for i in range(1, k + 1):
            result = result * (n - i + 1) // i
        return result

n = int(input("Ingrese el valor de n: "))
print(f"El número de Bernoulli B({n}) es {bernoulli(n)}")


# segunda operacion 
import math
data = [1,2,3,4,5,6,7,8,9]
for numero in data :
    resultados = math.sqrt(numero)
    print(f"la raiz de {numero} es {resultados}")
