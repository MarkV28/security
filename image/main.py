# -*- coding: UTF-8 -*-

from PIL import Image

image = Image.open('PNG.png', 'r')

morsecode_list = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', "t": "-", 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '-': '-....-', '/': '-..-.', ':': '---...', "'": '.----.', ')': '-.--.-', ';': '-.-.-', '(': '-.--.', '=': '-...-', '@': '.--.-.', '&': '.-...', 'à': '.--.-', 'é': '..-..', 'è': '.-..-', 'ñ': '--.--', 'ö': '---.', 'ü': '..--', 'ä': '.-.-', '"': '.-..-.'}

asci_list = {32: ' ', 45: "-", 46: "."}

pngdata = list(image.getdata())

lines = []
text = ""
solution = ''
offset = 0
prev_index = 0

for index, value in enumerate(pngdata):
	if value == 1:
		offset = index - prev_index
		prev_index = index
		# print index
		text += asci_list[offset]
		if offset == 32:
			for key in morsecode_list.keys():
				text = text.rstrip()
				# print key
				if morsecode_list[key] == text:
					lines.append(key)
					text = ""
			

solution = ''.join(lines)

print solution
