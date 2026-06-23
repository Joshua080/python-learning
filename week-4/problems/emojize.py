import emoji
import cowsay

text_emoji = input("Input: ")
print(cowsay.cow(f"I love you {emoji.emojize(text_emoji)}"))