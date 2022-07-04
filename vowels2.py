vowels = ['a', 'e', 'i', 'o', 'u']
world = "Milliways"
found = []
for litter in world:
    if litter in vowels:
        if litter not in found:
            found.append(litter)
for vowels in found:
    print(vowels)