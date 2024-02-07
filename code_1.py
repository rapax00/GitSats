def special_sum(numbers):
    """Calcula la suma de números pares y multiplica los impares por su índice, revelando palabras ocultas si se hace correctamente."""
    even_sum = 0
    odd_product = 1
    for i, number in enumerate(numbers):
        if number % 2 == 0:
            even_sum += number
        else:
            odd_product *= number * i
    
    if even_sum > 50 and odd_product < 1000:
        print("La suma especial y el producto revelan: PIONERO")
    elif even_sum <= 50:
        print("La suma de los pares debe superar 50 para revelar las palabras.")
    else:
        print("El producto de los impares debe ser menor que 1000 para encontrar las pistas.")

    return even_sum, odd_product

numbers = [1, 2, 3, 4, 5, 6, 7]
resultado = special_sum(numbers)
print("Resultado de la suma especial y el producto:", resultado)
