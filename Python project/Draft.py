import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-math.pi/2, 11*math.pi + math.pi/2, 0.001)
y = np.sin(x)
z = x + y

plt.plot(x, y)
plt.show()

ages = [25,32,16,56]
type(ages)

ages[-1]
newAges = ages + [12,42,11]
newAges
ages.append(120)
ages

my_friend = "Sammy"
my_friend
if my_friend == "Bob":
    print("Sup dude ?")
elif my_friend == "Sammy":
    print("Yo sammy")
else:
    print("I dont know you. get lost")


foods = ["pizza","falafel","hamburger","bamba","water"]
foods


for i in foods[:]:
    print(i)


my_com = "PC"

for i in range(5,100,2):
    print(i)
