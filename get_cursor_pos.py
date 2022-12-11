import pyautogui

while True:
    # Get the current coordinates of the cursor
    x, y = pyautogui.position()

    # Print the coordinates on the screen
    print(f"Cursor position: ({x}, {y})", end="\r")