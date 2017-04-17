import Maps

mapobj = Maps.Map21x21()
gameover = False
while gameover == False:
	print('Actions: find, viewmap, exit')
	action = input('What would you like to do?: ')
	if(action == 'find'):
		 print('Object Found at: ' + str(mapobj.findValue(input('What value would you like to find? '), input('How many times would you like to skip until you find your value? '))))
	elif(action == 'viewmap'):
		mapobj.printMap(1)
	elif(action == 'exit'):
		gameover = True
	else:
		print('That is not an action!')
input('Press [ENTER] to exit...')