# DESCRIPTION
#     This program uses the pyautogui library to automate interactions with a GUI. With just a few lines of code, you
#     can automate virtually any interaction, from clicking buttons and typing text to moving the cursor and simulating
#     mouse clicks. This uses the pyautogui library to provide smooth, natural movements, and with built-in
#     features like random jitter and variable speed, interactions look just like those performed by a real
#     person. Save time, increase productivity, and never perform another tedious manual task again.

import pyautogui
import time
import random
import string

def move_to_coordinates(
    coordinates,
    duration,
    easing_functions=[],
    jitter_range=(-5, 5),
    speed_range=(0.5, 1.5),
    moverel_range=(1, 3),
    moverel_duration_range=(0, 0.1)):

    # Add some random jitter to the coordinates to
    # make the movement of the cursor more natural and less robotic.
    jitter = (random.uniform(*jitter_range), random.uniform(*jitter_range))
    coordinates = (coordinates[0] + jitter[0], coordinates[1] + jitter[1])

    # Use the provided easing functions,
    # or default to the ones defined in the function if none were provided.
    if not easing_functions:
        easing_functions = [
            pyautogui.easeInQuad,
            pyautogui.easeOutQuad,
            pyautogui.easeInOutQuad]

    # Add some variation in the speed of the cursor movement.
    speed = random.uniform(*speed_range)

    # Move the cursor to the starting position.
    pyautogui.moveTo(
        coordinates,
        duration=duration / 2 * speed,
        tween=random.choice(easing_functions))

    # Add some random variation in the path of the cursor.
    for i in range(random.randint(*moverel_range)):
        pyautogui.moveRel(
            random.uniform(-10, 10),
            random.uniform(-10, 10),
            duration=random.uniform(*moverel_duration_range))

    # Move the cursor to the final destination.
    pyautogui.moveTo(
        coordinates,
        duration=duration / 2 * speed,
        tween=random.choice(easing_functions))

def __clicker(coordinates, duration):
    duration = random.uniform(
        duration * 0.8,
        duration * 1.2)
    move_to_coordinates(coordinates, duration)
    pyautogui.click(coordinates)

def shoot_invader(duration, count):
    for i in range(count):
        __clicker((327, 682), 0.4, 0.1)
        time.sleep(duration)
    __clicker((519, 680), 0.4, 0.1)

def generate_random_string(size):
    return ''.join(
        random.choices(
            string.ascii_lowercase,
            k=size))

def __writer(string, chunk_length=7, typing_speed_range=(0.05, 0.1)):
    chunks = [string[i:i+chunk_length]
        for i in range(0, len(string), chunk_length)]

    for chunk in chunks:
        pyautogui.typewrite(
            chunk,
            interval=random.uniform(*typing_speed_range))

    pyautogui.press('enter')


# INVADERS
# def main():
#     clicks = [
# 		((363, 119), 1.2), # navigator
# 		((686, 419), 0.9), # invader location
# 		((342, 596), 0.7), # yes, go
# 		((331, 559), 1),   # location under it
#         ((537, 609), 0.5), # apply
#         ((342, 601), 0.5), # yes
#         ((514, 425), 0.7)] # click invader

#     for click in clicks:
#         coordinates, duration = click
#         __clicker(coordinates, duration)
#     shoot_invader(6.5, 25)


# TASKS
def main():
    clicks = [
		((363, 119), 0.5),
		((686, 419), 0.5)]

    while True:
        for click in clicks:
            __clicker(*click)

if __name__ == "__main__":
    main()
