import pywhatkit
from utils import *
# Read the groups from the file
with open("groups.txt", "r") as file:
    groups = file.readlines()

# Send a WhatsApp Message to each group
for group in groups:
    group = group.strip()  # Remove any leading/trailing whitespace or newline characters
    pywhatkit.sendwhatmsg_to_group_instantly(group, "Hey All!")


# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")