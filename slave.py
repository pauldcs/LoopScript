#
#   slave.py
#   By: <pducos@student.42.fr>
#
# DESCRIPTION
#     This allows you to write scripts to simulate mouse and keyboard events on a computer.
#     The script language supports the following commands:
#
    ##############################################################################
    #
	#     CLICK
	#         Syntax: CLICK (minX, minY) (maxX, maxY) (duration, wait);
    #
	#         Description: Simulates a mouse click within the
	# 			specified rectangle on the screen. 
	#           Duration = time to move to click location.
	#           wait = time to wait after clicking
    #           
	#         Example:
	#             CLICK
	#                  (540, 240)
	#                  (540, 240)
	#	               (1.0, 1.5);
	#
	##############################################################################
    #
	#     WRITE
	#         Syntax: WRITE "string";
    #
	#         Description: Simulates typing the specified string on the keyboard.
    #
	#         Example:
	#             WRITE "Hello world!";
    #
	###############################################################################
	#
	#     WRITE_RSTR
	#         Syntax:		WRITE_RSTR n_chars;
    #
	#         Description:	Simulates typing a randomly generated string of 
	# 						the specified number of characters.
	#
	#         Example:
	#             WRITE_RSTR 10;
    #
	##############################################################################
	#
	#     WRITE_RTEXT
	#         Syntax: WRITE_RTEXT n_words;
    #
	#         Description: Simulates typing a english text string of the
	# 			specified number of words.
    #
	#         Example:
	#             WRITE_RTEXT 5;
    #
	##############################################################################
	#
	#     WAIT
	#         Syntax: WAIT n_secs;
    #
	#         Description: waits.
    #
	#         Example:
	#             WAIT 5;
	#
	##############################################################################
#
#! python3

import pyautogui
import time
import random
import string
import re


print ("""
__________         _________.__
\\______   \\___.__./   _____/|  | _____ __  __ ____
 |     ___<   |  |\\_____  \\ |  | \__  \\  \\/ // __ \\
 |    |    \\___  |/        \\|  |__/ __ \\   /\\  ___/
 |____|    / ____/_______  /|____(___  /\_/  \\___  >
		   \\/            \\/          \\/          \\/
""")


POSITION_DOWN = ((330,  360), (525,  550))
POSITION_LEFT = ((330,  360), (430,  455))
POSITION_UP   = ((480,  510), (430,  450))
POSITION_RIGHT= ((480,  510), (525,  545))


def random_inrange(min_value=0, max_value=100):
	return random.randint(min_value, max_value)


def random_afk():
	if random.randint(1, 666) == 1:
		sleep_time = random.uniform(0, 120)
		print("Going afk, back in {} seconds".format(sleep_time))
		time.sleep(sleep_time)


def human_type(
		string, chunk_length=7,
		typing_speed_range=(0.01, 0.03),
		hand_movement_delay=0.1,
		thinking_delay=0.09,
		space_delay=0.1):
	chunks = [string[i:i+chunk_length]
			  for i in range(0, len(string), chunk_length)]
	for chunk in chunks:
		time.sleep(hand_movement_delay)
		for character in chunk:
			if character == ' ':
				pyautogui.press('space')
				time.sleep(space_delay)
			else:
				pyautogui.typewrite(
					character,
					interval=random.uniform(*typing_speed_range))
		time.sleep(thinking_delay)
	pyautogui.press('enter')


def human_click():
	x, y = pyautogui.position()
	x += random.uniform(-2.5, 2.5)
	y += random.uniform(-2.5, 2.5)
	pyautogui.moveTo(x, y)
	for i in range(3):
		dx = random.uniform(-1, 1)
		dy = random.uniform(-1, 1)
		pyautogui.moveRel(dx, dy, duration=0.01)
	time.sleep(random.uniform(0.1, 0.3))
	button = "left"
	duration = random.uniform(0.1, 0.5)
	pyautogui.mouseDown(button=button, duration=duration)
	pyautogui.mouseUp(button=button, duration=duration)


def move_cursor(coordinates, duration=0.7, easing_functions=[]):
	jitter = (
		random.uniform(-5, 5),
		random.uniform(-5, 5))
	coordinates = (
		coordinates[0] + jitter[0],
		coordinates[1] + jitter[1])
	if not easing_functions:
		easing_functions = [
			pyautogui.easeInQuad,
			pyautogui.easeOutQuad,
			pyautogui.easeInOutQuad,
			pyautogui.easeInOutSine]
	speed = random.uniform(0.70, 1.30)
	pyautogui.moveTo(
		coordinates,
		duration=(duration * speed),
		tween=random.choice(easing_functions))
	for i in range(random.randint(0, 2)):
		pyautogui.moveRel(
			random.uniform(-7, 7),
			random.uniform(-7, 7),
			duration=random.uniform(0, 0.1))
	pyautogui.moveTo(
		coordinates,
		duration=duration / 4,
		tween=random.choice(easing_functions))


def click_spot(coordinates, duration=1):
	move_cursor(coordinates, duration)
	human_click()


def generate_random_string(size):
	return ''.join(
		random.choices(
			string.ascii_lowercase,
			k=size))

def generate_random_text(
		the_words=None,
		include_punctuation=False,
		include_digits=False):
	text = ""
	words = [
		"the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it","for", "not", "on", "with", 
		"as", "you", "do", "at", "this", "but", "his", "by", "from", "us", "we", "say", "her", "she", "or",
		"an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", 
		"who", "get", "which", "go", "me", "when", "make", "can", "like", "he", "time", "no", "just", "him", "know",
		"take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", 
		"then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use",
		"two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", 
		"these", "give", "day", "most", "they",
	]
	word_pairs = [
		("above", "the"), ("across", "the"), ("after", "the"), ("against", "the"), ("along", "the"),
		("among", "the"), ("around", "the"), ("at", "the"), ("before", "the"), ("behind", "the"),
		("below", "the"), ("beneath", "the"), ("beside", "the"), ("between", "the"), ("by", "the"),
		("down", "the"), ("during", "the"), ("except", "the"), ("for", "the"), ("from", "the"),
		("in", "the"), ("inside", "the"), ("into", "the"), ("like", "the"), ("near", "the"),
		("of", "the"), ("off", "the"), ("on", "the"), ("onto", "the"), ("out of", "the"),
		("outside", "the"), ("over", "the"), ("past", "the"), ("since", "the"), ("through", "the"),
		("throughout", "the"), ("till", "the"), ("to", "the"), ("toward", "the"), ("under", "the"),
		("underneath", "the"), ("until", "the"), ("up", "the"), ("upon", "the"), ("with", "the"),
		("within", "the"), ("without", "the"), ("and", "the"), ("but", "the"), ("or", "the"),
		("nor", "the"), ("for", "the"), ("yet", "the"), ("so", "the"), ("as", "the"), ("when", "the"),
		("where", "the"), ("why", "the"), ("how", "the"), ("while", "the"), ("if", "the"), ("because", "the"),
		("as if", "the"), ("though", "the"), ("even though", "the"), ("as though", "the"),
		("whether or not", "the"), ("in order that", "the"), ("in case", "the"), ("in the event that", "the"),
		("provided that", "the"), ("unless", "the"), ("until", "the"), ("before", "the"), ("after", "the"),
		("once", "the"), ("whenever", "the"), ("while", "the"), ("as soon as", "the"), ("as long as", "the"),
		("whenever", "the"), ("wherever", "the"), ("whoever", "the"), ("however", "the"), ("whatever", "the"),
		("whichever", "the"), ("no matter how", "the"), ("in spite of", "the"), ("regardless of", "the"),
		("whereas", "the"), ("otherwise", "the"), ("as much as", "the"),
		("rather than", "the"), ("in addition to", "the"), ("likewise", "the"), ("similarly", "the"),
		("furthermore", "the"), ("moreover", "the"), ("instead", "the")
	]
	adjectives = [
		"beautiful", "handsome", "ugly", "happy", "sad", "angry", "fierce", "scary", "powerful", "strong",
		"weak", "big", "small", "tiny", "gigantic", "fat", "thin", "old", "new", "young", "bright", "dark",
		"light", "heavy", "smooth", "rough", "soft", "hard", "shiny", "dull", "quiet", "noisy", "loud",
		"fascinating", "mysterious", "curious", "enigmatic", "perplexing", "enigmatic",
		"bizarre", "strange", "peculiar", "uncommon", "unexpected", "unprecedented", "unanticipated", 
		"extraordinary", "unbelievable", "remarkable", "astounding", "amazing", "incredible", "unbelievable",
		"miraculous", "phenomenal", "prodigious", "stupendous", "miraculous", "sublime", "splendid",
		"delightful", "enjoyable", "pleasurable", "wonderful", "splendid", "fabulous", "breathtaking",
		"awe-inspiring", "mind-blowing", "incredible", "fabulous", "splendid", "delightful", "dazzling", 
		"stunning", "gorgeous", "breathtaking", "magnificent", "resplendent", "splendid", "beautiful", 
		"majestic", "splendid", "grand", "grandiose", "opulent", "luxurious", "deluxe", "sumptuous", 
		"ornate", "elegant", "refined", "graceful", "delicate", "exquisite", "intricate", "detailed", 
		"intricate", "captivating", "mesmerizing", "enchanting", "bewitching", "enthralling", "hypnotic",
		"spellbinding", "mesmerizing", "alluring", "seductive", "charming", "graceful", "ravishing", 
		"appealing", "pleasant", "inviting", "cozy", "comfortable", "warm", "inviting", "hospitable",
		"genial", "friendly", "amicable", "sociable", "companionable", "convivial", "jovial", "merry",
		"happy", "joyful", "lively", "vibrant", "animated", "marvellous", "radiant", "glorious", "regal",
		"complex", "delightful", "welcoming", "cheerful",
	]
	office_words = [
		"office", "workplace", "workspace", "corporate",
		"business", "enterprise", "company", "organization",
		"firm", "incorporation", "institution", "agency",
		"department", "division", "unit", "team", "staff",
		"employee", "colleague", "associate", "partner", "manager",
		"supervisor", "executive", "director", "officer", "leader",
		"coordinator", "facilitator", "consultant", "analyst",
		"specialist", "expert", "advisor", "mentor", "coach", "trainer",
		"instructor", "teacher", "professor", "lecturer", "researcher",
		"scientist", "engineer", "technician", "assistant", "associate",
		"aide", "assistant", "helper", "support", "service", "maintenance",
		"operation", "production", "manufacturing", "development", "design",
		"innovation", "creativity", "strategy", "planning", "policy",
		"regulation", "law", "compliance", "ethics", "standards",
		"quality", "performance", "measurement", "assessment", "evaluation",
		"feedback", "analysis", "synthesis", "solution", "resolution",
		"decision", "choice", "option", "variation", "alternative",
		"possibility", "probability", "risk", "uncertainty", "diversity",
		"inclusion", "equity", "fairness", "justice", "rights", "opportunity",
		"access", "mobility", "flexibility", "adaptability", "agility",
		"resilience", "sustainability", "growth", "expansion", "increase",
		"improvement", "advancement", "success", "achievement", "recognition",
		"reward", "compensation", "benefits", "perks", "incentives", "bonuses",
		"allowances", "pensions", "retirement", "security", "safety",
		"health", "wellness", "happiness", "satisfaction", "fulfilment",
		"purpose", "meaning", "value", "culture", "tradition", "custom",
		"habit", "routine", "rule", "protocol", "procedure", "process",
		"system", "method", "technique", "approach", "tool", "resource",
		"asset", "capital", "investment", "funding", "budget", "cost", "expense",
		"charge", "fee", "price", "value", "worth", "profit", "gain", "loss",
		"impact", "consequence", "result", "outcome", "effect", "influence", "change",
		"transformation", "evolution", "progress", "movement", "shift", "trend",
		"pattern", "structure", "hierarchy", "order", "rank", "class", "status",
		"position", "role", "function", "responsibility", "duty", "obligation",
		"commitment", "dedication", "focus", "attention", "awareness", "concentration",
		"observation", "perception", "sensation", "intuition", "insight", "understanding",
		"comprehension", "knowledge"
	]
	punctuation = [".", "?", "!", ",", ":", ";"]
	num_words = random.randint(5, 10)
	capitalize_first_word = random.random() < 0.5

	if the_words == None:
		the_words = office_words
	for i in range(num_words):
		if i > 0:
			text += " "
		if random.random() < 0.5:
			pair = random.choice(word_pairs)
			text += pair[0] + " " + pair[1]
		elif random.random() < 0.25:
			adjective = random.choice(adjectives)
			noun = random.choice(words)
			text += adjective + " " + noun
		else:
			word = random.choice(words)
			if capitalize_first_word and i == 0:
				word = word.capitalize()
			text += word
		last_word = text.split()[-1]
		if last_word == "the" and the_words:
			text += " " + random.choice(the_words)
	if include_punctuation:
		text += random.choice(punctuation)
	if include_digits:
		text += str(random.randint(0, 9))
	return text


def press_backspace(n_times):
	for i in range(n_times):
		pyautogui.press("backspace")

######################################################################

# import csv
# from io import StringIO

# def parse_click_path(contents):
#     clicks = []
#     reader = csv.reader(StringIO(contents), delimiter=' ')
#     for row in reader:
#         if len(row) != 6:
#             raise ValueError('Invalid config file format')
#         try:
#             x = (int(row[0]), int(row[2]))
#             y = (int(row[1]), int(row[3]))
#             duration = float(row[4])
#             wait = float(row[5])
#         except ValueError:
#             raise ValueError('Invalid config file format')
#         click = ((x, y), (duration, wait))
#         clicks.append(click)
#     return clicks

# def parse_click_path(config_file):
#     clicks = []
	
#     with open(config_file, 'r') as f:
#         for line in f:
#             # Skip empty lines and lines that start with '#'
#             parts = line.split('#', 1)[0].strip()
#             if not parts:
#                 continue
				
#             parts = parts.split()
#             if len(parts) != 6:
#                 raise ValueError('Invalid config file format')
#             try:
#                 x = (
#                     int(parts[0]), int(parts[2]))
#                 y = (int(parts[1]), int(parts[3]))
#                 duration = float(parts[4])
#                 wait = float(parts[5])
#             except ValueError:
#                 raise ValueError('Invalid config file format')
#             click = ((x, y), (duration, wait))
#             clicks.append(click)
			
#     return clicks

######################################################################

# INVADERS
# def shoot_invader(duration, count):
# 	bonus = 0
# 	print ("Thank you next")
# 	for i in range(count):
# 		print (f"  - ({bonus}%) Normal attack...", end="\r")
# 		click_spot((327, 682), 0.4)
# 		bonus += 15
# 		time.sleep(duration)
# 	print (f"\n  ! Enhanced attack...")
# 	click_spot((519, 680), 0.4)

# def main():
# 	time.sleep(1)
# 	count = 0
# 	clicks_1 = parse_click_path('tasks/00_invaders.conf')
# 	clicks_2 = parse_click_path('tasks/01_invaders.conf')

# 	while True:
# 		choice = 0
# 		count += 1
# 		print (f"[loop: '{count}']", end ="\r")
# 		for i, click in enumerate(clicks_1):
# 			coords = click[0]
# 			duration = click[1][0]
# 			wait = click[1][1]
# 			if i == 3:
# 				choice = random.randint(1, 4)

# 				if   choice == 1:   coords = POSITION_DOWN
# 				elif choice == 2:   coords = POSITION_LEFT
# 				elif choice == 3:   coords = POSITION_UP
# 				elif choice == 4:   coords = POSITION_RIGHT

# 			click_spot((
# 					random.uniform(coords[0][0], coords[0][1]),
# 					random.uniform(coords[1][0], coords[1][1])),
# 				duration)
# 			time.sleep(wait)

# 		if   choice == 1:   coords = POSITION_UP
# 		elif choice == 2:   coords = POSITION_RIGHT
# 		elif choice == 3:   coords = POSITION_DOWN
# 		elif choice == 4:   coords = POSITION_LEFT

# 		click_spot((
# 				random.uniform(coords[0][0], coords[0][1]),
# 				random.uniform(coords[1][0], coords[1][1])),
# 			duration)

# 		shoot_invader(7.2, 25)

# 		for i, click in enumerate(clicks_2):
# 			coords = click[0]
# 			duration = click[1][0]
# 			wait = click[1][1]
# 			click_spot((
# 					random.uniform(coords[0][0], coords[0][1]),
# 					random.uniform(coords[1][0], coords[1][1])),
# 				duration)
# 			time.sleep(wait)

# TASKS
# def main():
#     count = 0
#     clicks = [
#         #  min_x max_x  min_y max_y  duration
#         (((502,  559), (690,  697)), 0.25),
#         (((542,  602), (737,  742)), 0.25)]

#     while True:
#         count += 1
#         print (f"[loop: '{count}']", end ="\r")
#         for click in clicks:
#             coords = click[0]
#             duration = click[1]
#             x = random.uniform(coords[0][0], coords[0][1])
#             y = random.uniform(coords[1][0], coords[1][1])
#             click_spot((x, y), duration)

# RENAME
# def main():
#     clicks_1 = [
# 		((519, 462), 0.5),
# 		((402, 424), 0.3),
# 		((402, 424), 0.2)]

#     clicks_2 = [
# 		((535, 624), 0.3)]

#     count = 0
#     while True:
#         count += 1
#         print (f"[loop: '{count}']", end ="\r")
#         for click in clicks_1:
#             click_spot(*click)
#         press_backspace(16)
#         human_type(
#             generate_random_string(random_inrange(8, 16)))
#         for click in clicks_2:
#             click_spot(*click)

##########################################################################

# CLICK command
click_regex = re.compile(
    r"CLICK[\s\t\n]+"
    r"\((?P<minX>\d+),[\s\t\n]+(?P<minY>\d+)\)[\s\t\n]+"
    r"\((?P<maxX>\d+),[\s\t\n]+(?P<maxY>\d+)\)[\s\t\n]+"
    r"\((?P<duration>[\d.]+),[\s\t\n]+(?P<wait>[\d.]+)\)"
)
# WRITE command
write_regex = re.compile(
    r"WRITE[\s\t\n]+\"(?P<str>.*)\""
)
# WRITE_RTEXT command
write_rtext_regex = re.compile(
    r"WRITE_RTEXT[\s\t\n]+(?P<n_words>\d+)"
)
# WRITE_RSTR command
write_rstr_regex = re.compile(
    r"WRITE_RSTR[\s\t\n]+(?P<n_chars>\d+)"
)
# WAIT command
wait_regex = re.compile(
    r"WAIT[\s\t\n]+(?P<n_secs>\d+)"
)

def parse_command(command):
	click_match = click_regex.search(command)
	if click_match:
		operands = click_match.groupdict()
		print(operands)
		return
	write_match = write_regex.search(command)
	if write_match:
		operands = write_match.groupdict()
		print(operands)
		return
	write_rtext_match = write_rtext_regex.search(command)
	if write_rtext_match:
		operands = write_rtext_match.groupdict()
		print(operands)
		return
	write_rstr_match = write_rstr_regex.search(command)
	if write_rstr_match:
		operands = write_rstr_match.groupdict()
		print(operands)
		return
	wait_match = wait_regex.search(command)
	if wait_match:
		operands = wait_match.groupdict()
		print(operands)
		return
	
	else:
		print(f"Error: invalid command '{command}'")

def parse_commands(commands):
	for command in commands:
		parse_command(command)

def main():
    try:
        with open("script.sv", "r") as f:
            lines = f.read().split(";")
            lines = [line.strip() for line in lines]
            parse_commands(lines)
    except IOError:
        print("An error occurred while reading 'script.txt'")

if __name__ == "__main__":
	main()
