import pywhatkit
from selenium import webdriver
import time

def read_groups(filename):
    return [line.strip() for line in open(filename, "r")]

def send_whatsapp_message(group, image_path, message):
    pywhatkit.sendwhats_image(f"+country_code{group}", image_path, message)

def main():
    groups = read_groups("groups.txt")
    image_path = input("Enter the image path: ").strip('"')

    driver = webdriver.Chrome()  # Ensure you have the Chrome WebDriver installed and in PATH
    driver.get("https://web.whatsapp.com")

    for group in groups:
        send_whatsapp_message(group, image_path, "Hello, this is an automated message testing the WhatsApp automation.")
        time.sleep(5)  # Wait for 5 seconds before closing the tab
        driver.close()

if __name__ == "__main__":
    main()
