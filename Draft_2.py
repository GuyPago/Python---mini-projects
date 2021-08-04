import random
import string
dates = [str(i).zfill(2) + '.07.2021' for i in range(1, 31)]
'12.05.2021'


credit_card = '4580' + ''.join(random.choices(string.digits, k=16))
print(credit_card)
