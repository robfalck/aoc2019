

with open('input.txt', 'r') as wdf:
    masses = [int(line) for line in wdf.readlines()]

fuel_reqs = []

for m in masses:
    fr = int(m / 3) - 2
    fuel_reqs.append(fr)

# print(masses)
#
# print()
#
# print(fuel_reqs)

print(sum(fuel_reqs))