
height=int(input('what is your height (cm)?'))
credits=int(input('how many credits do you have?'))
if height >= 137 and credits >= 10:
  print("enjoy the ride!")
elif height < 137 and credits >= 10:
  print("you are not tall enough to rde.")
elif height >= 137 and credits < 10:
  print("you dont have enough credits.")
else:
  print("they have not met either requirments.")      
