import pywhatkit
import time
from selenium import webdriver


def read_contacts(filename):
    # Directly return the list comprehension
    return [line.strip() for line in open(filename, "r")]


def send_whatsapp_message(number, message):
    # pywhatkit.sendwhatmsg_instantly(number, message, tab_close=True)

    # Send a WhatsApp Message to a Contact at 1:30 PM
    # pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

    # Same as above but Closes the Tab in 2 Seconds after Sending the Message
    # pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

    # Send an Image to a Group with the Caption as Hello
    # pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

    # Send an Image to a Contact with the no Caption
    # pywhatkit.sendwhats_image(number, r"D:\Transit\EM.jpg")
    # Send an Image to a Contact with the Caption as Hello
    pywhatkit.sendwhats_image(number, r"D:\Transit\EM.jpg", message, tab_close=True)

    # Send a WhatsApp Message to a Group at 12:00 AM
    # pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

    # Send a WhatsApp Message to a Group instantly
    # pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

    # Play a Video on YouTube
    # pywhatkit.playonyt("PyWhatKit")


def main():
    contacts = read_contacts("contacts.txt")
    message = "Hello, This is an automated message testing the WhatsApp automation"
    for contact in contacts:
        send_whatsapp_message(contact, message)
        time.sleep(
            30
        )  # Corrected comment: wait for 30 seconds before sending the next message


if __name__ == "__main__":
    main()
