# -*- coding: UTF-8 -*-

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
			counter = 0
			for char in line:
				if char in words[i]:
					counter += 1
			if counter == len(words[i]) and len(line) == len(words[i]):
				lines.append(words[i])
				# counter = 0
				break

text = ','.join(lines)

print text