def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        print('Nie wolno dzielić przez zero!')

while True:
    print('Mozliwe operacje: dodawanie, odejmowanie, mnozenie, dzielenie. Aby wyjsc wpisz: wyjscie')

    operacja = input('Wybierz operacje: ')

    if operacja == 'wyjscie':
        break

    try:
        x = float(input('Podaj pierwszą liczbę: '))
        y = float(input('Podaj drugą liczbę: '))
    except ValueError:
        print('Proszę podać prawidłową liczbę')
        continue

    if operacja == 'dodawanie':
        print(dodawanie(x, y))
    elif operacja == 'odejmowanie':
        print(odejmowanie(x, y))
    elif operacja == 'mnozenie':
        print(mnozenie(x, y))
    elif operacja == 'dzielenie':
        print(dzielenie(x, y))
    else:
        print('Nieznana operacja')
