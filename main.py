import json
import threading
import time
import pyautogui
import keyboard

def get_positions_interactively() -> dict[str, list]:
    """
    Prompt the user to click on specific areas of the screen to set positions for each step.
    Make sure that you put the IDE or terminal back into focus before you press 'enter'.
    Returns a dictionary of the step names and positions.
    """
    positions = {}
    steps = ["Take Picture", "Send To", "Send To Box", "Select Person", "Send"]
    for step in steps:
        input(f"Hover over the '{step}' button and press ENTER to capture its position...")
        x, y = pyautogui.position()
        positions[step] = [x, y]
        print(f"Captured position for '{step}': {x}, {y}")
    return positions

def save_positions_to_file(positions: dict[str, list], file: str = "ButtonPosition.json") -> None:
    """Save the positions dictionary to a JSON file."""
    with open(file, "w") as pos_file:
        json.dump(positions, pos_file, indent=4)
    print(f"Positions saved to '{file}'.")

def load_positions_from_file(file: str = "ButtonPosition.json") -> dict[str, list]:
    """Load positions from a JSON file."""
    try:
        with open(file, "r") as pos_file:
            return json.load(pos_file)
    except FileNotFoundError:
        exit(f"The file named '{file}' was not found. Please set positions interactively first.")

def send_snaps(count: int, interval: float, delay: float, positions: dict[str, list], user: str) -> None:
    """Send snaps on Snapchat using mouse movements.

    :param count: The amount of snaps to send
    :param interval: Time between each snap
    :param delay: The delay between each step/action
    :param positions: Dictionary including the names and positions of each step
    :param user: The username of the recipient whom the snaps will be sent to
    """
    sec_to_complete: float = (count * (len(positions) * (delay * 2))) + (count - 1) * interval
    if "n" in input(f"Estimated time to complete: "
                    f"{int(sec_to_complete / 60)} minute{'s' if int(sec_to_complete / 60) > 1 else ''}"
                    f" {int(sec_to_complete % 60)} second{'s' if int(sec_to_complete % 60) > 1 else ''}\n"
                    f"Continue? [y/n]: ").lower():
        return
    for i in range(count):
        if i:
            print("Waiting for", interval, "sec.")
            time.sleep(interval)
        print(f"Snap #{i + 1}")

        for step, coords in positions.items():
            print(step)
            time.sleep(delay)

            pyautogui.click(x=coords[0], y=coords[1])
            time.sleep(delay)

            if step == "Send To Box":
                pyautogui.write(user)
            elif step == "Select Person":
                print("Selecting the person...")
    pyautogui.press("esc")


def exit_on_button_press(button: str = "esc"):
    while True:
        keyboard.wait(button)
        print("Exiting")
        return True

def main() -> None:
    if "n" not in input("Set positions interactively (recommended)? [y/n]:\n> "):
        step_positions = get_positions_interactively()
        save_positions_to_file(step_positions)
    else:
        step_positions = load_positions_from_file(file="ButtonPosition.json")

    count = input("Amount of snaps to send (default: 10): ")
    interval = input("Time between each snap (default: 1): ")
    delay = input("Delay between actions (default: 0.5): ")
    user: str = ""
    while not user:
        user = input(f"Recipient: ")

    main_process = threading.Thread(target=send_snaps,
                                    args=(int(count) if count else 10,
                                          float(interval) if interval else 1,
                                          float(delay) if delay else 0.5,
                                          step_positions,
                                          user),
                                    daemon=True)
    main_process.start()
    if exit_on_button_press():
        exit()

if __name__ == '__main__':
    main()