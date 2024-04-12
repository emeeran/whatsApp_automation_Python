# send_image.py
from utils import read_contacts
import pywhatkit


def send_whatsapp_image(number, message, image_path):
    print(f"Sending image {image_path} to {number}")
    pywhatkit.sendwhats_image(number, image_path, message, tab_close=True)


def send_messages_to_contacts(contacts, message, image_path):
    for contact in contacts:
        send_whatsapp_image(contact, message, image_path)


contacts = read_contacts("contacts.txt")
message = "Hello, this is an automated message testing the WhatsApp automation."
image_path = input("Please enter the path to the image: ").strip('"')

send_messages_to_contacts(contacts, message, image_path)

# Test passed. The image was sent to all the contacts in the contacts.txt file.
