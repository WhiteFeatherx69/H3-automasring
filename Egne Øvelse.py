from selectors import SelectSelector

Besked = "Hej verden"
print(Besked + "!")

navn = input("Hvad Hedder du: ")
print("Hej " + navn + "!")


alder = int(input("Hvor gammel er du: "))

if alder >= 18:
    print("Du er over 18")
else :
    print("Du er under 18")


