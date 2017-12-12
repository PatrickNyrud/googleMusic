import wikipedia
import os

os.system("cls")

wikipedia.set_lang("en")

sumry = wikipedia.random(pages = 1)

check = wikipedia.page(sumry)

asd = check.content
ge = asd.encode("utf-8", "ignore")

print sumry
raw_input()
print ge

with open("wiki.txt", "w") as f:
	f.write(ge)