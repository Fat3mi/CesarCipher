class CesarCode:
    def __init__(self, code, text):
        self.code = code
        self.text = text

    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                'm': 12,
                'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
                'y': 24,
                'z': 25}

    def encryption(self):
        cipher_text = ''

        for t in self.text:
            if t == ' ':
                cipher_text += ' '
            else:
                new = self.alphabet.get(t) + self.code
                if new > 25:
                    newrec = new - 26
                    for k, v in self.alphabet.items():
                        if v == newrec:
                            cipher_text += k
                else:
                    for k, v in self.alphabet.items():
                        if v == new:
                            cipher_text += k

        return cipher_text

    def decryption(self):
        key = (25 - self.code) + 1

        plain_text = ''

        for t in self.text:
            if t == ' ':
                plain_text += ' '
            else:
                new = self.alphabet.get(t) + key
                if new > 25:
                    newrec = new - 26
                    for k, v in self.alphabet.items():
                        if v == newrec:
                            plain_text += k
                else:
                    for k, v in self.alphabet.items():
                        if v == new:
                            plain_text += k

        return plain_text


cesar_calc = input('Welcome im omid fatemi \n choose -> Encryption / e Or Decryption / d :')
itrate = int(input('please insert your encoding number (1~25) :'))
input_text = input('write your text for encryption : \n')

if cesar_calc == 'e':
    if itrate <= 25 and itrate >= 1:
        ce = CesarCode(itrate, input_text)
        print(ce.encryption())

    else:
        print('wrong number')
elif cesar_calc == 'd':
    cd = CesarCode(itrate, input_text)
    print(cd.decryption())

else:
    print('wrong choose ! try again')
