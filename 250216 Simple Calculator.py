a = float(input("Enter 1st number: "))
c = float(input("Enter 2nd number: "))
b = input("Enter symbol: ")

h = "+"
i = "-"
j = "*"
k = "/"

if b == h:
   print(f"{a}{b}{c}={a+c}")
elif b == i:
   print(f"{a}{b}{c}={a-c}")
elif b == j:
   print(f"{a}{b}{c}={a*c}")
elif b == k:
   print(f"{a}{b}{c}={a/c}")
 

# 10*5=50