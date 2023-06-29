from string import ascii_letters


class CesarCode:
    def __init__(self, code, text):
        self.code = code
        self.text = text

    alphabet = ascii_letters

    def encryption(self):
        cipher_text = ''

        for t in self.text:
            if t not in self.alphabet:
                cipher_text += t
            else:
                new = (self.alphabet.index(t) + self.code) % len(self.alphabet)
                cipher_text += self.alphabet[new]

        return cipher_text

    def decryption(self):
        newcode = self.code * -1
        decrypt = CesarCode(newcode, self.text)
        return decrypt.encryption()


cesar_calc = input('Encryption / e Or Decryption / d :')
itrate = int(input('please insert your encoding number (1~51) :'))
input_text = input('write your text for encryption : \n')

if cesar_calc == 'e':
    if itrate <= 51 and itrate >= 1 and itrate != 26:
        ce = CesarCode(itrate, input_text)
        print(ce.encryption())

    else:
        print('wrong number ist cant be 0 , 26 or 52')
elif cesar_calc == 'd':
    cd = CesarCode(itrate, input_text)
    print(cd.decryption())

else:
    print('wrong choose ! try again')
