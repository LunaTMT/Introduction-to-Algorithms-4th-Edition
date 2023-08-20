import random

def addBinaryIntegers(A, B, answer):

    if len(A) > len(B):
        B = B.zfill(len(A))
    else:
        A = A.zfill(len(B))
    
    carry = 0
    res = ""
    for a, b in zip(A[::-1], B[::-1]):
        a = int(a)
        b = int(b)

        if (a, b, carry) == (1, 1, 1):
            res += "1"
        elif (a, b, carry) in ((1,0,1), (0,1,1), (1,1,0)):
            carry = 1
            res += "0"
        elif (a, b, carry) in ((1,0,0), (0,1,0), (0,0,1)):
            carry = 0
            res += "1"
        else:
            res += "0"
    
    if carry == 1:
        res += "1"

    print(True if res[::-1] == answer else False)
 
for i in range(10):
    A = random.randint(1, 999999999999999999999)
    B = random.randint(1, 999999999999999999999)
    answer = A+B
    addBinaryIntegers(bin(A)[2:], bin(B)[2:], bin(answer)[2:])

