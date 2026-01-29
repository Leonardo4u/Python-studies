import random

def get_lucky_number():
  lucky_num = random.randint(1,100)
  return lucky_num

# Get a lucky number between 1 and 100
lucky_number = get_lucky_number()

print("Your lucky number is:", lucky_number)