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

def random_inrange(min_value=0, max_value=100):
    return random.randint(min_value, max_value)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_coordinates(min_x=0, max_x=1920, min_y=0, max_y=1080):
    return (random.randint(min_x, max_x), random.randint(min_y, max_y))

def move_cursor_randomly(duration):

    coordinates = random_coordinates()
    jitter = (random.uniform(-5, 5), random.uniform(-5, 5))
    coordinates = (
        coordinates[0] + jitter[0],
        coordinates[1] + jitter[1])

    easing_functions = [
        pyautogui.easeInQuad,
        pyautogui.easeOutQuad,
        pyautogui.easeInOutQuad]

    speed = random.uniform(0.5, 1.5)

    pyautogui.moveTo(
        coordinates,
        duration=duration / 2 * speed,
        tween=random.choice(easing_functions))

    for i in range(random.randint(1, 3)):
        pyautogui.moveRel(
            random.uniform(-10, 10),
            random.uniform(-10, 10),
            duration=random.uniform(0, 0.1))

    pyautogui.moveTo(
        coordinates,
        duration=duration / 2 * speed,
        tween=random.choice(easing_functions))

def click_randomly(duration):

    coordinates = random_coordinates()
    move_cursor(coordinates, duration)
    pyautogui.click(coordinates)

def random_sleep():
    if random.randint(1, 222) == 1:
        sleep_time = random.uniform(0, 120)
        print("Going to sleep for {} seconds".format(sleep_time))
        time.sleep(sleep_time)

def move_cursor(coordinates, duration, easing_functions=[]):
    """ Move the cursor to the specified 
        coordinates with natural-looking movements."""
    # Add some random jitter to the coordinates to make
    # the movement more natural.
    jitter = (random.uniform(-5, 5), random.uniform(-5, 5))
    coordinates = (
        coordinates[0] + jitter[0],
        coordinates[1] + jitter[1])

    # Use the provided easing functions,
    # or default to some common ones if none were provided.
    if not easing_functions:
        easing_functions = [
            pyautogui.easeInQuad,
            pyautogui.easeOutQuad,
            pyautogui.easeInOutQuad]

    # Add some variation in the speed of the cursor movement.
    speed = random.uniform(0.5, 1.5)

    # Move the cursor to the starting position.
    pyautogui.moveTo(
        coordinates,
        duration=duration / 2 * speed,
        tween=random.choice(easing_functions))

    # Add some random variation in the path of the cursor.
    for i in range(random.randint(1, 3)):
        pyautogui.moveRel(
            random.uniform(-10, 10),
            random.uniform(-10, 10),
            duration=random.uniform(0, 0.1))

    # Move the cursor to the final destination.
    pyautogui.moveTo(
        coordinates,
        duration=duration / 2 * speed,
        tween=random.choice(easing_functions))

def __clicker(coordinates, duration=0.4):
    """ Click at the specified coordinates
        with natural-looking movements and timing."""
    # Add some random variation to the duration of the click.
    duration = random.uniform(duration * 0.8, duration * 1.2)
    move_cursor(coordinates, duration)

    # Attempt to click at the specified coordinates. If a FailSafeException is raised (e.g. because the cursor
    # moved outside of the screen), try clicking again with the same parameters.
    try:
        pyautogui.click(coordinates)
    except pyautogui.FailSafeException:
        __clicker(coordinates, duration)


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

def __writer(
        string,
        chunk_length=7,
        typing_speed_range=(0.05, 0.1)):
    chunks = [string[i:i+chunk_length]
        for i in range(0, len(string), chunk_length)]

    for chunk in chunks:
        pyautogui.typewrite(
            chunk,
            interval=random.uniform(*typing_speed_range))

    pyautogui.press('enter')

def random_sleep():
    if random.randint(1, 222) == 1:
        sleep_time = random.uniform(0, 120)
        print("Going to sleep for {} seconds".format(sleep_time))
        time.sleep(sleep_time)

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
    count = 0
    clicks = [
		((363, 119), 0.5),
		((686, 419), 0.5)]
    move_cursor_randomly(10)
    while True:
        count += 1
        print (f"[loop: '{count}']", end ="\r")
        for click in clicks:
            __clicker(*click)

# RENAME
# def main():
#     clicks_1 = [
# 		((363, 119), 0.5),
# 		((686, 419), 0.5)]

#     clicks_2 = [
# 		((363, 119), 0.5),
# 		((686, 419), 0.5)]

#     while True:
#         for click in clicks_1:
#             __clicker(*click)
#         __writer(generate_random_string(random.uniform(8, 16)))
#         for click in clicks_2:
#             __clicker(*click)


if __name__ == "__main__":
    main()
