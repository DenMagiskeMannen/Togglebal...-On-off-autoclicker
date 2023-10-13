# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:06:52 2023

@author: teodo
"""

import time
import pyautogui as pg
from pynput import keyboard
import threading
time.sleep(1)

#WHOOOOOO THREADING FUCKERS


autoclicker_on=False
autoclicker_key='p'

def change_state(variable):
    if variable== True:
        variable=False
        print("Changed to False",variable)
    elif variable== False:
        variable=True
        print("Changed to True",variable)
    else:
        print("change_state fucked it")
    return(variable)
liste=[]
min_time=0.5
last_click_time=time.time()
def on_press(key):
    global autoclicker_on
    global last_click_time
    current_click_time=time.time()
    #liste.append(key)
    #print(liste)
    if current_click_time-last_click_time >= min_time:
        if key == keyboard.KeyCode.from_char('p'):
            print("P")
            autoclicker_on=change_state(autoclicker_on)
    else:
        print("Not enought time elapsed")
    last_click_time=current_click_time
    
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        #print(dic["Inputs"])
        return False
        
    
def thready_boy():
    global autoclicker_on
    while True:
        if autoclicker_on == True:
            print("Clicked!")
            pg.click(button='right')
        time.sleep(0.2)
    
My_parralell_universe = threading.Thread(target=thready_boy, daemon=True)
My_parralell_universe.start()


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



