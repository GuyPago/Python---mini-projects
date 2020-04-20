import time
from PythonProject.GeneralProjects.Project_3_GuyHub import launch_hub
launch_hub()
def mat_hub():
    while True:
        user_input = input("Welcome to Guy's Math center\n\n's' --> Series" +
                           "q --> Back to hub")
        if (user_input == 'q'):
            print("Going back to hub..")
            time.sleep(2)
