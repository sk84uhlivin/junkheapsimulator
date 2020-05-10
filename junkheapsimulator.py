import random

amber = [0, 1, 2, 3, 4]
flourite = [5, 6, 7]
damascus = [8]
a = 0
f = 0
d = 0
x = 0

while x < 40:
    roll = random.randint(0, 99)
    if roll in amber:
        a += 1
    elif roll in flourite:
        f += 1
    elif roll in damascus:
        d += 1
    x += 1

amber_v = 3000
flourite_v = 6000
damascus_v = 6400

amber_g = a * amber_v
flourite_g = f * flourite_v
damascus_g = d * damascus_v
g = amber_g + flourite_g + damascus_g

print()
print(f"Amber: {a} x {amber_v}")
print(f"Flourite: {f} x {flourite_v}")
print(f"Damascus Steel: {d} x {damascus_v}")
print()
print(f"You got {g}G!")

