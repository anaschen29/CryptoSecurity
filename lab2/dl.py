import secrets
import math



G = 2
# Not a very secure prime - don't use this for anything
P = 115792089237316195423570985008687907853269984665640564039457584007913129870127

# For your testing - generates a random short discrete log
def gen_random_instance(numbits=48):
    m = secrets.randbits(numbits)
    x = pow(G, m, P)
    return (m, x)

def read_inputs():
    with open("/Users/anaschentouf/Desktop/Spring 2023/6.5610/public/inputs.txt", "r") as f:
        return [int(v) for v in f.readlines()]


def my_attack(x,numbits):
    
    m=2**24   
    #Hash Table
    hash_table = {pow(G, i, P)%P: i for i in range(m)} 
    print('hash complete')          
    gamma = pow(G, m *(P - 2), P) % P #Fermat   
    
    print('checking')        
    for index in range(m):         
        y = (x * pow(gamma, index, P)) % P
        
        if y in hash_table:          


            collision=hash_table[y]         

            return index*m+collision                  
        

print('hi')
if __name__ == "__main__":
    numbits = 48
    m, x = gen_random_instance(numbits)
    print('generated')
    a = my_attack(x, numbits)
    if a != m:
        print(a,m,"Fail :(")
    else:
        print("Pass :)")
        ID = 911086967
        i = ID % 1000
        x = read_inputs()[i]
        print(my_attack(x, numbits))
        x = read_inputs()[i]