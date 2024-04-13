# utils.py
import os

def read_contacts(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]
