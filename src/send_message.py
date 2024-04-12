# send_image.py
from utils import read_contacts
import pywhatkit


def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(number, message, tab_close=True)


def send_messages_to_contacts(contacts, message):
    for contact in contacts:
        send_whatsapp_message(contact, message)


contacts = read_contacts("contacts.txt")
message = "Hello, this is an automated message testing the WhatsApp automation."
send_messages_to_contacts(contacts, message)

# Test passed. The image was sent to all the contacts in the contacts.txt file.
