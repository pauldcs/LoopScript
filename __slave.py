#
#   __slave.py
#   By: <pducos@student.42.fr>
#
# DESCRIPTION
#     This program uses the pyautogui library to automate interactions with a GUI. With just a few lines of code, you
#     can automate virtually any interaction, from clicking buttons and typing text to moving the cursor and simulating
#     mouse clicks. This uses the pyautogui library to provide smooth, natural movements, and with built-in
#     features like random jitter and variable speed, interactions look just like those performed by a real
#     person. Save time, increase productivity, and never perform another tedious manual task again.
#

import pyautogui
import time
import random
import string

POSITION_DOWN = ((330,  360), (525,  550))
POSITION_LEFT = ((330,  360), (430,  455))
POSITION_UP   = ((480,  510), (430,  450))
POSITION_RIGHT= ((480,  510), (525,  545))

def random_inrange(min_value=0, max_value=100):
    return random.randint(min_value, max_value)

# def random_coordinates(min_x=0, max_x=1920, min_y=0, max_y=1080):
#     return (random.randint(min_x, max_x), random.randint(min_y, max_y))

# def move_cursor_randomly(duration):
#     coordinates = random_coordinates()
#     jitter = (random.uniform(-5, 5), random.uniform(-5, 5))
#     coordinates = (
#         coordinates[0] + jitter[0],
#         coordinates[1] + jitter[1])
#     easing_functions = [
#         pyautogui.easeInQuad,
#         pyautogui.easeOutQuad,
#         pyautogui.easeInOutQuad]
#     speed = random.uniform(0.5, 1.5)
#     pyautogui.moveTo(
#         coordinates,
#         duration=duration / 2 * speed,
#         tween=random.choice(easing_functions))
#     for i in range(random.randint(1, 3)):
#         pyautogui.moveRel(
#             random.uniform(-5, 5),
#             random.uniform(-5, 5),
#             duration=random.uniform(0, 0.1))
#
#     pyautogui.moveTo(
#         coordinates,
#         duration=duration / 2 * speed,
#         tween=random.choice(easing_functions))

# def click_randomly(duration):
#     coordinates = random_coordinates()
#     move_cursor(coordinates, duration)
#     pyautogui.click(coordinates)

def random_sleep():
    if random.randint(1, 666) == 1:
        sleep_time = random.uniform(0, 120)
        print("Going to sleep for {} seconds".format(sleep_time))
        time.sleep(sleep_time)


def move_cursor(coordinates, duration, easing_functions=[]):
    # Add some random jitter to the coordinates to make
    # the movement more natural.
    jitter = (
        random.uniform(-5, 5),
        random.uniform(-5, 5))
    coordinates = (
        coordinates[0] + jitter[0],
        coordinates[1] + jitter[1])
    # Use the provided easing functions,
    # or default to some common ones if none were provided.
    random_sleep()
    if not easing_functions:
        easing_functions = [
            pyautogui.easeInQuad,
            pyautogui.easeOutQuad,
            pyautogui.easeInOutQuad,
            pyautogui.easeInOutElastic,
            pyautogui.easeInOutSine,
            pyautogui.easeOutBounce]
    # Add some variation in the speed of the cursor movement.
    speed = random.uniform(0.5, 1.5)
    # Move the cursor to the starting position.
    pyautogui.moveTo(
        coordinates,
        duration=duration / 2 * speed,
        tween=random.choice(easing_functions))
    # Add some random variation in the path of the cursor.
    for i in range(random.randint(0, 3)):
        pyautogui.moveRel(
            random.uniform(-7, 7),
            random.uniform(-7, 7),
            duration=random.uniform(0, 0.1))
    # Move the cursor to the final destination.
    pyautogui.moveTo(
        coordinates,
        duration=duration / 2 * speed,
        tween=random.choice(easing_functions))


def __click(coordinates, duration=0.4):
    # Add some random variation to the duration of the click.
    duration = random.uniform(duration * 0.8, duration * 1.2)
    move_cursor(coordinates, duration)
    # Attempt to click at the specified coordinates.
    # If a FailSafeException is raised (e.g. because the cursor
    # moved outside of the screen), try clicking
    # again with the same parameters.
    try:
        pyautogui.click(coordinates)
    except pyautogui.FailSafeException:
        __click(coordinates, duration)


def generate_random_string(size):
    return ''.join(
        random.choices(
            string.ascii_lowercase,
            k=size))


def press_backspace(num_times):
    for i in range(num_times):
        pyautogui.press("backspace")


def __write(string, chunk_length=7, typing_speed_range=(0.05, 0.1)):
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


def shoot_invader(duration, count):
    bonus = 0
    print ("Thank you next")
    for i in range(count):
        print (f"  - ({bonus}%) Normal attack...", end="\r")
        __click((327, 682), 0.4)
        bonus += 15
        time.sleep(duration)
    print (f"\n  ! Enhanced attack...")
    __click((519, 680), 0.4)


# INVADERS
def main():
    count = 0
    clicks_1 = [
        (((317,  330), (114,  123)), 3),     # Navigator
        (((673,  709), (417,  421)), 1),     # Invader's location
        (((316,  378), (594,  603)), 0.8),   # Yes, go to coordinates
        (((317,  356), (548,  579)), 0.8),   # Location down
        (((507,  564), (582,  595)), 0.7),   # Apply
        (((318,  375), (596,  603)), 0.7)]   # Yes
    
    clicks_2 = [
        (((600,  610), (320,  320)), 2)]   # Red cross

    time.sleep(0.7)

    while True:
        choice = 0
        count += 1
        print (f"[loop: '{count}']", end ="\r")
        for i, click in enumerate(clicks_1):
            coords = click[0]
            duration = click[1]
            if click == (((317,  356), (548,  579)), 0.8):
               
                choice = random.randint(1, 4)

                if   choice == 1:   coords = POSITION_DOWN
                elif choice == 2:   coords = POSITION_LEFT
                elif choice == 3:   coords = POSITION_UP
                elif choice == 4:   coords = POSITION_RIGHT
                
            __click((
                random.uniform(coords[0][0], coords[0][1]),
                random.uniform(coords[1][0], coords[1][1])),
            duration)

        if   choice == 1:   coords = POSITION_UP
        elif choice == 2:   coords = POSITION_RIGHT
        elif choice == 3:   coords = POSITION_DOWN
        elif choice == 4:   coords = POSITION_LEFT

        __click((
                random.uniform(coords[0][0], coords[0][1]),
                random.uniform(coords[1][0], coords[1][1])),
            duration)

        shoot_invader(7.2, 27)

        for click in clicks_2:
            coords = click[0]
            duration = click[1]
            __click((
                random.uniform(coords[0][0], coords[0][1]),
                random.uniform(coords[1][0], coords[1][1])),
            duration)

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
#             __click((x, y), duration)

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
#             __click(*click)
#         press_backspace(16)
#         __write(
#             generate_random_string(random_inrange(8, 16)))
#         for click in clicks_2:
#             __click(*click)

if __name__ == "__main__":
    main()
