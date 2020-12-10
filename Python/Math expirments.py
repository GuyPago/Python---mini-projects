def is_pangram(x):
    abc = {}
    for i in x.replace(' ', ''):
        abc[i.lower()] = abc.get(i.lower(), True)

    print(abc)
    print(len(abc))

    return len(abc) == 26


def best_judge(lst):
    j2s = {}
    for tup in lst:
        j2s[tup[1]] = j2s.get(tup[1], 0) + 1
    return max(j2s, key=j2s.get)


print(best_judge([('avi', 'geffen'), ('benny', 'shlomi'), ('david', 'shlomi')]))

print(is_pangram("The quick brown fox jumps over the lazy dog"))
