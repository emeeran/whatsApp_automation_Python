import pywhatkit
import time
from selenium import webdriver

# Function to read contacts from a file
def read_contacts(filename):
    """
    Read contacts from a file and return them as a list.

    Args:
        filename (str): The path to the file containing contacts.

    Returns:
        list: A list of contacts read from the file.

    Raises:
        FileNotFoundError: If the specified file is not found.
    """

def read_contacts(filename):
    with open(filename, 'r') as file:
        contacts = [line.strip() for line in file]
    return contacts

# Function to send WhatsApp message
def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(number, message, tab_close=True)

# Main function
def main():
    contacts = read_contacts('contacts.txt')
    message = "Hello, This is an automated message"
    for contact in contacts:
        send_whatsapp_message(contact, message)
        time.sleep(30)  # wait for 10 seconds before sending the next message

if __name__ == "__main__":
    main()