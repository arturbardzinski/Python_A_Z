from name_function import get_formated_name

print("Wpisz 'q' aby wyjść.")
while True:
  first = input("\nPodaj imię: ")
  if first == "q":
    print("\n===Koniec programu===")
    break
  last = input("\nPodaj nazwisko: ")
  if last == "q":
    print("\n===Koniec programu===")
    break
  
  formatted_name = get_formated_name(first, last)
  print(f"\n\t>>> Sformatowane imie i nazwisko: {formatted_name}")