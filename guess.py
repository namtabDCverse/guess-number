import random

number = random.randint(1,100)
i = 10
while i > 0:
	i = i - 1
	number_player = input('請猜數字:')
	number_player = int(number_player)
	if number_player == number:
		print("正確")
		break
	else:
		if i > 0:
			if number > number_player:
				print('比答案小，還有',i,'次機會')
			elif number < number_player:
				print('比答案大, 還有',i,'次機會')
		elif i == 0:
			print('答案是:', number)
