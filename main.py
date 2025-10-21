# A program to calculate the amount of data that n bits can store.

Nbits = int(input("Bits: "))

Power = 0

ans = 0
while Power <= Nbits:
  ans += 2**Power
  Power += 1

print(f"The amount of data stored in {Nbits} is {ans}")
