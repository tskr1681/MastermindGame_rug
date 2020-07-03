def solution(S):
    # write your code in Python 3.6
    no_a = S.count('a')
    if no_a < 3 or no_a%3 != 0:
        return 0
    
    no_a_in_each = no_a / 3
    
    i, j, k, l = 0, 0, 0, 0
    
    for s in S:
        curr_count = 0
        if s == "a":
            curr_count += 1
            
        if curr_count == 
    
