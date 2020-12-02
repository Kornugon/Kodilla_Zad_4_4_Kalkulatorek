"""
Zadanie 4.4: kalkulator
Załóżmy, że będzie przyjmował zawsze dwie liczby do obliczeń.

Po uruchomieniu programu jesteśmy pytani o typ obliczenia

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:
Następnie pobieramy dwie wartości liczbowe.

Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).
Następnie wykonujemy obliczenie i drukujemy rezultat z print.

Do pobierania wartości użyj input. Nie ma potrzeby sprawdzania, czy podane argumenty są liczbami, przewidujemy poprawne uzupełnienie.
Przykładowe wywołanie razem z wartościami wybranymi przez użytkownika może wyglądać tak:

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
Podaj składnik 1. 2.3
Podaj składnik 2. 5.4
Dodaję 2.30 i 5.40
Wynik to 7.70


Dla chętnych
Jeśli chcesz usprawnić swoje zadanie, możesz dodać dwa rozszerzenia:

Sprawdzaj, czy podana wartość na pewno jest liczbą.
W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów niż tylko dwa, np. możesz dodać do siebie trzy i więcej liczb.
"""

#chyba najbardziej podstawowa wesja według opisu zadania
#rozwazanie z "argparse" bardziej mi sie podoba :)
#swoje wcześniejsze zostawiam w wcześniejszym commicie


import logging
logging.basicConfig(format='%(levelname)s:%(asctime)s: %(message)s', level=logging.DEBUG)

def operation():

  action = ""
  result = 0

  str_operation = input("Choose action from the following: sum, sub, mul, div: ")
  number_1 = float(input("Enter first number: "))
  number_2 = float(input("Enter second number: "))

  if str_operation == "div" and number_2 == 0:
    logging.error("Divide by 0")
    number_2 = float(input("Enter second number again: "))

  if str_operation == "sum":
    action = "addition"
    result = number_1 + number_2
  elif str_operation == "sub":
    action = "subtraction"
    result = number_1 - number_2
  elif str_operation == "mul":
    action = "multiplication"
    result = number_1 * number_2
  elif str_operation == "div":
    action = "division"
    result = number_1 / number_2
  
  logging.info(f"Your action is: {action}")  #miało być info z loggingu :)

  print(f"For arguments {number_1} and {number_2} result of {action} is {result}")


if __name__ == '__main__':
  operation()