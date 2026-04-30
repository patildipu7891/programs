#dublicate in list
n = [4,5,4,5,6,5,4,2,8,9,5,6,7,4,3,2,3,1,0,1]

seen = set()
duplicates = set()

for i in n:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print(duplicates)