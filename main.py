def factorial(n):
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Введите число: "))
    print(f"Факториал {num} равен {factorial(num)}")