world = "hello, world"
lworld = list(world)

print(world)
print(lworld)



for i in range(3):
    lworld.pop(0)
lworld.remove('w')
lworld.remove('d')
lworld.pop(4)
lworld.insert(5, 'o')

new_world = ''.join(lworld)

print(new_world)
print(lworld)

