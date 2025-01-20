import pyautogui
from time import sleep
from pyautogui import mouseInfo

# mouseInfo()

with open("files/alunos.txt", "r", encoding="utf-8") as file:
    for line in file:
        aluno = line.split(",")[0]
        email = line.split(",")[1]
        pyautogui.click(1548, 1002, duration=1)
        pyautogui.write(aluno)
        pyautogui.click(1551, 1054, duration=1)
        pyautogui.write(email)
        pyautogui.click(1551, 1090, duration=0.5)
        pyautogui.screenshot(f"files/{aluno}.png")
        sleep(1)

# 1267, 718
# 1267, 775
