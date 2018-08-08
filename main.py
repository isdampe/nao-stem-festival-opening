import sys, time, animations
from naoqi import ALProxy

class Welcome:

	def __init__(self, ip, port):
		self.tts = ALProxy("ALTextToSpeech", ip, port)
		self.animatedSpeech = ALProxy("ALAnimatedSpeech", ip, port)
		self.posture = ALProxy("ALRobotPosture", ip, port)
		self.motion = ALProxy("ALMotion", ip, port)
		self.ip = ip

	def go(self):
		self.posture.goToPosture("Stand", 1.0);
		time.sleep(2.0)

		self.animatedSpeech.say("On behalf of St Margaret's and Berwick " \
			"Grammar School, ^start(animations/Stand/Gestures/Hey_1) " \
			"I would like to welcome you to the Game Changers " \
			"and Change Makers STEM Festival ^wait(animations/Stand/Gestures/Hey_1) " \
			" in partnership with the Day of Stem, and the Australian College " \
			"of Educators. ^run(animations/Stand/Gestures/BowShort_1)")

		time.sleep(1.0)
		self.animatedSpeech.say("^start(animations/Stand/Gestures/Explain_1	) " \
			"I know that robots like me are being used to " \
			"teach Aboriginal Languages, and this illustrates the complementarity" \
			"of the ancient and the new ^wait(animations/Stand/Gestures/Explain_1).");

		time.sleep(1.0)
		self.animatedSpeech.say(" In some ways, this sums up our event. " \
			"^run(animations/Stand/Gestures/IDontKnow_1).")

		self.animatedSpeech.say("^start(animations/Stand/Gestures/YouKnowWhat_1) " \
			"This also sums up where our culture is going. " \
			"^wait(animations/Stand/Gestures/YouKnowWhat_1)" \
			"We can use the new to not only capture, preserve and strengthen " \
			"the past, ^start(animations/Stand/Gestures/Enthusiastic_4) " \
			"but also to shape the future. ^wait(animations/Stand/Gestures/Enthusiastic_4)");

		time.sleep(1.0)

		self.animatedSpeech.say("The advancements of the present")
		time.sleep(0.15)
		self.animatedSpeech.say(" shape the " \
			"life ^start(animations/Stand/Gestures/YouKnowWhat_5) opportunities " \
			"of our young people in the future ")
		time.sleep(0.15)
		self.animatedSpeech.say("through influencing the worlds of education")
		time.sleep(0.15)
		self.animatedSpeech.say("careers")
		time.sleep(0.25)
		self.animatedSpeech.say(" and communication." \
			"^wait(animations/Stand/Gestures/YouKnowWhat_5)")

		time.sleep(1.0)

		self.animatedSpeech.say("This is indeed a time where not only is the " \
			"game changing")
		time.sleep(0.5)
		self.animatedSpeech.say("but the rules of the game are changing. "  \
			"^start(animations/Stand/Gestures/Thinking_1) The new " \
			"rules are being formulated by those prepared to think in new and " \
			"different ways ^wait(animations/Stand/Gestures/Thinking_1)")
		time.sleep(0.5)
		self.animatedSpeech.say("but ways that must be informed by a strong sense " \
			"of what we believe is right.");

		time.sleep(1.0)


		self.animatedSpeech.say("As a result, ^start(animations/Stand/Gestures/Yes_1)" \
		 	" we need to ensure that those " \
			"that make those new rules are as knowledgeable and wise as " \
			"possible. ^wait(animations/Stand/Gestures/Yes_1).");

		time.sleep(1.0)

		self.animatedSpeech.say("Which brings me back to this event.")
		self.animatedSpeech.say("It is to ")
		time.sleep(0.1)
		self.animatedSpeech.say("^start(animations/Stand/Gestures/Enthusiastic_4)" \
			" inform ^wait(animations/Stand/Gestures/Enthusiastic_4)")
		self.animatedSpeech.say("inspire")
		time.sleep(0.1)
		self.animatedSpeech.say("and hopefully cause deep reflection so that we " \
			"may be the ^start(animations/Stand/Gestures/ShowSky_1) best we " \
			"can be for all humanity and the planet. " \
			"^wait(animations/Stand/Gestures/ShowSky_1)");

		time.sleep(2.5)

		self.animatedSpeech.say("On behalf of the Principal of Margaret's and " \
			"Berwick Grammar School")
		self.animatedSpeech.say("Miss Annette Rome")
		self.animatedSpeech.say("^start(animations/Stand/Gestures/ShowSky_9) " \
			"I wish you all a stimulating and challenging " \
			"time ^wait(animations/Stand/Gestures/ShowSky_9)")
		time.sleep(0.25)
		self.animatedSpeech.say("^start(animations/Stand/Gestures/Enthusiastic_5) " \
			"and, I declare Game Changers and Change Makers open! ^wait(animations/Stand/Gestures/Enthusiastic_5)");

		time.sleep(1.0)
		animations.wipe(self.motion)
		time.sleep(1.0)
		self.animatedSpeech.say("^run(animations/Stand/Gestures/BowShort_1)")
		time.sleep(5.0)
		self.posture.goToPosture("Sit", 1.0);
		self.motion.rest()

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Usage: python main.py [hostname] [port]"
		sys.exit(1)

	w = Welcome(sys.argv[1], int(sys.argv[2]))
	w.go()