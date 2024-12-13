def nwd(a, b):
    print(f'Wywołanie funkcji nwd({a}, {b})')
    if b == 0:
        print(f'Powrót: nwd({a}, {b}) = {a}')
        return a
    else:
        result = nwd(b, a % b)
        print(f'Powrót: nwd({a}, {b}) = {result}')
        return result

# Wprowadzenie liczb przez użytkownika
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

# Obliczanie NWD
print(f'Największy Wspólny Dzielnik (NWD) {a} i {b} to {nwd(a, b)}')
