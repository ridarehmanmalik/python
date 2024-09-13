import random
question=input('question:')
num=random.randint(1,9)
if num == 1:
  print('yes definitely.')
elif num == 2:
  print('it is decidedly so.')
elif num == 3:
  print('without a doubt.')
elif num == 4: 
  print('reply hazy,try again.')
elif num == 5:
  print('ask again later.')   
elif num == 6:
  print('better not tell you know.')
elif num == 7:
  print('my sources say no.')
elif num == 8:
  print('outlook not so good.')
elif num == 9:
  print('very doubtful.')
else:
  print('error')

  print('magic 8 ball:'+answer)