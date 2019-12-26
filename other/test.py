import lyricwikia
import re
from PyDictionary import PyDictionary
import enchant

dictionary=PyDictionary()

# name = "Barack (of Washington)"
# name = re.sub('[\(\)\{\}<>]', '', name)
# print(name)

artist = "Lil pump"
song = "Gucci gang"

def run():
	lyrics = lyricwikia.get_lyrics(artist, song)
	d = enchant.Dict("en_US")
	word_list = []
	for x in lyrics.split():
		word = x
		word = re.sub("""[\(\)\{\}<>?,":.!'-]""", '', word)
		if word.lower() not in word_list:
			try:
				check_if_word = d.check(word.lower())
			except Exception as e:
				pass
			if check_if_word:
				word_list.append(word.lower())
			else:
				pass
		else:
			pass
	i = 0
	for x in word_list:
		try:
			print x
		except:
			pass
		i += 1

	print "\n" + artist + ", " + song
	print str(i) + " ord!"

run()
# d = enchant.Dict("en_US")
# print d.check("hello")
#(dictionary.meaning(word.lower()))