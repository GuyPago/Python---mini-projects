import string




with open('Python\GeneralProjects\data\dict.txt', 'r') as f:
    text = f.read()

def count(text,L):
    count = 0
    for i in text:
        if i == L:
            count += 1
    return count

count(text,'0')


print(string.ascii_lowercase)
