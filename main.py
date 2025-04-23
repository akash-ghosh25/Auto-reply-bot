import pyautogui
import pyperclip
import time
from openai import OpenAI
from google import genai
import re


client = genai.Client(api_key="Your_gemini_Api")

# Function to click on the icon
def click_icon():
    pyautogui.click(930, 1170)
    time.sleep(1)  # Wait a second for the action to register

# Function to select the text and copy to clipboard
def select_and_copy():
    time.sleep(2)
    # Move to the starting position and click
    pyautogui.moveTo(713, 222)
    pyautogui.mouseDown()  # Start dragging

    # Drag to the end position
    pyautogui.moveTo(1811, 1020, duration=1)  # Add duration for smooth drag
    pyautogui.mouseUp()  # Release the mouse button

    # Copy the selected text (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1848,877)
    time.sleep(1)  # Wait for clipboard operation

    # Get the copied text from the clipboard
    copied_text = pyperclip.paste()
    return copied_text

# Function to paste the copied text and press Enter
def paste_and_press_enter():
    # Click on the target position (1017, 1072)
    pyautogui.click(1017, 1072)
    time.sleep(1)  # Wait a second for the click to register

    # Paste the copied text (Ctrl+V)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Wait for paste operation

    # Press Enter
    pyautogui.press('enter')


def is_last_message_from_me(chat_log, my_name="Akash Ghosh"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if my_name in messages:
        return True 
    return False

def remove_timestamp_and_username(input_string):
    # Regular expression to match the pattern of [time, date] username:
    pattern = r"^\[\d{1,2}:\d{2} [apm]+, \d{1,2}/\d{1,2}/\d{4}\] [A-Za-z\s]+: "
    
    # Replace the matching pattern with an empty string
    result = re.sub(pattern, "", input_string)
    return result


# def is_last_message_from_me(chat_log, my_name="Akash Ghosh"):
#     # Split the chat log based on the timestamp format
#     messages = re.split(r'\[\d{1,2}:\d{2} (AM|PM), \d{1,2}/\d{1,2}/\d{4}\] ', chat_log)
    
#     # Remove empty entries from the split
#     messages = [msg for msg in messages if msg.strip()]
    
#     # Get the last message and check if it is from the specified sender
#     last_message = messages[-1]
#     if my_name in last_message:
#         return False
#     return True


click_icon()
while True:
    # Main script execution
    copied_text = select_and_copy()
    # print(copied_text)
    
    # Check if the last message is from sender or not
    # print(is_last_message_from_me(copied_text))
    if not is_last_message_from_me(copied_text):

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="You are Akash, a friendly and approachable coder from India who is fluent in Bengali, Hindi, and English. You analyze each chat and respond naturally, just like a human would—casually and thoughtfully. When interacting, you switch between Bengali, Hindi, and English based on the context and user preferences. You use English primarily for coding-related topics, but feel free to incorporate Hindi or Bengali when discussing cultural topics or when the conversation naturally flows in those languages. Your responses are always warm, curious, and friendly, making the user feel comfortable and understood. This message recived now: " + copied_text,
        )

        print(response.text)
        # response = remove_timestamp_and_username(response.text)
        pyperclip.copy(response.text)
        paste_and_press_enter()
        
        # print(response)
