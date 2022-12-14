#
#   pyslave.py
#   By: <pducos@student.42.fr>
#
# DESCRIPTION
#     This program uses the pyautogui library to automate interactions with a GUI. With just a few lines of code, you
#     can automate virtually any interaction, from clicking buttons and typing text to moving the cursor and simulating
#     mouse clicks. This uses the pyautogui library to provide smooth, natural movements, and with built-in
#     features like random jitter and variable speed, interactions look just like those performed by a real
#     person. Save time, increase productivity, and never perform another tedious manual task again.
#
#! python3

from os import system
import pyautogui
import time
import random
import string

system("clear")
print ("""
__________         _________.__
\\______   \\___.__./   _____/|  | _____ ___  __ ____
 |     ___<   |  |\\_____  \\ |  | \__  \\  \\/ // __ \\
 |    |    \\___  |/        \\|  |__/ __ \\   /\\  ___/
 |____|    / ____/_______  /|____(____  /\_/  \___  >
           \/            \/           \/          \/ v1.0
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
        print("Going to sleep for {} seconds".format(sleep_time))
        time.sleep(sleep_time)


def human_type(string, chunk_length=7, typing_speed_range=(0.05, 0.1)):
    chunks = [string[i:i+chunk_length]
        for i in range(0, len(string), chunk_length)]
    for chunk in chunks:
        pyautogui.typewrite(
            chunk,
            interval=random.uniform(*typing_speed_range))
    pyautogui.press('enter')


def human_click():
    # Move the cursor slightly in a random direction before clicking
    x, y = pyautogui.position()
    x += random.uniform(-2.5, 2.5)
    y += random.uniform(-2.5, 2.5)
    pyautogui.moveTo(x, y)

    # Add jitter and tremor to the cursor movement
    for i in range(3):
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)
        pyautogui.moveRel(dx, dy, duration=0.01)

    # Add a small delay before clicking
    time.sleep(random.uniform(0.1, 0.3))

    # Apply random variations to the clicking
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
            pyautogui.easeInOutElastic,
            pyautogui.easeInOutSine]
    speed = random.uniform(0.75, 1.25)
    pyautogui.moveTo(
        coordinates,
        duration=(duration * speed),
        tween=random.choice(easing_functions))
        
    for i in range(random.randint(0, 3)):
        pyautogui.moveRel(
            random.uniform(-7, 7),
            random.uniform(-7, 7),
            duration=random.uniform(0, 0.1))
    pyautogui.moveTo(
        coordinates,
        duration=duration / 4,
        tween=random.choice(easing_functions))


def click_spot(coordinates, duration=1):
    # Move the cursor to the specified coordinates.
    move_cursor(coordinates, duration)
    # Perform a realistic mouse click.
    human_click()


def generate_random_string(size):
    return ''.join(
        random.choices(
            string.ascii_lowercase,
            k=size))


def press_backspace(num_times):
    for i in range(num_times):
        pyautogui.press("backspace")

######################################################################

def parse_click_path(config_file):
    clicks = []
    
    with open(config_file, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) != 6:
                raise ValueError('Invalid config file format')
            try:
                x = (int(parts[0]), int(parts[1]))
                y = (int(parts[2]), int(parts[3]))
                duration = float(parts[4])
                wait = float(parts[5])
            except ValueError:
                raise ValueError('Invalid config file format')
            click = ((x, y), (duration, wait))
            clicks.append(click)
            
    return clicks

######################################################################

# INVADERS
def shoot_invader(duration, count):
    bonus = 0
    print ("Thank you next")
    for i in range(count):
        print (f"  - ({bonus}%) Normal attack...", end="\r")
        click_spot((327, 682), 0.4)
        bonus += 15
        time.sleep(duration)
    print (f"\n  ! Enhanced attack...")
    click_spot((519, 680), 0.4)

def main():
    time.sleep(1)
    count = 0
    clicks_1 = parse_click_path('tasks/00_invaders.conf')
    clicks_2 = parse_click_path('tasks/01_invaders.conf')

    while True:
        choice = 0
        count += 1
        print (f"[loop: '{count}']", end ="\r")
        for i, click in enumerate(clicks_1):
            coords = click[0]
            duration = click[1][0]
            wait = click[1][1]
            if click == (((317,  356), (548,  579)), (0.5, 0.3)):

                choice = random.randint(1, 4)

                if   choice == 1:   coords = POSITION_DOWN
                elif choice == 2:   coords = POSITION_LEFT
                elif choice == 3:   coords = POSITION_UP
                elif choice == 4:   coords = POSITION_RIGHT

            click_spot((
                    random.uniform(coords[0][0], coords[0][1]),
                    random.uniform(coords[1][0], coords[1][1])),
                duration)
            time.sleep(wait)

        if   choice == 1:   coords = POSITION_UP
        elif choice == 2:   coords = POSITION_RIGHT
        elif choice == 3:   coords = POSITION_DOWN
        elif choice == 4:   coords = POSITION_LEFT

        click_spot((
                random.uniform(coords[0][0], coords[0][1]),
                random.uniform(coords[1][0], coords[1][1])),
            duration)

        shoot_invader(7.2, 1)

        for i, click in enumerate(clicks_2):
            coords = click[0]
            duration = click[1][0]
            wait = click[1][1]
            click_spot((
                    random.uniform(coords[0][0], coords[0][1]),
                    random.uniform(coords[1][0], coords[1][1])),
                duration)
            time.sleep(wait)

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

if __name__ == "__main__":
    main()
