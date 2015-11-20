# -*- coding: UTF-8 -*-

import urllib
import httplib2
import re

asci_list = {32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: "\\", 93: ']', 94: '^', 95: '_', 96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~', 129: 'ü', 130: 'é', 131: 'â', 132: 'ä', 133: 'à', 136: 'ê', 137: 'ë', 138: 'è', 139: 'ï', 140: 'î', 141: 'ì', 142: 'Ä', 144: 'É', 147: 'ô', 148: 'ö', 149: 'ò', 150: 'û', 151: 'ù', 152: 'ÿ', 153: 'Ö', 154: 'Ü', 160: 'á', 161: 'í', 162: 'ó', 163: 'ú', 164: 'ñ', 165: 'Ñ'}

def isprime(n):
    if n == 2:
        return True
    if n < 2 or not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if not n % x:
            return False
    return True

def perform_operation(nlist):
    inc = 0
    prmval = 0
    numval = 0
    for x in nlist:
        x = int(x)
        if isprime(x):
            prmval += x
        elif x > 2:
            numval += x
        inc += 1
    return (prmval * numval)

if __name__ == '__main__':
	url = 'https://www.hackthissite.org/user/login'
	login_data = {
		'username': 'KwawK',
		'password': 'KI%5Frl@@IJW5VS'
	}
	headers = {
		'Content-type': 'application/x-www-form-urlencoded',
		'Referer': 'https://www.hackthissite.org/'
	}

	http = httplib2.Http()
	response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(login_data))

	headers['Cookie'] = response['set-cookie']
	url = 'https://www.hackthissite.org/missions/prog/12/'

	response, content = http.request(url, 'GET', headers=headers)

	string = re.findall("value=\"(.*)\"", content)
	numbers =  re.findall("[2-9]", string[0])
	string = re.findall("[^0-9]", string[0])
	new_string = string[:25]
	answer_backside = perform_operation(numbers)

	text = ""
	for chars in new_string:
		for key in asci_list.keys():
			if asci_list[key] == chars:
				text += str(asci_list[key+1])

	text += str(answer_backside)

	url = 'https://www.hackthissite.org/missions/prog/12/index.php'

	data = {'solution': text, 'submitbutton': 'Submit'}
	response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(data))

	print content
	print response