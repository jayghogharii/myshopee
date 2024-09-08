import time
import pyautogui
from selenium import webdriver

def move_cursor():
    a = 100
    b = 100
    for i in range(5):
    	pyautogui.moveTo(a, b, duration=1)
    	a += 100
    	b+= 100
    

def main():
   
    try:
        while True:
            move_cursor()
            time.sleep(5)
            move_cursor()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
