"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for
Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
bytes. The user would keep the encrypted message and the encryption key in different locations, and without both
"halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the
password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The
balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt
(right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the
plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original
text.
"""
import numpy as np

def freq_analysis(l):
    dic_frec = {}
    for i in range(len(l)):
        if l[i] in dic_frec:
            dic_frec[l[i]] += 1
        else:
            dic_frec[l[i]] = 1
    return dic_frec


def xor_vigenere(msg, len_key):
    key = [ord(" ") for i in range(len_key)]
    for i in range(len_key):
        l = encrypted[i::3]
        dic = {x: l.count(x) for x in l}
        key[i] ^= max(dic, key=dic.get)

    decrypted = (msg[char] ^ key[char%3] for char in range(len(msg)))
    return(sum(decrypted))



if __name__ == "__main__":
    with open("p059_cipher.txt") as file:
        encrypted = [int(elem) for elem in file.read().split(',')]
    # print(encrypted)
    # print(len(encrypted))
    # print(ord('a'), ord('z'))  # the key consists of 3 characters in the interval [97;122]
    # print(xor_vigenere(encrypted, 3))

    l1 = encrypted[0::3]
    l2 = encrypted[1::3]
    l3 = encrypted[2::3]

    print(l1)
    print(l2)
    print(l3)

    fl1 = freq_analysis(l1)
    fl2 = freq_analysis(l2)
    fl3 = freq_analysis(l3)

    el1 = max(fl1, key=fl1.get)
    el2 = max(fl2, key=fl2.get)
    el3 = max(fl3, key=fl3.get)
    print(el1, el2, el3)

    # avec une analyse manuelle des fréquences et en réfléchissant un peu, on part du principes que les caractères qui ont
    # une fréquence maximale ne sont pas le e mais les espaces

    decr1 = [int(elem) ^ 101 for elem in l1]
    decr2 = [int(elem) ^120 for elem in l2]
    decr3 = [int(elem)^112 for elem in l3]

    decrypted = []
    for i in range(len(decr2)):
        decrypted.append(decr1[i])
        decrypted.append(decr2[i])
        decrypted.append(decr3[i])

    decrypted_msg = ""
    for elem in decrypted:
        decrypted_msg += chr(elem)

    print(decrypted_msg)
    print(sum(decrypted))




    # Pour le reste : https://www.bibmath.net/crypto/index.php?action=affiche&quoi=poly/viganalyse
    # https://www.apprendre-en-ligne.net/crypto/vigenere/decodevig.html