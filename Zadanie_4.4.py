
# Zadanie: kalkulator

# Czas na duże, poważne zadanie! Dojrzewasz jako programista, więc mamy coś odpowiedniego – stworzymy własny kalkulator, oczywiście nieco uproszczony. Załóżmy, że będzie przyjmował zawsze dwie liczby do obliczeń.

# Docelowo chcielibyśmy uzyskać taki efekt:

#     Po uruchomieniu programu jesteśmy pytani o typ obliczenia

#     >> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:

#     Następnie pobieramy dwie wartości liczbowe.

#     Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).

#     Następnie wykonujemy obliczenie i drukujemy rezultat z print.

# Do pobierania wartości użyj input. Nie ma potrzeby sprawdzania, czy podane argumenty są liczbami, przewidujemy poprawne uzupełnienie.

# Przykładowe wywołanie razem z wartościami wybranymi przez użytkownika może wyglądać tak:

# >> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
# Podaj składnik 1. 2.3
# Podaj składnik 2. 5.4
# Dodaję 2.30 i 5.40
# Wynik to 7.70

# Dla chętnych

# Jeśli chcesz usprawnić swoje zadanie, możesz dodać dwa rozszerzenia:

#     Sprawdzaj, czy podana wartość na pewno jest liczbą.
#     W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów niż tylko dwa, np. możesz dodać do siebie trzy i więcej liczb.

# Prześlij link do zdalnego repozytorium z zadaniem Mentorowi. Sprawisz mu frajdę!

import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def dodawanie(first_number, second_number):
    result_ = first_number + second_number
    logging.info(f"Dodaję {first_number} i {second_number}")
    return result_

def odejmowanie(first_number, second_number):
    result_ = first_number - second_number
    logging.info(f"Odejmuję {first_number} i {second_number}")
    return result_

def mnożenie(first_number, second_number):
    result_ = first_number * second_number
    logging.info(f"Mnożę {first_number} i {second_number}")
    return result_

def dzielenie(first_number, second_number):
    result_ = first_number / second_number
    logging.info(f"Dzielę {first_number} i {second_number}")
    return result_

def calculations(calculation, first_number, second_number):
    if calculation == 1:
        return dodawanie(first_number, second_number)
    elif calculation == 2:
        return odejmowanie(first_number, second_number)
    elif calculation == 3:
        return mnożenie(first_number, second_number)
    elif calculation == 4:
        return dzielenie(first_number, second_number)
    else:
        print("nieprawidłowy rodzaj działania")
        exit





if __name__ == "__main__":

    while True:
        calculation = int(input("Podaj działanie (1: Dodawanie, 2: Odejmowanie, 3: Mnożenie, 4: Dzielenie): "))
    
        if 1 <= calculation <= 4:  # Sprawdzamy, czy wartość jest w zakresie 1-4
            break  
        else:
            print("Wybierz poprawny typ działania!")  
       
    first_number = float(input("Podaj składnik 1.  "))
    second_number = float(input("Podaj składnik 2.  "))

    result = calculations(calculation, first_number, second_number)
    print(f"Wynik to: {result}")
    





