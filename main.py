# In deze opdracht gaan we een aantal dingen oefenen met functies
# Ook zal je code die je eerder hebt geschreven voor een opdracht om gaan zetten
# naar functies, zodat deze eventueel makkelijker gebruikt kunnen worden

# In opdracht 2 hebben jullie een fizzbuzz programma geschreven
# We konden daarin de % operator gebruiken om te controleren of getal X
# volledig deelbaar was door getal Y.
# Schrijf een functie die deze controle voor jou uitvoert. Wat heb je hier voor nodig?
#Een functie die, wanneer opgeroepen, de eerst   #ingevoerde waardes deelt met de 
#tweede ingevoerde waarde. 
#Vervolgens controleert een if-statement of het #resultaat hiervan nul is. 
#Indien dit het geval is, is x dus deelbaar door y.
# > Wat ga je de functie meegeven?
# > Wat gaat de functie teruggeven?
# > Wat gebeurt er binnen de functie om van de parameters de return waarde te maken?

#def deelbaar_door(x, y):
  #if x % y == 0:
    #return True
  #else:
    #return False

#print(deelbaar_door(15, 4))

# Als uitkomst zouden we dus iets willen kunnen doen als:

# print(fullyDivisble(15,3)) # Dus, is 15 volledig deelbaar door 3?
# >>> True
# print(fullyDivisible(16,3))
# >>> False

# We hebben het ook kort gehad over functie compositie, dus het combineren van
# functies om ingewikkelder gedrag voor elkaar te krijgen
# > Maak een functie die het hele fizzbuzz programma voor je kan uitvoeren. Maak hiervoor
# gebruik van de functie die je bij de vorige opdracht hebt geschreven

#def deelbaar_door(getal):
#  if getal % 3 == 0 and getal % 5 == 0:
#    print('Fizzbuzz')
#  elif getal % 5 == 0:
#    print('Buzz')
#  elif getal % 3 == 0: 
#    print('Fizz')
#  else:
#    print('Geen fizzbuzz :(')

# deelbaar_door(int(input('Voer een getal in')))

# Voorbeeld output:

# print(fizzbuzz(12))
# >>> Fizz
# print(fizzbuzz(15))
# >>> Fizzbuzz
# print(fizzbuzz(20))
# >>> Buzz
# print(fizzbuzz(4))
# >>> 4

# In opdracht 3 hebben we bijvoorbeeld laten printen hoe vaak elke klinker in een 
# gegeven stuk tekst voorkwam. Hiervoor maakten we gebruik van string.count(klinker) functie
# Deze moesten we alleen iedere keer handmatig 5 keer uitschrijven - en als we dit willen
# printen voor een ander stuk tekst moet je ze nóg een keer 5 keer uitschrijven. Daar kunnen
# we een functie voor maken!

# Schrijf een functie die een stuk tekst meekrijgt, en dan voor die tekst afdrukt hoe vaak
# elke klinker voorkomt.
# Bedenk weer goed wat deze functie mee moet krijgen en wat deze gaat teruggeven. 
# Voorbeeld output:


# print(telKlinkers(tekst))
# >>> A komt 5 keer voor
# >>> U komt 2 keer voor
# >>> O komt 12 keer voor
# >>> E komt 6 keer voor
# >>> I komt 0 keer voor


def aantal_klinkers(text):
  text.lower()
  print(f"De letter a komt {text.count('a')} keer voor.")
  print(f"De letter u komt {text.count('u')} keer voor.")
  print(f"De letter u komt {text.count('o')} keer voor.")
  print(f"De letter u komt {text.count('e')} keer voor.")
  print(f"De letter u komt {text.count('i')} keer voor.")

aantal_klinkers(input('Voer een string in'))