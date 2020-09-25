# Ohjelma kysyy ikäsi ja ilmoittaa ikäsi vuoden kuluttua

print('Mikä sinun nimesi on?')    #Kysy nimi
myName = input()
print('Hauska tavata ' + myName + '!')
print('Nimesi pituus on ' + str(len(myName)) + ' kirjainta.')
print('Kuinka vanha olet?')     #Kysy ikä
myAge = input()
print('Vuoden päästä olet ' + str(int(myAge) + 1) + ' vuotta vanha.')
