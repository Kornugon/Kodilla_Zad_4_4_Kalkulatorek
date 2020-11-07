"""
Zadanie: kalkulator
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

# Komentarz od Piotra :)
# w tym zadaniu komentarze i "printy" specjalnie piszę w PL :)
# wartości miały byc pobrane przez "input" więc nie stosowałem *args ani **kwargs
# przy "błędnych" inputach ponawiam operacje - tak for fun w sumie :)
# nie wiem szczerze czy to ok (po pythonowemu :) ) ale jakoś działa :)
# nie przepadam za softem, który ma błąd i "stoi" (pomijajac tu logowanie) dlatego dalem opcję poprawienia wpisanych wartości jeśli są nie ok
# choc np przy dzieleniu chyba nie czyści listy i coś jest nie ok :P
# dla dobrych danych od poczatku dziala spoko
# dodatkowo zamiana przecinka na kropkę + str na int lub float

import logging
logging.basicConfig(format='%(levelname)s:%(asctime)s: %(message)s', level=logging.DEBUG)

variables = []
math_operation = 0


def is_int(str):
  # sprawdzenie czy int
    try:
        int(str)
        return True
    except ValueError:
        return False


def is_int_or_float(str):
  # sprawdzenie czy int albo float
    try:
        float(str) or int(str)
        return True
    except ValueError:
        return False


def dot_var(a):
  # zamiana przecinka na kropkę - w sumie to nie wiem po co z tego zrobilem funkcję :D
  dot_text = []
  var_ok = []

  for text in a:
    dot_sep_text = text.replace(",", ".")
    dot_text.append(dot_sep_text)
  
  # sprawdzenie czy podany tekst może być liczbą
  for text in dot_text:
    if is_int_or_float(text):
      var_ok.append(1)
    else:
      var_ok.append(0)

  return var_ok, dot_text


def operation():
  """
  Function of operation choosing.
  If selected operation is out of range - repeat.
  """
  while True:
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    str_operation = input("Chcę wykonać operację numer: ")
    if not is_int(str_operation): #sprawdzenie czy int
      logging.warning("Błędny kod działania.\n")
      continue
    else:
      math_operation = int(str_operation)

    if math_operation < 1 or math_operation > 4:
      logging.warning("Działanie poza zakresem.\n")
      continue #ponowne wywołanie bez przerywania programu - czyli wybierz operacje jeszcze raz
    else:
      math_operation = int(str_operation)
      break
  return math_operation


def user_var():
    """
    Function for getting user variables - for adding and multiply only.
    If there is just one variable - repeat.
    """
    while True:
      user_text = input("Podaj liczby do działania rozdzielone spacją: ")
      splited_text = user_text.split(' ')
      variables = []
      var_ok, dot_text = dot_var(splited_text) #zamiana przecinka na kropkę
    
      # Jeśli jakaś "wartość jest "textem" lub tylko jedna liczba
      if not all(var_ok):
        logging.warning("Wpisano tekst nie liczbę.\n")
        continue #ponowne wywołanie bez przerywania programu - czyli wpisz wiecej niż jedną liczbę
      elif len(dot_text) < 2:
        logging.warning("Wpisano tylko jedną liczbę.\n")
        continue #ponowne wywołanie bez przerywania programu - czyli wpisz wiecej niż jedną liczbę

      # zamiana tekstu na liczbę
      for txt in dot_text:
        variables.append(float(txt) if '.' in txt else int(txt)) #zamiana stringa na int lub float

      # wyjscie z petli while
      if len(dot_text) == len(variables):
        break

    logging.info(f"Podane liczby to: {variables}")
    return variables


def user_var_second():
    """
    Function for getting user variables - for subtraction and division only.
    If there is just one variable - repeat.
    """
    while True:
      # tutaj chce by po podaniu blednej 1 liczby nie pytal o 2 liczbe
      first = input("Podaj pierwszą liczbę działania: ")
      first = first.replace(",", ".")

      # sprawdzenie czy podany tekst może być liczbą
      if is_int_or_float(first):
        break
      else:
        logging.info("Pozycja pierwsza - nieprawidłowa.\n")
        continue #ponowne wywołanie bez przerywania programu - czyli wpisz wiecej niż jedną liczbę


    while True:
      # definicja 2 liczby po petli sprawdzajacej poprawnosc pierwszej liczby
      second = input("Podaj drugą liczbę działania: ")
      second = second.replace(",", ".")

      # sprawdzenie czy podany tekst może być liczbą
      if is_int_or_float(second) and second != "0":
        break
      else:
        logging.info("Pozycja druga - nieprawidłowa.\n")
        continue #ponowne wywołanie bez przerywania programu - czyli wpisz wiecej niż jedną liczbę


    while True:
      # definicja listy gdy obie liczby sa ok
      var = [first, second]

      # zamiana tekstu na liczbę
      for txt in var:
        variables.append(float(txt) if '.' in txt else int(txt)) #zamiana stringa na int lub float

      # wyjscie z petli while
      if len(var) == len(variables):
        break

    logging.info(f"Podane liczby to: {variables}")
    return variables



def adding(a):
    """
    Self commented function - adding :)
    """
    result = sum(a)
    return result

def subtract(a):
    """
    Self commented function - subtraction :)
    """
    result = a[0] - a[1]
    return result

def multiply(a):
    """
    Self commented function - multiply :)
    """
    import math
    result = math.prod(a)
    return result

def division(a):
    """
    Self commented function - division :)
    """
    result = a[0] / a[1]
    return result



while True:
    variables = [] # czyszczenie wynikow na poczatku petli
    math_operation = operation()
    if math_operation == 1:
        logging.debug("Wykonujesz dodawanie:")
        variables = user_var()
        print(f"Wynik dodawania to: {adding(variables)}")
    elif math_operation == 2:
        logging.debug("Wykonujesz odejmowanie:")
        variables = user_var_second()
        print(f"Wynik odejmowania to: {subtract(variables)}")
    elif math_operation == 3:
        logging.debug("Wykonujesz mnożenie:")
        variables = user_var()
        print(f"Wynik mnozenia to: {multiply(variables)}")
    elif math_operation == 4:
        logging.debug("Wykonujesz dzielenie:")
        variables = user_var_second()
        print(f"Wynik dzielenia to: {division(variables)}")
    

    again = input("\nJeszcze raz? [Y/any] ").capitalize()

    if again == "Y":
      continue
    else:
      break