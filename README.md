# MD5-Decrypter
Dieses Skript ist selbst entwickelt und Basiert auf Random Hash von hashcat. Es ist vereinfachter und schneller und es Funktioniert ohne eine wordlist und generiert alle Buchstaben Zahlen durch.

(target_hash, min_length=1, max_length=8)

min_length = 1   minimum Passwortlänge

max_length = 8   maximum Passwortlänge

Es liegt euch Frei die characters zu ändern

    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?)%!"§$&(/=`´^*#+-.,;:_'
    
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    characters = 'abcdefghijklmnopqrstuvwxyz'
    
Ihr könnt es so designen wie Ihr es für richtig empfindet.


Aus Liebe zur Community <3 #C1D3

Mit einer der schnellsten MD5 decrypter. Nicht schneller als Hashcat aber schnell als alle anderen.


Einfach den MD5 hash unten einfügen in der zeile   target_hash = ""
danach abspeichern und python3 md5.py
