import itertools
def reorder(N):
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
            for cand in itertools.permutations(str(N)))
print(reorder(1))   #True
print(reorder(22))  #False
print(reorder(16))  #True
