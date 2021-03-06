import time
import random
"""
1. Útskýrðu stuttlega tímaflækjurnar hér fyrir neðan.  Nefndu dæmi um reiknirit sem hafa eftirfarandi tímaflækjur.
    a. big O er notað í Classify algorithms samkvæmt hvernig keyrslu tímin er og geymslu kröfur stækar eins og input stærð stækar
    b. Margfalda 2 n-digit númer af einföldu algorithma; svona algortihma eins og bubble sort, selection sort og insertion sort; mörk á eitthverju á sumum venjulegri sorting algorithms eins og quicksort, Shellsort og tree sort
    c. keyrslu tímin stækar í hlutfalli við n

"""

#2

# recursiv -----
# def bubble_sort(listt): 
#     for i, num in enumerate(listt): 
#         try: 
#             if listt[i+1] < num: 
#                 listt[i] = listt[i+1] 
#                 listt[i+1] = num 
#                 bubble_sort(listt) 
#         except IndexError: 
#             return 0
#     return listt 
#   # 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 20 21 22 23 25 26 27 28 29 30
# listt = [10, 5, 2, 4, 1, 3, 6, 9, 8 , 7, 20, 12, 14, 15, 13, 16, 18, 19, 17, 30, 25, 21, 23, 26, 22, 27, 29, 28, 24] 
# bubble_sort(listt) 
  
# print("Sorted array:"); 
# for i in range(0, len(listt)): 
#     print(listt[i], end=' ') 
# --------------------

#endur taka til að læra betur

startTime = time.time()

def bubble_sorta(arr):
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

b = 0
arr = []
m = 1
while(b < 10000):
    arr.append(m)
    random.shuffle(arr)
    m += 1
    b += 1


print(arr,'\n')
bubble_sorta(arr)

print("Sorted array: ")
for e in range(0, len(arr)):
    print('\n',arr[e], end=' ')

print('\n',time.time() - startTime)


startTime2 = time.time()

list4 = [10, 5, 2, 4, 1, 3, 6, 9, 8 , 7, 20, 12, 14, 15, 13, 16, 18, 19, 17, 30, 25, 21, 23, 26, 22, 27, 29, 28, 24] 
print(list4.sort())

print('\n',time.time() - startTime2)



# fallið tekur inn lista en ekki streng og skilar lista en ekki streng
def stafróf(ss):
    for e, tal in enumerate(ss):
        try:
            if ss[e+1] < tal:
                ss[e] = ss[e+1]
                ss[e+1] = tal
                stafróf(ss)
 
        except IndexError:
            pass
 
    return ss
 
inp3 = input("# 3 Slá inn orð ")
texti = stafróf(list(inp3)) # breytum streng í lista fyrir fallið...
 
print(''.join(texti)) # breytum lista í streng fyrir output...

#     if s == "":
#         print()
#     else:
#         print(s[0])
#         stafróf(s[1:])

# inp8 = str(input("#8 Slá inn orð "))
# stafróf(inp8)





# 4
print('\n', '# 4')
def fall(L):
    haesta = max(L)
    countL =[0]*(haesta+1)
    result =[0]*len(L)

    for i in L: # á meðan i inn í L 
        countL[i] += 1 # fyrst er addað vinstra valueið í hægra og svo add svarinu í vinstra valueið
    
    summa = 0
    for i in range(len(countL)):  # i inn í range með leingdina af countL
        summa += countL[i]  # fyrst er addað vinstra valueið í hægra og svo add svarinu í vinstra valueið
        countL[L[i]] -= 1  # fyrst er mínusað vinstra valueið í hægra og svo add svarinu í vinstra valueið

    return result

# Keyrsluforrit...
L = [7,1,8,2,5,10,8,9,3,6,1]
print(fall(L))

# Svo flækju stigið er O(1) + O(1) + O(1) + O(n) + O(n) sem þíðir að svarið er big O(n)

#5
def insertFall(listi, n):
    for i in range(len(listi)):
        if listi[i] > n:
            index = i
            break
    
    listi = listi[:i] + [n] + listi[i:]
    return listi

listi = [2,3,5,6,7,9,10]

inp5 = int(input("#5 Slá inn tölu "))
print(insertFall(listi,inp5))