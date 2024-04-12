# send_scheduled_message.py
from utils import read_contacts
import pywhatkit
from datetime import datetime, timedelta

def send_whatsapp_message(number, message, hour, minute):
    pywhatkit.sendwhatmsg(number, message, hour, minute, 15, True, 2)

def send_messages_to_contacts(contacts, message):
    start_hour = int(input("Enter the starting hour (24-hour format): "))
    start_minute = int(input("Enter the starting minute: "))
    current_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    for contact in contacts:
        send_whatsapp_message(contact, message, current_time.hour, current_time.minute)
        current_time += timedelta(minutes=1)

contacts = read_contacts("contacts.txt")
message = "Hello, this is an automated scheduled message testing the WhatsApp automation."
send_messages_to_contacts(contacts, message)
