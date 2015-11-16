# -*- coding: UTF-8 -*-

from collections import Counter

f = open('wordlist.txt', 'r')
words = f.read().split('\n')
lines = []
text = ''

while True:
	line = raw_input()
	if 'quit' in line:
		break
	elif line:
		for i in range(0, len(words)):
			if len(words[i]) == len(line):
				if not list(set(list(words[i])) - set(list(line))):
					if len(Counter(words[i])) == len(Counter(line)):
						lines.append(words[i])
						break

text = ','.join(lines)

print text