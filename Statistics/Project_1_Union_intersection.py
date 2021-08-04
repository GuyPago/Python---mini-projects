# Union

A = {1,2,3}
B = {2,3,4,5}

union_1 = A.union(B)
union_2 = A | B

intersection_1 = A.intersection(B)
intersection_2 = A & B

difference_1 = B.difference(A)
difference_2 = B - A

sym_diff_1 = B.symmetric_difference(A)
sym_diff_2 = B ^ A

print(union_1 == union_2, union_1)
print(intersection_1 == intersection_2, intersection_1)
print(difference_1 == difference_2, difference_1)
print(sym_diff_1 == sym_diff_2, sym_diff_1)
B - A
