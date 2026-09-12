def calcular_promedio(nota1, nota2):
    suma = nota1 + nota2
    promedio = suma / 2
    return promedio


if __name__ == "__main__":
    calificacion1 = 85.0
    calificacion2 = 90.0
    resultado = calcular_promedio(calificacion1, calificacion2)
    print(f"El promedio de las notas es: {resultado}")