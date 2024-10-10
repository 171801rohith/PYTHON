# 4, 16, 36, 64, ....N 
n = int(input("Enter n :"))
for i in range(2,n):
    if i%2==0:
        print(i*i)
    else:
        continue     
