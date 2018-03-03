import random
import turtle
turtle.goto(0,7)
class Riddle(object):
	def __init__(self,riddle_Text,answer1,answer2,answer3,correct_answer):
		self.riddle_Text=riddle_Text
		self.answer1=answer1
		self.answer2=answer2
		self.answer3=answer3
		self.correct_answer=correct_answer

easy=[]
medium=[]
hard=[]
#make_easy_riddles
five_e=Riddle("If you are running in a race and pass the second place person, what place are you in?","a)third place","b)second place","c)first place","b)second place")
second_e=Riddle("which part of the body closes when we sneeze?","a)ears","b)nose","c)eyes","c)eyes")
third_e=Riddle("l=i c=z r=a n=p which code means pizza? :p","a)frlc","b)nlccn","c)nlccr","c)nlccr")
easy.append(five_e)
easy.append(second_e)
easy.append(third_e)
##
##
sixth_m=Riddle("Tamer is 6 years old Inon is tow times younger than Tamer. a few years pass..now Tamer is 70 years old.how old is Inon?","a)35","b)73","c)67","c)67")
four_m=Riddle("there are 10 fishes in the aqurium, 7 died how many fishes are in the aquarium now? ","a)10","b)3","c)54","a)10")
first_m=Riddle("find the code! meet-meetmeetmeetmeetmeet-meetmeetmeet-meetmeet","a)1431","b)1532","c)banana","b)1532")
medium.append(sixth_m)
medium.append(four_m)
medium.append(first_m)
##
##
#nn_h=riddle("you're trapped in an old building,there is no food no water no electricity no people around no  only three doors,")
nn_h=Riddle("a BMW car was going to a famous city, in the way it MEETs three cars. how many cars are going to that famous city?","a)1","b)3","c)4","a")
seventh_h=Riddle("when did meet start?","a)1989","b)2004","c)2003","b")
e_h=Riddle("why does Nizar own a lot of ducks?","a)it's a gift from his girlfriend","b)because a duck saved him when he was a littel kid","c)because it's cheep and good for debuging","c")
hard.append(seventh_h)
hard.append(e_h)
hard.append(nn_h)
f=Riddle("gtfb","bgg","gg","gfg","fuj")
def congrats():
	print("congratiulations!!")
def choosehard():
	x=random.randint(1,random.randint(2,3))
	if(x==1):
		f=seventh_h
		turtle.write(seventh_h.riddle_Text)
		turtle.write(seventh_h.answer1)
		turtle.write(seventh_h.answer2)
		turtle.write(seventh_h.answer3)
		#turtle.onkeypress(congrats, "b")
	if(x==2):
		f=e_h
		print(e_h.riddle_Text)
		print(e_h.answer1)
		print(e_h.answer2)
		print(e_h.answer3)
	if(x==3):
		f=nn_h
		print(nn_h.riddle_Text)
		print(nn_h.answer1)
		print(nn_h.answer2)
		print(nn_h.answer3)
choosehard()

	#money = money + based on difficulty
h=f.correct_answer
turtle.onkeypress(congrats(), h)
turtle.listen()
turtle.mainloop()

