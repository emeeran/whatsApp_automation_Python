# utils.py
import os

def read_contacts(filename):
    filepath = os.path.join("..", filename)
    with open(filepath, "r") as file:
        contacts = [line.strip() for line in file]
    return contacts
