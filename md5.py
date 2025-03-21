import hashlib
import itertools
import sys
import time

def md5_crack(target_hash, min_length=1, max_length=8):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    found_password = None
    for length in range(min_length, max_length + 1):
        print(f"\nTrying passwords of length {length}: ", end="", flush=True)
        start_time = time.time()
        total_combinations = len(characters) ** length
        progress = 0
        
        for password in generate_passwords(characters, length):
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            progress += 1
            sys.stdout.write("\rProgress for length {}: {:.2f}%".format(length, progress / total_combinations * 100))
            sys.stdout.flush()
            if hashed_password == target_hash.lower():
                found_password = password
                break
        
        print("\nTime taken for length {}: {:.2f} seconds".format(length, time.time() - start_time))
        if found_password:
            break

    if found_password:
        print(f"\nPassword cracked! The original password for length {len(found_password)} is: {found_password}")
    else:
        print("\nPassword not cracked.")

def generate_passwords(characters, length):
    for password in itertools.product(characters, repeat=length):
        yield ''.join(password)

# Beispielaufruf
target_hash = "5d1eca158c00250d9c4c32d947b7c433"
md5_crack(target_hash)