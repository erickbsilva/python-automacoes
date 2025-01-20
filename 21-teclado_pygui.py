import pyautogui
import time

pyautogui.press("winleft")
time.sleep(2)
pyautogui.write("calculadora")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("ctrl", "shift", "esc")
time.sleep(2)
# with pyautogui.hold('alt'):
#     pyautogui.press(['f4'])
# time.sleep(2)
# with pyautogui.hold('alt'):
#     pyautogui.press(['f4'])
# time.sleep(2)
with pyautogui.hold("winleft"):
    pyautogui.press(["left"])
time.sleep(2)
pyautogui.click()
time.sleep(2)
with pyautogui.hold("winleft"):
    pyautogui.press(["right"])
