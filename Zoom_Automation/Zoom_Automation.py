import os
import pyautogui
from time import sleep
import pandas as pd
from datetime import datetime
import imaplib
import email

host = 'imap.gmail.com'
username = 'ishanmitra020@gmail.com'
password = 'brvvuzqmalzxpspx'


def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date', 'body']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
        link = my_message['Subject']
    return my_message


def sign_in(meet_id, password):
    os.startfile('C:\\Users\\sanja\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    sleep(10)
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    sleep(3)
    meeting_id_type = pyautogui.locateCenterOnScreen("C:\\1. Ishan's Files\\Coding Files\\Python\\Zoom_Automation\\meeting_id_box.png")
    #pyautogui.moveTo(join_btn)
    #pyautogui.click()
    pyautogui.write(meet_id)

    meet_btn_press = pyautogui.locateCenterOnScreen("C:\\1. Ishan's Files\\Coding Files\\Python\\Zoom_Automation\\meet_btn.png")
    pyautogui.moveTo(meet_btn_press)
    pyautogui.click()
    sleep(10)

    meeting_pass_type = pyautogui.locateCenterOnScreen("C:\\1. Ishan's Files\\Coding Files\\Python\\Zoom_Automation\\meeting_pass_box.png")
    #pyautogui.moveTo(join_btn)
    #pyautogui.click()
    pyautogui.write(password)

    joinmeetbtn = pyautogui.locateCenterOnScreen("C:\\1. Ishan's Files\\Coding Files\\Python\\Zoom_Automation\\join_meet_btn.png")
    pyautogui.moveTo(joinmeetbtn)
    pyautogui.click()

if __name__ == "__main__":
    my_inbox = get_inbox()
    if 'https://us05web.zoom.us/j/' in link:
        name = link
        name.replace['https://us05web.zoom.us/j/', '']
        name.replace['?pwd=', '']
    sign_in('2320140633', '16MOwm')
