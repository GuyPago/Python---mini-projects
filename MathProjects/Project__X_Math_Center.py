import time
import sys
sys.path.append('C:\\Users\guypa\github\guypago\PythonProject')
import GuyHub

def mat_hub():
    while True:
        user_input = input("Welcome to Guy's Math center !\n\n's' --> Series\n" +
                           "'q' --> Back to hub\n")
        if (user_input == 'q'):
            print("Going back to hub..")
            time.sleep(1)
            print("\n\n")
            GuyHub.launch_hub()
        elif (user_input == "s"):
            pass





if __name__ == "__main__":
    mat_hub()
