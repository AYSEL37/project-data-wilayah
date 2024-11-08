import os
import random
import string
data = dict()
while True:
    os.system("cls") # WIN
    # os.system("clear") # mac/linux
    print(f" {'DATA WILAYAH INDONESIA':🤍^45}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    PULAU = input("Enter PULAU\t\t:")
    PROVINSI = input("Enter PROVINSI\t\t:")
    KOTA = input("Enter KOTA\t:")
    data[ keyFinal ] = { keyFinal : { 'PULAUkey' : PULAU, 'PROVINSIkey' : PROVINSI,'KOTAkey' : KOTA } }
    
    opsi = input("input data LAGI (y/t) :").lower()
    if opsi == 't':
        break

print("-"*40)
print(f"Key\t PULAU\tPROVINSI\t KOTA")
print("-"*40)
for key, value in data.items():
    print(f"{key}.\t {data[key]['PULAUkey']}\t {data[key]['PROVINSIkey']}\t \t{data[key]['KOTAkey']}") 