#!/usr/bin/python3
def isWinner(x, nums):
    if x != len(nums):
        return None
    
    Ben = 0
    Maria = 0
    
    for n in range(x):
        num = nums[n]
        
        #check for number of prime numbers and append to array
        for i in range(0,num):
            prime = []
            if i == 1:
                continue
            flag = 0
            
            for j in range(2, i // 2 + 1):
                if (i % j == 0):
                    flag = 0
                    break
            
                if (flag == 1):
                    prime.append(i)
        
        #How many prime numbers
        primes = len(prime)
            
        #round winner time
        if primes % 2 == 0:
            Ben += 1
        else:
            Maria +=1
    
    #who's the final winner
    if Ben < Maria:
        winner = "Maria" 
    elif Ben > Maria:
        winner = "Ben"
    else:
        winner = None
    
    return winner
