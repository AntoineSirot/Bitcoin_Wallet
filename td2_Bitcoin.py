import secrets
import hashlib
import binascii
import sys



def padd_binary(bin_str: str, size: int) -> str:
    """
    Pads a binary string with zeros to the left
    :param bin_str: binary string to pad
    :param size: size of the padded string
    :return: padded binary string
    """
    for _ in range(size - len(bin_str)):
        bin_str = '0' + bin_str
    return bin_str

def byte_to_binary(b: bytes, size: int) -> str:
    """
    Converts a byte to a binary string
    :param byte: byte to convert
    :param size: size of the binary string
    :return: binary string
    """
    order = -1 if sys.byteorder == 'little' else 1
    bin_n = bin(int.from_bytes(b, byteorder='big'))[2:]
    return padd_binary(bin_n, size)

Liste = {}
Liste[0] = "Créer nombre aléatoire pour Seed en base 10 et en Binaire"
Liste[1] = "Créer autre chose"
Liste[2] = "Jcp"
print(Liste)
a = int(input())
if a==0 :
  print("Bien joue")
  seed = secrets.token_bytes(16)
  binSeed = byte_to_binary(seed,128)
  print("Valeur de la seed en binaire : " + binSeed)
  print("Valeur de la seed en base 10 : " + str(int(binSeed,2)))
  hashSeed = hashlib.sha256(seed).digest()
  print("Valeur du Hash de la seed : " + str(hashSeed))
  binhashSeed = byte_to_binary(hash, 256)
  print("Valeur du Hash de la seed en binaire : " + binhashSeed)
  EntCheck = binSeed + binhashSeed[:4]
  print("Entropie + Checksum en binaire : " + EntCheck)
  Splited = ['0','0','0','0','0','0','0','0','0','0','0','0']
  for j in range(12) :
    Splited[j] = EntCheck[11*j:(j+1)*11]
  print(Splited)

  
  


elif a==1:
  print("1")
elif a==2 : 
  print("2")
