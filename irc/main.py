# -*- coding: UTF-8 -*-

import socket
import re

server = "irc.quakenet.org"
channel = "#testKwawK"
botnick = "KwawKBot"

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))

ircsock.recv (4096)
ircsock.send('NICK KwawKPyBot\r\n')
ircsock.send('USER ' + botnick + ' ' + botnick + ' ' + botnick + ' :Affix IRC\r\n')

while True:
	data = ircsock.recv (4096)
	print data
	if data.find('PING') != -1:
		ircsock.send('PONG ' + data.split()[1] + '\r\n')
	if data.find('MODE') != -1:
		ircsock.send('JOIN ' + channel + '\r\n')