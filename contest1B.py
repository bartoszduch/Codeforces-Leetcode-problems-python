# Wczytaj dwie liczby a i b jako parę liczb oddzielonych spacją
a, b = map(int, input().split())

# Inicjuj zmienną max na początkową wartość a + b
max_value = a + b

# Sprawdź, czy można uzyskać większą wartość przez mnożenie
if max_value < a * b:
    max_value = a * b

# Sprawdź, czy można uzyskać większą wartość przez odejmowanie
if max_value < a - b:
    max_value = a - b

# Sprawdź, czy można uzyskać większą wartość przez dzielenie
if b != 0 and max_value < a / b:
    max_value = a / b

# Wydrukuj maksymalną wartość
print(max_value)