# send_group_message.py

from utils import read_contacts
import pywhatkit


def send_group_message(group_id, message):
    pywhatkit.sendwhatmsg_to_group_instantly(group_id, message)
