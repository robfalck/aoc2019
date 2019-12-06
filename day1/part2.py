depth = 0

def calc_fuel_mass(mass, recurse=False):
    global depth
    fuel_mass = int(mass / 3) - 2
    depth += 1
    if recurse:
        if fuel_mass <= 0:
            return 0
        else:
            return fuel_mass + calc_fuel_mass(fuel_mass, recurse=True)
    else:
        return fuel_mass


with open('input.txt', 'r') as wdf:
    masses = [int(line) for line in wdf.readlines()]

fuel_reqs = []

for m in masses:
    fr = calc_fuel_mass(m, recurse=True)
    print(depth)
    exit(0)
    fuel_reqs.append(fr)

# print(masses)
#
# print()
#
# print(fuel_reqs)

print(sum(fuel_reqs))

