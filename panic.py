phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(5):
    plist.pop()
plist.remove("'")
plist.remove(" ")
plist.pop(0)
plist.insert(2, " ")
plist.insert(4, "a")


new_phrasw = ''.join(plist)
print(plist)
print(new_phrasw)