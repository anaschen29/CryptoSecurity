# Tested with python >= 3.8.10
# import bitstring
# from bitstring import BitArray
import binascii
# read file in binary mode
def read_file(fn):
    with open(fn, "rb") as f:
        return f.read()


# A function to try a guess
def try_substitution(substitutes, cipher):
    out = ""
    for b in cipher:
        if b in substitutes:
            out += " " + substitutes[b]
        else:
            out += " " + str(b)
    return out


def frequency_analysis(input):
    freq={}
    unique=set(input)
    for elt in unique:
        freq[elt]=input.count(elt)
    return freq

def Sort_Tuple(input):
    input.sort(key = lambda inp: inp[1])
    return input

def listXOR(a,b):
    if len(a)==len(b):
        return [a[i]^b[i] for i in range(len(a))]

def find_spaces(cipher1,cipher2):
    pass




if __name__ == "__main__":
    valid_range=[bin(3)]+[bin(x) for x in range(97,123)]
    words = read_file("Desktop/Spring 2023/6.5610/public/1000_dict.txt").split()
    for i in range(len(words)):
        words[i]=words[i].decode()
    cipher1 = list(read_file("Desktop/Spring 2023/6.5610/public/c1.bin"))
    cipher2 = list(read_file("Desktop/Spring 2023/6.5610/public/c2.bin"))
    XOR=[cipher1[i]^cipher2[i] for i in range(len(cipher1))]
    print(len(cipher1))
    possible_key={}
    for i in range(len(XOR)):
        if XOR[i]>63:
            possible_key[i]=(cipher1[i]^32,cipher2[i]^32)
    for key in possible_key:
        a,b=possible_key[key]
        # print( key, 'either (',cipher1[i]^a, cipher2[i]^a, ')  or (', cipher1[i]^b, cipher2[i]^b, ')')
    # print(possible_key)
        # print(key^string1[:11])
    # print(cipher1, min(cipher1))
    # cipher2= list(read_file("Desktop/Spring 2023/6.5610/public/c2.bin"))
    # freq=frequency_analysis(cipher1)
    # freq_list = [(k, v*100/len(cipher1)) for k, v in freq.items()]
    # print(Sort_Tuple(freq_list))
    # print('______')
    # freq=frequency_analysis(cipher2)
    # freq_list = [(k, v*100/len(cipher2)) for k, v in freq.items()]
    # print(Sort_Tuple(freq_list))

    # print(read_file("Desktop/Spring 2023/6.5610/public/c1.bin")^read_file("Desktop/Spring 2023/6.5610/public/c1.bin"))
    #102, e
    #90, a
    #40, 

    # print(try_substitution({102: 'e', 90: 'a'}, cipher))
    
    valid_range=[32]+[x for x in range(97,123)]
    dict={}
    str="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        dict[i+97]=str[i]
    dict[32]=" "


    def convert(l):
        #takes list of integers
        return [dict[l[i]] for i in range(len(l))]
    
    def word(l):
        total=""
        for i in l:
            total+=i
        return total
     
    def split_list(l):
        if 32 not in l:
            return [word(l)]
        while 32 in l:
            s=32
            i=l.index(s)
            prefix=l[:i]
            suffix=l[i+1:]
            return split_list(prefix)+split_list(suffix)

    
    def valid_ones(n):
        if n==1:
            total=[]
            for a in valid_range:
                if a not in total:
                    for b in valid_range:
                        if a^b==23:
                            total.append([a])
        
        
        for valid in prev_valid:
            for suffix in valid_range:
                if suffix==32:
                    pass

    
    def prefix(pref):
        for word in words:
            try:
                if word.index(pref)==0:
                    return True
            except:
                pass
        return False


    for M1 in range(97,123):
        for m1 in valid_range:
            if M1^m1==23:
                for m2 in valid_range:
                    if m2==32: 
                        if m1 in [97,105]:
                            print(m1,M1,m2)
                    else:
                        if prefix(word(convert([m1,m2]))) and prefix(word(convert([M1,m2]))):
                            print(m1,M1,m2)
    #                         pass
    #                         for m3 in valid_range:
    #                             for m4 in valid_range:
    #                                 for M4 in valid_range:
    #                                     if m4^M4==31:
    #                                         print(m1,M1,m2,m3,m4,M4)



