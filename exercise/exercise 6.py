wrd=input("enter a word: ")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("word is palindrome")
else:
    print("word isnt palindrome")