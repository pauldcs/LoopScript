import pyautogui
import time
import random

def click(coordinates,
          min_duration=0.3,
          max_duration=0.5,
          min_delay=0.1,
          max_delay=0.3):

    print(f"Moving...")

    pyautogui.moveTo(
        coordinates,
        duration=random.uniform(min_duration, max_duration),
        tween=pyautogui.easeOutQuad)

    print(f"  └── Arrived: {coordinates}")

    position = (
        round(coordinates[0] + random.uniform(-3.5, 3.5), 3),
        round(coordinates[1] + random.uniform(-3.5, 3.5), 3))

    time.sleep(random.uniform(min_delay, max_delay))
    pyautogui.click(position)
    print(f"  └── Clicked: {position}\n")

def clicker():
    while True:
        a_x = round (random.uniform(498, 560), 3)
        a_y = round (random.uniform(693, 704), 3)
        b_x = round (random.uniform(540, 605), 3)
        b_y = round (random.uniform(735, 744), 3)

        click((a_x, a_y),
            0.1, 0.3,
            0.1, 0.17)
        
        click((b_x, b_y),
            0.1, 0.3,
            0.1, 0.17)

def main():
    clicker()

if __name__ == "__main__":
    main()