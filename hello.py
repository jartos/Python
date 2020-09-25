# This program says hello and asks for my name.

print('Mikä sinun nimesi on?')    #Ask for their name
myName = input()
print('Hauska tavata ' + myName + '!')
print('Nimesi pituus on ' + str(len(myName)) + ' kirjainta.')
print('Kuinka vanha olet?')     #Ask for their age
myAge = input()
print('Vuoden päästä olet ' + str(int(myAge) + 1) + ' vuotta vanha.')
