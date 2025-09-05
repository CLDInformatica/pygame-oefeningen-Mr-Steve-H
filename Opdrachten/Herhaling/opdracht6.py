# Maak een functie genaamd rekenmachine met 3 argumenten:

#   - getal1
#   - getal2
#   - operatie

# De operatie kan plus, min, keer of delen zijn. 

# Doe iets met getal1 en getal2 afhankelijk van de operatie en return het resultaat.
# Dus als operatie plus is tel je de 2 getallen bij elkaar op, enz.
# Voer hierna de functie uit met verschillende inputs en bekijk de resultaten.
# Let op: Het is verplicht om een functie te gebruiken!

def Rekenmachine(getal1, getal2, operatie):
   if operatie == 'plus':
    return getal1 + getal2
   elif operatie == 'min':
    return getal1 - getal2
   elif operatie == 'keer':
    return getal1 * getal2
   elif operatie == 'delen':
    return getal1 // getal2
   else:
    print('Dat is geen geldige operatie')

print(Rekenmachine(2, 5, 'keer'))
print(Rekenmachine(10, 2, 'delen'))