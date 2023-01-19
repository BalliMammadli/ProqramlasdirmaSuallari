# Bir a ədədi verilir.Sizdən tələb olunan bu ədədin rəqəmlərinin cəmini tapmadır

def findSumOfDigits(a):
n=int(input("ededi daxil edin: "))
sum=0
def findSumOfDigits(a):
    global n
    global sum
    while n>0:
        r=n%10
        n=n//10
        sum=sum+r
    return sum

    
findSumOfDigits(123) # 6
