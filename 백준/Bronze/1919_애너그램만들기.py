word1 = list(input())
word2 = list(input())
new_word1 = word1.copy()

for item in word1:
	if item in word2:
		new_word1.remove(item)
		word2.remove(item)
	else:
		continue

print(len(new_word1)+len(word2))
