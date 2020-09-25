# Etsii puhelinnumeron ja sähköpostiosoitteen

import pyperclip, re

phoneRegex = re.compile(r'''(
        
        (\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))? 

                                # (\d{3}) operaattorin tunnus / alkuosa
                                # (\s|-|\.)? erotin merkki tai väli
                                # (\d{7}) numerot (7)
        )''', re.VERBOSE)

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+              # käyttäjänimi
        @                              # @-symboli
        [a-zA-Z0-9.-]+                 # domainin nimi
        (\.[a-zA-Z]{2,4}               # piste (.) + loppuosa
        )''', re.VERBOSE)


# Etsi leikepöydän tekstistä.

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
                phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
for groups in emailRegex.findall(text):
        matches.append(groups[0])


# Kopioi tulokset leikepöydälle.

if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
else:
        print('No phone numbers or email addresses found.')


