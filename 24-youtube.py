import pyautogui
import time

pyautogui.press("winleft")
time.sleep(2)
pyautogui.write("edge")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.moveTo(247, 90)
time.sleep(2)
pyautogui.click()
pyautogui.write("youtube one bit code")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.moveTo(329, 489)
time.sleep(2)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(1641, 640)
time.sleep(2)
pyautogui.click()
pyautogui.alert(
    text="Obrigado por se inscrever nesse canal", title="Agradecimento", button="OK"
)
