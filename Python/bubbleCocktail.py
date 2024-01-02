'''
Created on Mar. 3, 2022

@author: Tim Mah

Compares my implimentation of Bubble sort and the Bubble sort variation, cocktail shaker.
'''
import random
import time

def bubble_sort(list):
    isSorted = False;
    while not isSorted:
        isSorted = True;
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                isSorted = False;
                temp = list[i];
                list[i] = list[i+1];
                list[i+1] = temp;
    return list

def cocktail_shaker(list):
    isSorted = False;
    while not isSorted:
        isSorted = True;
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                isSorted = False;
                temp = list[i];
                list[i] = list[i+1];
                list[i+1] = temp;
        
        for c in range((len(list)-2), 1, -1):
                isSorted = True
                if list[c-1] > list[c]:
                    isSorted = False;
                    temp = list[c];
                    list[c] = list[c-1];
                    list[c-1] = temp;
    return list

def compareBubble():
    ten_thousand_nums = []
    for i in range(10000):
        ten_thousand_nums.append(random.randint(100000, 999999))
    ten_thousand_copy = ten_thousand_nums[:]
    
    starting_time_r = time.time()
    #bubble_sort(ten_thousand_nums)
    time_r = time.time() - starting_time_r
    
    starting_time_m = time.time()
    cocktail_shaker(ten_thousand_copy)
    time_m = time.time() - starting_time_m
    
    return [time_r, time_m]

def avgBubble(n):
    time_list = []
    for i in range(n):
        print("|", end='')
        time_list.insert(0, "")
        time_list[0] = compareBubble()
    total_r = 0
    total_m = 0
    print("\n")
    for t in time_list:
        print("[", end="")
        total_r += t[0]
        total_m += t[1]
    print("]\nDone.\n")
    print("Average time for bubble sort was", total_r/n, "seconds. The avg. time for cocktail sort was", total_m/n, "seconds.")
avgBubble(100)
