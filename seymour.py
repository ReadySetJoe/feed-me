## Also, I'm gonna make a lil secret game in here for fun! Shhhh don't tell anyone ;)

def joes_secret_game():
  import sys,time,random

  typing_speed = 100 #wpm
  def printc(t):
      for l in t:
          sys.stdout.write(l)
          sys.stdout.flush()
          time.sleep(random.random()*10.0/typing_speed)
      print()

  hero = {}
  printc("Hello! What's your name?")
  hero['name'] = input()
  printc("Nice to meet you, "+hero['name']+"! I'm your computer! I know we've hung out a lot, but I feel like we've never really gotten to talking. ")
  lets_do_it = False
  please = 0
  while not lets_do_it:
    printc("Would you be willing to help me out with something? [y/n]")
    lets_do_it = input() == 'y'
    printc("Pleeeeease?"*(please>0) + " please"*please + "?"*please>(0))




