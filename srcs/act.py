import pyautogui
import time
import random
import string

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

def click_spot(coordinates, duration=0.3):
	move_cursor(coordinates, duration)
	human_click()

def generate_random_string(size):
	return ''.join(
		random.choices(
			string.ascii_lowercase,
			k=size))