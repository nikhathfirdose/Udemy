from random import randint

answer = randint(1,10)
while True:
  print(answer)
  try:
    guess = int(input("number"))
    if guess>0 and guess<11:
      if guess== answer:
        print("yayy")
        break
    else:
      print("nooo")
  except ValueError:
    print("enter a numer yu bozo")