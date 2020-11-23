# arvauspeli
import random

print('Tervetuloa. Anna nimesi')
name = input()

print('Hei ' + name + '! Pelataanpa arvauspeliä. Olen arponut numeron väliltä 1-20. Arvaatko sen? Saat kuusi yritystä.')
secretNumber = random.randint(1, 20)
      
for arvaukset in range (1, 7):
      print('Arvaa numero!')
      arvaus = int(input())

      if arvaus < secretNumber:
              print('Luku on liian pieni.')
      elif arvaus > secretNumber:
              print('Luku on liian suuri.')
      else:
              break # Tässä kohtaa oikea vastaus!

if arvaus == secretNumber:
      print('Onneksi olkoon, ' + name + '! Arvasit täysin oikein! Käytit yhteensä ' + str(arvaukset) + ' arvausta.')

else:
      print('Ei osunut. Oikea numero olisi ollut ' + str(secretNumber)'.')      
