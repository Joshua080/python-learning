def main():
    word = input("Input: ")

    print(shorten(word))

def shorten(word):
    ans = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            ans += char
    return ans


if __name__ == "__main__":
    main()
