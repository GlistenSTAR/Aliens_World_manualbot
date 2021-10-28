import ait
from ocr import OCRHandler
from event import event
from datetime import datetime
import pyautogui
import time
# from config import game_url
def game(driver):
    OCR = OCRHandler()
    start_time = datetime.now().minute
    later_time = start_time
    trigger = False
    Approve_window = True
    capture_pos =   [[(403,495),(87,30),(433,500)],     # Login
                    [(130,190),(175,35),(300,550)],     # Approve
                    [(700,271),(75,30),(725,283)],      # MINE 
                    [(415,575),(70,20),(438,583)],      # Mine (cycle start)
                    [(400,562),(98,40),(438,583)],      # Claim (cycle start)
                    [(270,500),(80,30),(300,510)],      # Approve Account
                    [(320,370),(70,30),(370,450)],      # Claim
                    [(150,190),(175,35),(300,600)],     # Approve 
                    [(180,535),(80,25),(250,550)],      # Mining Hub (cycle end)
                    [(410,273),(67,38),(669,259)]]      # Error
    capture_name = ["Login","Transaction","VE","PY","Claim","Approved","Ialeke","Transaction","Mining","€rror"]
    while True:
        iterater = 0
        for pos in capture_pos:
            capture_word = event(OCR, pos[0], pos[1])
            print(capture_word+"---"+capture_name[iterater]) # output
            # time.sleep(1)
            if capture_word.find(capture_name[iterater]) >= 0:
                if capture_name[iterater] == "Change":
                    trigger = True   
                    start_time = datetime.now().minute                    
                else:
                    trigger = False
                if capture_name[iterater] == "Outdated,":
                    ait.press("F5")
                else:  
                    ait.move(pos[2][0], pos[2][1])
                    ait.click()
                    print("----------------------------clicked---------------------")
                    time.sleep(30000)
                    if Approve_window == True and capture_name[iterater] in ["Land"]:
                        time.sleep(5)
                        pyautogui.hotkey("ctrl","-")
                        Approve_window = False
                if capture_name[iterater] == "Mining":
                    print("************* TLM was mined successfully ****************")
            iterater = iterater + 1
        later_time = datetime.now().minute
        if trigger == True and later_time > start_time + 5:
            start_time = later_time
            trigger = False
            print("window was refreshed")
            ait.press("F5")
        print(datetime.now().strftime ("%Y-%m-%d %H:%M:%S"))


