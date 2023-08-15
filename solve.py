lst = []
n = int(input("Size: "))

for i in range(1, n+1):
    ele = i
    # adding the element
    lst.append(ele) 
 
index = 0
loop = 0



while len(lst) != 1:
    if loop % 2 == 0:
        try:
            lst.pop(index)
            index += 1
        except:
            index = len(lst) + 1
        if index > len(lst):
            if len(lst) % 2 != 0:
                index = 0
                loop+=1
            else:
                index = 1
                loop += 1
        
    else:
        try:
            lst.pop(index)
            index += 1
        except:
            index = len(lst) + 1
        if index > len(lst):
            index = 0
            loop += 1
print(lst)