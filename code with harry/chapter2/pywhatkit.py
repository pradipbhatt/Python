import pyautogui
import time

# Define the Hindi song lyrics
lyrics = """
hello
"""

# Allow some time to switch to the desired message box (like WhatsApp, Instagram, etc.)
time.sleep(3)  # You can adjust the time based on how long it takes to focus on the message box

# Function to type out a paragraph and wait for reply before continuing
def send_lyrics():
    # Loop through the lyrics and type one paragraph at a time
    for line in lyrics.split("\n"):
        if line.strip():  # Skip empty lines
            for char in line:
                pyautogui.typewrite(char)  # Type each character
                time.sleep(0.1)  # Small delay between characters for realism
            pyautogui.press('enter')  # Press Enter to go to the next line
            time.sleep(0.5)  # Slight pause between lines

            # Wait for the reply before sending the next line (simulate checking for a reply)
            print("Waiting for reply...")  # You can replace this with any logic to confirm a reply
            time.sleep(10)  # Adjust this time to the expected time to get a reply (e.g., 10 seconds)

# Call the function to start sending the lyrics
send_lyrics()
