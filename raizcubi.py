def raiz_cubica(numero):
    return numero ** (1/3)
try:
    numero = float(input("ingrese un numero: "))
    resultado = raiz_cubica(numero)
    print(f"raiz cubica de {numero} es aproximadamente {resultado:.4f}")
except ValueError:
    print("numero invalido")