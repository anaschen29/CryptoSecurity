# pip install rsa
import rsa
import math
EXPONENT = 5
KEYSIZE = 2048


def generate_keys():
    return rsa.newkeys(KEYSIZE, exponent=EXPONENT)

# Encrypt without padding
def insecure_encrypt(pub_key, msg):
    payload = rsa.transform.bytes2int(msg)
    encrypted = rsa.core.encrypt_int(payload, pub_key.e, pub_key.n)
    keylength = rsa.common.byte_size(pub_key.n)
    block = rsa.transform.int2bytes(encrypted, keylength)
    return block

# Code used to generate files
def gen_icrt_attack(msg):
    keys = [generate_keys() for _ in range(EXPONENT)]
    ciphertexts = [insecure_encrypt(k[0], msg) for k in keys]
    as_nums = [rsa.transform.bytes2int(c) for c in ciphertexts]
    moduli = [k[0].n for k in keys]
    kf = open("keys.txt", "w")
    kf.writelines([str(pk) + "\n" for pk in moduli])
    cf = open("ciphertexts.txt", "w")
    cf.writelines([str(c) + "\n" for c in as_nums]) 

def broadcast_attack():
    kf = open("keys.txt")
    cf = open("ciphertexts.txt")
    moduli = [int(k) for k in kf.readlines()]
    as_nums = [int(c) for c in cf.readlines()]
    # TODO: your attack
    r = 0


    # Print out string for answer
    print(str(rsa.transform.int2bytes(r)))

# broadcast_attack()

with open("Downloads/public3/keys.txt") as kf:
    moduli=[int(k) for k in kf.readlines()]

with open("Downloads/public3/ciphertexts.txt") as cf:
    ciphers = [int(c) for c in cf.readlines()]
print(ciphers)

def find(i):
    N=moduli[i]
    prod=1
    for j in range(5):
        if j!=i:
            prod*=moduli[j]
    k=pow(prod, -1, N)    
    return prod*k

P=1
for mod in moduli:
    P*=mod
total=0
for i in range(5):
    total+=find(i)*ciphers[i]
total=total%P
# print(total, math.log(total)/math.log(10))

#number of digits floor(log())+1 = 696

lower=int(1.55194*10**139)
upper=int(1.55199*10**139)

# lower=2
# upper=100
# total=229345007
counter=0
while True:
    
    if counter==1000:
        break
    mid = (lower + upper)//2
    if mid**5==total:
        print('ANSWER FOUND', mid)
        print(counter)
        break
    elif mid**5>total:
        upper = mid + 1   
    else:                     
        lower = mid - 1 
    counter+=1

print(str(rsa.transform.int2bytes(mid)))