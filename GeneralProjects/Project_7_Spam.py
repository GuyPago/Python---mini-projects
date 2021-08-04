# """Guy's Spam conversion algorithm.

import pyautogui as ag
import time
import pyperclip

time.sleep(5)
times = 10
for i in range(times):
    with open('data/spam.txt', 'r') as f:
        for line in f:
            ag.typewrite(line)
            # ag.press('enter')
        if times > 1:
            pass
            # ag.typewrite(f'Repeating {times-1} more times...\n')
        times -= 1
ag.typewrite('B------')
ag.press('enter')

