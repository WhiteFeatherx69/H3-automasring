Besked = "Hej verden"
print(Besked + "!")

navn = input("Hvad hedder du: ")
print("Hej " + navn + "!")

alder = int(input("Hvor gammel er du: "))

if alder >= 18:
    print("Du er over 18")
else:
    print("Du er under 18 år")

tal = 0
while tal < alder:
    tal = tal + 1
    print(tal)

for tal in range(1, alder + 1):
    print(tal)
