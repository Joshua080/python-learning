str = input("Input: ")
ans = ""
for char  in str:
    if char.lower() not in ["a", "e", "i", "o", "u"]:
        ans += char
print(ans)
