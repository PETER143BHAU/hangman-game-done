print('                      WELCOME TO HANGMAN')
w=1
fg=1
d=[]
gh=[]
i=input('               DO YOU WANT TO PLAY THIS GAME  Y/N   ')
if i=='y' or i=='Y':
	print('                      OK LETS PLAY')
	import random
	l=['time','role','name','you','please','problem','hangman','laptop','nothing']
	s=(random.choice(l))
	print('SO GUESS ONE WORD')
	f=('-'*len(s))
	for i in s:
		d.append(i)
	for j in f:
		gh.append(j)	
	while 1:
		print('enter any letter')
		print(''.join(gh))
		u=input()
		if u in d:
			for k in range(len(s)):
				if u==d[k]:
					gh[k]=u
					print(''.join(gh))
		if len(u)>1:
			print('invalid input')
		elif u not in d:
			print('wrong GUESS')
			print('you have',len(s)-fg,'chances')
			fg+=1		
			import hangman
			print(hangman.IMAGES[w])
			w+=1
			if (hangman.IMAGES[w])==(hangman.IMAGES[8]):
				print('you loose')		
				break
		if s==''.join(gh):
			print('                      NICE PLAYER')
			import photo
			print(photo)
			break

else:
	print('  OK THAN DONT PLAY')




		

# s=[q,w,e,r,t]
# s[2]='m'
# print(s )


	

# a=['n','v','g','u','r','u','k','u','l']
# b=['-','-','-','-','-','-','-','-','-','-']
# for i in range(len(a)):
# 	if 'g'==a[i]:
# 		b[i]='g'
# print(' '.join(b))
