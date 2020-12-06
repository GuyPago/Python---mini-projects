''' Exercise #6. Computational Thinking and Programming.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def how_many_common_letters(s1, s2):
    count = 0
    for i in set(s1):
        if i in s2:
            count += 1
    return count


#########################################
# Question 2 - do not delete this comment
#########################################
def clean_word(word, chars_list):
    word = word.lower()
    for i in chars_list:
        if i in word:
            word = word.replace(i, '')
    return word


#########################################
# Question 3 - do not delete this comment
#########################################
def ciel_list_of_floats_in_place(floats_list):
    for i in range(len(floats_list)):
        if floats_list[i] % 1 != 0:
            floats_list[i] = floats_list[i] // 1 + 1
    return None


#########################################
# Question 4 - do not delete this comment
#########################################
def clean_words_of_sentence(sentence):
    wrong = ['#','$','!','?','%',',','.']
    sentence = sentence.lower()
    lst = sentence.split()
    for i in range(len(lst)):
        for j in wrong:
            if j in lst[i]:
                lst[i] = lst[i].replace(j,'')
    return lst



#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_pattern(p):
    if p.count(')') == p.count('('):
        while '()' in p:
            p = p.replace('()','')
        if p == '':
            return True
    return False
