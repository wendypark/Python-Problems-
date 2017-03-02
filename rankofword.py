from itertools import permutations
from itertools import chain

def find_rank(word):
    x = sorted([''.join(p) for p in permutations(word)])
    temp = []
    for iterate in x:
        if iterate not in temp:
            temp.append(iterate)
    for i in range(0, len(temp)):
        if temp[i] == word:
            return(i+1)
            break
            
            perms = [''.join(p) for p in permutations('stack')]

if __name__ == '__main__':

    testcases = []
    num_cases = int(input())
    for _ in range(num_cases): 
        testcases.append(input().split())
    print(testcases)
    testcases = list(chain.from_iterable(testcases))
    print(testcases)
    if 1 <= num_cases <= 10:
        for word in testcases:
            if 1 <= len(word) <= 100:
                print(find_rank(word))
            else:
                exit(0)
    else:
        exit(0)
        