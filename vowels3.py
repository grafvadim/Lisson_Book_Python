vowels = ['a', 'e', 'i', 'o', 'u']
world = input("Provide a world to search for vowels: ")
found = []
for litter in world:
    if litter in vowels:
        if litter not in found:
            found.append(litter)
for vowels in found:
    print(vowels)