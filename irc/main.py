# -*- coding: UTF-8 -*-

import socket
import hashlib

server = "irc.hackthissite.org"
channel = "#perm8"
botnick = "KwawK"

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))

ircsock.recv (4096)
ircsock.send('NICK ' + botnick + '\r\n')
ircsock.send('USER ' + botnick + ' ' + botnick + ' ' + botnick + ' :Python IRC Bot\r\n')
# 
try:
	while True:
		data = ircsock.recv (4096)
		print data
		if data.find('PING') != -1:
			ircsock.send('PONG ' + data.split()[1] + '\r\n')
		if data.find('MODE ' + botnick + ' :+ix') != -1:
			ircsock.send('PRIVMSG NickServ identify KwawK Iecanv78\r\n')
			ircsock.send('NS set autoop on\r\n')
			ircsock.send('JOIN ' + channel + '\r\n')
			ircsock.send('NOTICE moo !perm8\r\n')
		if data.find('!md5') != -1:
			print str(data[40:56])
			answer = hashlib.md5(str(data[40:56])).hexdigest()
			print answer
			ircsock.send('NOTICE moo !perm8-result ' + answer + '\r\n')
		if data.find('VERSION') != -1:
			ircsock.send('NOTICE moo \001VERSION FireDogFuckas:1.0:Hobos\001\r\n')
		if data.find('!perm8-attack') != -1:
			ircsock.send('JOIN #takeoverz\r\n')
			ircsock.send('KICK #takeoverz moo\r\n')
except KeyboardInterrupt:
	ircsock.send('DISCONNECT')
	print "Bye Bye"