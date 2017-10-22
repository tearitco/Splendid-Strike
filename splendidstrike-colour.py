#!/usr/bin/python

import os
import time
import random
from random import randint

#################### VARIABLES ##############
_ICBM_ratio = 0
number_of_ABMs = 44			# Yes, this is really the number of ABMs the USA has.
number_of_ICBMs = random.randint(1,20)	# Let's generate between 1 and 20 enemy warheads
ICBMs_in_entire_war = number_of_ICBMs
hits = 0
misses = 0
enemy_salvoes = 1
begin = ""
nukeouts = 0
current_target = ""
russian_roulette = random.randint(0,100)

###################### SUBROUTINES #####################################
def other_side_effects(nukeouts,ICBMs_in_entire_war):

#	print "nukeouts:", nukeouts
#	print "ICBMS in war:", ICBMs_in_entire_war

	shot_down_ICBMs = (ICBMs_in_entire_war - nukeouts)	
	chance_of_kessler = random.randint(0,shot_down_ICBMs)

#	print "shot down ICBMs:",shot_down_ICBMs
#	print "chance of Kessler:",chance_of_kessler
	if (chance_of_kessler > 6):
		print "\n You have shot down so many ICBMs that they have collided with"
		print "other objects in space to cause the dreaded ABLATION CASCADE"
		print "(AKA Kessler Syndrome), essentially the debris from your little"
		print "war has crashed into orbiting satellites, blowing them to bits."
		print "The bits have in turn smashed into other satellites, a result of "
		print "which is, we can no longer use our satellites or launch new ones."
		print "\n In fact, space will be inaccessible for many decades, perhaps ";
		print "even centuries, to come."

	if (shot_down_ICBMs > 0):
		print "\n Also, the plutonium and uranium from the",shot_down_ICBMs,"ICBMs"
		print "you shot down is raining down on Earth, causing "
		print "environmentalists to become upset and slowly giving "
		print "everyone cancer. \n"

	
		
def PressEnter():
	try:
		cont = int(input("\n Press ENTER to continue..."))
	except:	
		print "",


def NuclearExplosion():
	print "AAAAAAAAARRRRRRRRRRRRGGGGGGGGGGGGGGGGHHHHHHHHHHHH!!!!"
	print ('\033[0;37;47m'+'                                  ')
	print ('\033[2;29;47m'+'                ********')
#	print "              ",
	#print ('\033[0;31;41m'+'         '+'\033[0m')
#	print ('\033[2;31;47m'+'         ***********************')
	print ('\033[2;31;47m'+'                   ')
	print "             **************"
	print "          ********************"
#	print ('       **************'+'\033[2;3;47m'+'************')
	print ('       **************'+'\033[1;31;47m'+'************')
	print "      ***************************"
	print "       **************************"
	print "         ************",
	print ('\033[2;31;47m'+'**********\n         *********************')
	print "          *******************"
	print "                 *****"
	print "                ***** "
	print "           ***   *****   *****"
	print "       ****     *****        ***"		
	print "      *          *****          ** "	
	print "     ***         ****         ***"
	print "        ******  ******   ****** "
	print "              ** ***** **"
	print "                 ****  "
	print "                 ****  "
	print "                 ****  "
	print "                ******  "
	print "     *****************************"		
	print ('    *******************************\n\n '+'\033[0m')
	print "      KABOOOOOOOOOOOOOOOOOOOOOOM!"
	time.sleep(1)
	



def check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts):
	if (number_of_ABMs < 0 and number_of_ICBMs >0):

		print ('\033[0;30;41m'+'\t   YOU HAVE RUN OUT OF ABMS!            '+'\033[0m')
		print ('\033[1;33;41m'+'\t Unfortunately, the enemy has not...    '+'\033[0m')

#		print ('\033[7;30;91m'+'\t   YOU HAVE RUN OUT OF ABMS!'+'\033[0m')
#		print ('\033[7;30;91m'+'\t Unfortunately, the enemy has not...'+'\033[0m')
		nukeouts += number_of_ICBMs
		loop = nukeouts
		pauser (40000)
		NuclearExplosion()
#		print "    KABOOOOOOOOOOOOOOOOOOOOOOM!\n\n ";
		print "   ",nukeouts,
		print "American cities have been destroyed!",
		print ('\033[3;33;40m'+' ')
		print " MILLIONS of people are dead, many of whom voted for YOU!"
#		print "DEBUG: Before call: Nukeouts;",nukeouts,"ICBMs in war:",ICBMs_in_entire_war
		other_side_effects(nukeouts,ICBMs_in_entire_war)
		print (' Oh, woe, woe, woe is you! It\'s just so UNFAIR and FAKE!'+'\033[0m')
		print "\n";
		if (nukeouts > 30):
			print ('\033[3;33;40m'+' ')
			print "It gets worse. Nuclear winter turns the planet into a radioactive iceball"
			print "and as a reult, Mar-A-Lago and your other fine resorts are completely "
			print "snowed under. Your guests are very cross and demand their money back."
			print "YOU ARE FINANCIALLY RUINED, and because everyone else is dead, there is "
			print "nobody left alive to bail you out."
			print "\n You spend the rest of your life eating baked beans and Spam in a "
			print "very classy nuclear bunker, which very soon smells unbearable. Outside, "
			print "MEXICANS have taken over, cleared all the dead bodies away, and turned"
			print "the USA into a massive ski resort."
			print ('\033[0m')

		print "\n \t GAME OVER \n";
		quit();


def pauser(loops):
	loops *= 1000
	while (loops > 0):
		loops -=1
	return




############################### main_loop ########################################

def main_loop(number_of_ICBMs, enemy_salvoes, number_of_ABMs, nukeouts, misses, hits,ICBMs_in_entire_war):
	pauser (100)
	enemy_salvo = random.randint(1,number_of_ICBMs)
	print ('\033[91m'+'\n \t ')
	print "\t *** There are ",enemy_salvo, "ICBMs incoming! ***"
	print (' '+'\033[0m'),
	print "    This is the ",enemy_salvoes,
	if (enemy_salvoes == 1):
		print "st",
	elif (enemy_salvoes == 2):
		print "nd",
	elif (enemy_salvoes == 3):
		print "rd",
	else:
		print "th",
	print "salvo."
	check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)	

	print "\n   You have ",number_of_ABMs,
	print "ABMs left."
	number_of_ICBMs -= enemy_salvo

	if (number_of_ICBMs > 0):
		print "\n   Intelligence indicates that They will still have another",number_of_ICBMs
		print "   ICBM(s) left in reserve after this attack."
	try:
		ABM_ICBM_ratio = int(input("\n How many ABMs to each ICBM?  >"))
	except:
		print " Numerals ONLY, please! (sorry Trump, I know you don't like Arabic things, but" 
		print "we really, REALLY need Arabic numerals!)"
		ABM_ICBM_ratio = int(input("\n How many ABMs to each ICBM?  >"))

	number_of_ICBMs += enemy_salvo   	# Bit of a bodge this

	ABMs_spent = (ABM_ICBM_ratio * enemy_salvo)
#	number_of_ABMs -= ABMs_spent

	enemy_round = enemy_salvo;



	print "\n\n"

	print "*****************************"
	print "*ENEMY MISSILE SALVO BEGINS!*"
	print "*****************************"

	time.sleep(1)
	while (enemy_salvo > 0):
		time.sleep(1)
		current_target = ""
		print "\n\n"
		print ('\033[7;30;91m'+'                                         ')
		print "     Missiles left to shoot down:",enemy_salvo,"   ",
		if (enemy_salvo)<10:
			print " "
		else:
			print ""
		print ('                                         '+'\033[0m')
		ABM_salvo = ABM_ICBM_ratio
		print ('\033[0;30;42m'+'  Firing ABMS... fingers crossed! '+'\033[0m')	# green
		print ('\033[0;30;42m'+'ABMs:'),
		print number_of_ABMs,'  ICBMs:',number_of_ICBMs,'  nukeouts:',nukeouts,
		print ('\033[0m')
#		print ('ABMs:',number_of_ABMs,'  ICBMs:',number_of_ICBMs,'  nukeouts:',nukeouts+'\033[0m')
#		print ('ABMs:',number_of_ABMs,'  ICBMs:',number_of_ICBMs,'  nukeouts:',nukeouts+'\033[0m')
		check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)	

		while (ABM_salvo >0):
			time.sleep(1)
			ABM_salvo -= 1
			number_of_ABMs -= 1
			if (current_target != "HIT"):
				check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)
			elif (number_of_ABMs < 0 and current_target == "HIT"): # Obscure bug, gaffa taping it
				print ('\033[7;30;91m'+'\t YOU HAVE RUN OUT OF ABMS AND CANNOT FIRE!'+'\033[0m')
				pauser(200)
				break
			your_ABM = random.randint(0,100)	 
			if (your_ABM in range (0,56)):
				print ('\033[44m'),
				if (current_target == "HIT"):
					pauser (200)
					print "\t* ANOTHER HIT! * Well done! You hit the same missile more than once!",
				else:
					pauser (500)
					print "\t \t ******   A HIT!  ******\t\t\t\t    ",

				print ('\033[0m')	# back to normal
				hits += 1
				abm_salvo = 0
				current_target = "HIT"
			else:
				print ('\033[0;30;47m'),	# white
				if (current_target == "HIT"):
					pauser (200)
					print "\t Your missile screams past the cloud of debris!!",
				else:
					pauser (500)
					print "\t ***** AAAARGH YOU MISSED! ABMS LEFT IN SALVO:",ABM_salvo,
				print ('\033[0m')	# back to normal
				misses += 1

		if (number_of_ABMs < 0):	# Obscure bug, 2nd part of fix
			number_of_ABMs = 0	# 
		number_of_ICBMs -= 1
		enemy_salvo -= 1
		if (current_target != "HIT"):
			time.sleep(1)
			NuclearExplosion()
			nukeouts += 1

	time.sleep(1)
	enemy_salvoes +=1
	ABMs_ever = hits+misses
#	hits_this_round = hits
#	misses_this_round = misses
	print "\n\n"
	print ('\033[0;30;47m'),	# white
	print "\n ****************************************"
	print " *         POST BATTLE REPORT:          *"
	print " * Total number of enemy missiles:",ICBMs_in_entire_war,"\t*"
	print " * Enemy missiles fired this round:",enemy_round,"\t*"
	print " * Enemy missiles left:",number_of_ICBMs,"\t\t*"
	print " * ABMS left:",number_of_ABMs,"\t\t\t*"
	print " * Total ABMs fired (ever):",ABMs_ever,"\t\t*"
	print " * Hits: (this round)",hits,"\t\t*"
	print " * Misses: (this round)",misses,"\t\t*"
	print " * Total cities destroyed:",nukeouts,"    \t*"
	print " ****************************************\n"
	print "\n Please note that it is possible for more than one ABM to hit a single enemy missile\n"
	print ('\033[0m')	# back to normal
	print "\n\n\n"
	return (number_of_ICBMs,number_of_ABMs,enemy_salvoes,nukeouts)




############################ MAIN PROGRAM #######################################

print "\n\n\n\n\n\n\n\n\n"
#print "RR:",russian_roulette
print ('\033[91m'+'')
print "\n \t\t Splendid Strike",
print (''+'\033[0m')
print " \tA computer game by Andrew Wade."
print " \t(C) Copyright Andrew Wade 2017"
print "\n Please maximise this window for the best possible experience :-)"

try:
	cont = int(input("\n Press ENTER to continue"))
except:	
	print "",

print "\n You are",
print ('\033[3;33;40m'+' President Donald Trump...'+'\033[0m'),
print ' (sorry) '
print " "
print ('\033[3;33;40m'+'  It\'s a nice, quiet day. You\'re just getting down to a bit of light '+'\033[0m')
print ('\033[3;33;40m'+'  entertainment at the expense of libtardz, Commies and Rocket Man on  '+'\033[0m')
print ('\033[3;33;40m'+'  Twitter while fiddling around with all the buttons and things in your ')
print ('  special briefcase, when all of a sudden everyone completely loses it! '+'\033[0m')
print ('\033[3;33;40m'+'  An aide pops his head round the door and tells you in a breathless voice\n '+'\033[0m')
print "\t",
print ('\033[7;30;91m'+'   NUKES!!! COMMIE NUKES COMIN\' TO GET US!! '+'\033[0m')
print "\n";
print ('\033[3;33;40m'+'  You run to the desk of the Oval Office, where you had a computer '+'\033[0m')
print ('\033[3;33;40m'+'  terminal installed that connects you to the missile defence system.'+'\033[0m')
print ('\033[3;33;40m'+'  This allows YOU to control America\'s defences. You have the best '+'\033[0m')
print ('\033[3;33;40m'+'  defences, truly fantastic - and as the most talented bravest cleverest '+'\033[0m')
print ('\033[3;33;40m'+'  person in the world, YOU are the only one who knows how to beat those '+'\033[0m')
print ('\033[3;33;40m'+'  dirty Commies and SAVE AMERICA!'+'\033[0m')
print "\n";
print ('\033[3;33;40m'+'  Each ABM you fire has a 56% chance of hitting the enemy missiles '+'\033[0m')
print ('\033[3;33;40m'+'  that are raining down on God\'s Country like dollar bills in one of '+'\033[0m')
print ('\033[3;33;40m'+'  your very classy entertainment resorts. '+'\033[0m')
print "\n"
print ('\033[3;33;40m'+'  You can fire these singly or in salvoes, but because the enemy missiles '+'\033[0m')
print ('\033[3;33;40m'+'  come in SO DARNED FAST, you have to tell the computer how many ABMs '+'\033[0m')
print ('\033[3;33;40m'+'  to fire at each enemy ICBM in advance.'+'\033[0m')
print "\n";

try:
	cont = int(input("\n Press ENTER to start the game!"))
except:	
	print "",


print ""
print "  OK, I hope you're ready... starting in ",


print "3...",

print "2...",

print "1...",


print "\n\n\n"

print "\t\t ******************************"
print "\t\t *",
print ('\033[91m'+' WARNING! MISSILE ALERT!'+'\033[0m'),
#print ('\033[6m'+' WARNING! MISSILE ALERT!'+'\033[0m'),


print " *"
print "\t\t ******************************"
while (number_of_ICBMs > 0):
	(number_of_ICBMs,number_of_ABMs,enemy_salvoes,nukeouts) = main_loop(number_of_ICBMs, enemy_salvoes, number_of_ABMs, nukeouts, misses, hits, ICBMs_in_entire_war)


try:
	cont = int(input("\n Press ENTER to continue"))
except:	
	print "",

if (nukeouts == 0):
	print "\n"
	print "\n"
	print ('\033[1;37;44m'+'\t\t YOU WIN - BIGLY! \t\t')
	print (''+'\033[0m')

	print ('\033[1;37;44m'+' * * * * * *  '+'\033[0;31;41m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+'  * * * * * * '+'\033[2;37;47m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+' * * * * * *  '+'\033[0;31;41m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+'  * * * * * * '+'\033[2;37;47m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+' * * * * * *  '+'\033[0;31;41m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+'  * * * * * * '+'\033[2;37;47m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+' * * * * * *  '+'\033[0;31;41m'+'                    '+'\033[0m')
	print ('\033[2;37;47m'+'                                  '+'\033[0m')
	print ('\033[0;31;41m'+'                                  '+'\033[0m')
	print ('\033[2;37;47m'+'                                  '+'\033[0m')
	print ('\033[0;31;41m'+'                                  '+'\033[0m')
	print ('\033[2;37;47m'+'                                  '+'\033[0m')
	print ('\033[0;31;41m'+'                                  '+'\033[0m')
	print "\n\n YAAAAAY!! AMERICA HAS SURVIVED!!!"
	print "\n  YOU WIN AND ARE THE BEST PRESIDENT EVER!!!"
	print "\n Now the missile defence system has been proved"
	print "infallible, you can bomb all those OTHER places "
	print "you don't like! Where's your map and pin?"
	other_side_effects(nukeouts,ICBMs_in_entire_war)
	print "\n\n";

	if (russian_roulette > 15):
		PressEnter()
		print "\n\n\n"
		print "\n\n\n\n"
		print "\t\t\t BUT THEN....\n";
		print "\n Your partying is interrupted by the sound of a "
		print ('\033[7;30;91m'+'               VERY LOUD KLAXON!                '+'\033[0m')
		print ""
		print " The ",
		print ('\033[91m'+'BIG RED PHONE'+'\033[0m'),
		print " is ringing. You scoop it up and "
		print " who should it be but YOUR BOSS, Vladimir Putin!"
		print "\n"
		print " He is extremely distraught and yells at you "
		print ""
		print ('\033[1;37;44m'+'  \"What the f*** do you think you\'re doing you '+'\033[0m')
		print ('\033[7;30;91m'+'   f**ing c*cks*ck*r? I told you - don\'t F*CK  '+'\033[0m')
		print ('\033[0;30;47m'+'         with Mutha Russia!!!!\"                '+'\033[0m'),
		print ""
		print " Putin slams the phone down and you look up into "
		print " the panicked face of yet another aide."
		print ""
		print "  \"Mr. President, sir, it seems the Russians "
		print "    mistook our ABM launches for an attack! "
		print "       We gotta get ya to safety sir! \""
		print " "
		print ('\033[3;33;40m'+' \"No time for that Boy\"'+'\033[0m')+' you growl,',
		print ('\033[3;33;40m'+'\"I\'ll handle this!\"'+'\033[0m')
		print "\n\n"
		PressEnter()
		print "\n\n\n\n\n"
		print "\t\t ******************************"
		print "\t\t *",
		print ('\033[91m'+' WARNING! MISSILE ALERT!'+'\033[0m'),
		print " *"
		print "\t\t ******************************"



		number_of_ICBMs = random.randint(299,1801)
		ICBMs_in_entire_war = number_of_ICBMs
		enemy_salvoes = 1
		while (number_of_ICBMs > 0):
			(number_of_ICBMs,number_of_ABMs,enemy_salvoes,nukeouts) = main_loop(number_of_ICBMs, enemy_salvoes, number_of_ABMs, nukeouts, misses, hits, ICBMs_in_entire_war)


		


else:
	print "\n\t\t  YOU LOSE!"
	print "\n"
	print ('\033[3;33;40m'+' Well, I hope you\'re pleased with yourself. Only'), nukeouts
	print " American cities have been blown to smithereens. "
	other_side_effects(nukeouts,ICBMs_in_entire_war)
	print "\n Of course, North Korea has been reduced to its constituent "
	print " atoms, so there's always that."
	print "\n"
	print " Still, you'll be able to build some nice hotels and resorts "
	print " once all the dead bodies have been cleared away! "
	print " "	
	print " BTW, some gentlemen from INTERPOL want to talk to you about "
	print " war crimes charges..."
	print "\n They blame YOU for starting the war, for some reason. "
	print " \n \t \t I know, right? Ingrates!"
	print ('\n'+'\033[0m')



print "\n"

try:
	cont = int(input("\n Press ENTER for the sleeve notes..."))
except:	
	print "",

print "\n \n    This game was inspired by Ankit Panda and Vipin Narang's article in"
print "  War On The Rocks and Carnegie Endowment For International Peace, "
print " \"Deadly Overconfidence: Trump Thinks Missile Defenses Work Against North Korea,"
print " and That Should Scare You"
print "\n Read it here:\n https://warontherocks.com/2017/10/deadly-overconfidence-trump-thinks-missile-defenses-work-against-north-korea-and-that-should-scare-you/"
print "\n Or here: \n http://carnegieendowment.org/2017/10/17/deadly-overconfidence-trump-thinks-missile-defenses-work-against-north-korea-and-that-should-scare-you-pub-73451"
print "\n\n"
print "\n Also, see this: https://www.thedailybeast.com/how-a-north-korean-missile-could-accidentally-trigger-a-us-russia-nuclear-war"
print "\n If you have any CONSTRUCTIVE opinions to offer, please contact me via Twitter, "
print "where I go by @andywade"
print "\n\n"

try:
	cont = int(input("\n Press ENTER to exit..."))
except:	
	print "",

quit()





