import time
import sys
sys.path.append('C:\\Users\guypa\github\guypago\PythonProject\GeneralProjects')
from Project_3_GuyHub import launch_hub

def mat_hub():
    while True:
        user_input = input("Welcome to Guy's Math center\n\n's' --> Series" +
                           "q --> Back to hub")
        if (user_input == 'q'):
            print("Going back to hub..")
            time.sleep(2)
            launch_hub()
