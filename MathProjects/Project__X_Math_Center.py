import time
import sys
sys.path.append('C:\\Users\guypa\github\guypago\PythonProject')
import GuyHub

def mat_hub():
    while True:
        user_input = input("Welcome to Guy's Math center !\n\n's' --> Series\n" +
                           "'q' --> Back to hub\n")
        if (user_input == 'q'):
            GuyHub.back_to_hub("Guy's Math Center")
        elif (user_input == "s"):
            pass





if __name__ == "__main__":
    mat_hub()
