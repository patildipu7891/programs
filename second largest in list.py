#second largest in list
n = [6,78,3,7,744,646,567,35,8356,35,7577,56763,235,35]

largest = n[0]
second_largest = n[0]

for i in n:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print( second_largest)