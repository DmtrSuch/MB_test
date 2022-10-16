import random
import string
from collections import Counter


def counter_1(n_customers: int) -> Counter:
    sum_groups = []
    for n in range(0,n_customers):
        temp = ''.join(random.choice(string.digits) for i in range(random.randint(5,7)))
        if temp[0] == "0" :
            sum1 = sum([int(item) for item in temp])
            sum2 = 0
            for letter_itr in range(len(temp)):
                if letter_itr+1 == len(temp):
                    if int(temp[letter_itr]) >= int(temp[letter_itr-1]):
                        sum2+=int(temp[letter_itr])
                        break
                if int(temp[letter_itr]) <= int(temp[letter_itr+1]):
                    sum2+=int(temp[letter_itr])
                else: break
            if sum1 == sum2:
                sum_groups.append(sum2)
    return Counter(sum_groups)


def counter_2(n_customers: int, n_first_id: int) -> Counter:
    sum_groups = []
    for n in range(0,n_customers):
        if n == 0 and n_first_id > 9999 and n_first_id < 10000000:
            temp = str(n_first_id)
        else:
            temp = ''.join(random.choice(string.digits) for i in range(random.randint(5,7)))
        sum1 = sum([int(item) for item in temp])
        sum2 = 0
        for letter_itr in range(len(temp)):
            if letter_itr+1 == len(temp): 
                if int(temp[letter_itr]) >= int(temp[letter_itr-1]):
                    sum2+=int(temp[letter_itr])
                break
            if int(temp[letter_itr]) <= int(temp[letter_itr+1]): 
                sum2+=int(temp[letter_itr])
            else: break
        if sum1 == sum2:
            sum_groups.append(sum2)
    print(sum_groups)
    return Counter(sum_groups)
    
