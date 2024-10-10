# 1, 5, 13, 29, 49, 77 .... N
n = int(input("Enter n :"))
a = 4
b=1
print(b)
for i in range(1,n):
    if a%3==0:
        a+=4
        continue
    b+=a
    a+=4
    print(b)
    