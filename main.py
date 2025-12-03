#7-misol

a = float(input("1-son: "))
b = float(input("2-son: "))
c = float(input("3-son: "))

print("Eng katta son:", max(a, b, c))

# 8-misol

y = int(input("Yilni kiriting: "))

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    print("Kabisat yili")
else:
    print("Oddiy yil")

# 9-misol

a = float(input("1-son: "))
b = float(input("2-son: "))
c = float(input("3-son: "))

print("Eng kichik son:", min(a, b, c))

# 10-misol
n = int(input("Raqam kiriting: "))

if n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    print("Boshqa raqam")

# 11-misol

a = float(input("1-tomon: "))
b = float(input("2-tomon: "))
c = float(input("3-tomon: "))
d = float(input("4-tomon: "))

if a == b == c == d:
    print("Kvadrat")
else:
    print("To'rtburchak")

# 12-misol
n = float(input("Son kiriting: "))

if n <= 100:
    print("Kichik yoki teng 100")
else:
    print("Katta")
