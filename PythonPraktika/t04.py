# Verilən ədədin rəqəmlərini tərsinə çevirən funksiya yazın.

def reverseNumberDigits(a):
n=int(input("ededi daxil edin: "))
sum=0
def findSumOfDigits(a):
    global n
    global sum
    while n>0:
        r=n%10
        n=n//10
        print(r)

    
reverseNumberDigits(123) # 321 #eyni setirde nece edirdik unutdum
