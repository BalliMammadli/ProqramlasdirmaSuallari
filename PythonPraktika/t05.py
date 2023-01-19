# Verilən massivdəki ən böyük ədədi tapın.

def findMax(lst):
    def findMax(lst):
   i=0
   for i in lst:
    
    if lst[i]>lst[i+1]:
        return lst[i]
    else:
        return lst[i+1]
        
  

    
print(findMax([1, 2, 3])) # 3
