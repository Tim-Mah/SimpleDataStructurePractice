'''This compares my implementations of radix sort and merge sort. Iterative approach.
   
   CISC-121 2022W
   
   Name:   Timothy Mah
   Section: 001
   Student Number: 20267967
   Email:  20tvm@queensu.ca
   

   I confirm that this assignment solution is my own work and conforms
   to Queen's standards of Academic Integrity
'''
import random
import time

def radix_sort(l):
    '''Radix sort list l, returns sorted list'''
    next_dig = True
    num_dig = 1
    dig = 1/10
    while  next_dig:
        dig = int(dig * 10.0)
        next_dig = False
        # Negative and positive digit slots
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(l)):
            # append l[i] at position of digit this loop is on

            bucket[(l[i]//dig)%10].append(l[i])
            if(len(str(l[i]))) > num_dig:
                # only trigger if statement once
                if not next_dig:
                    num_dig += 1
                next_dig = True
        l = []
        for i in range(len(bucket)):
            for b in range(len(bucket[i])):
                l.append(bucket[i][b])
    return l

def merge(l1, l2):
    '''Merge two sorted lists, l1 and l2. Returns merged list merge'''
    merged = []
    for i in range(len(l1)+len(l2)):
        if len(l1) >0 and len(l2) >0:
            #compare first elements and second elements, smallest first
            if l1[0] <= l2[0]:
                merged.append(l1[0])
                l1 = l1[1:]
            else:
                merged.append(l2[0])
                l2 = l2[1:]
                    
        elif len(l1) == 0 and len(l2) >0:
            for b in range(len(l2)):
                merged.append(l2[0])
                l2 = l2[1:]
        elif len(l1) >0 and len(l2) == 0:
            for b in range(len(l1)):
                merged.append(l1[0])
                l1 = l1[1:]
    return merged

def merge_sort(l):
    '''Merge sort list l or positive integers, returns sorted list'''
    #Sections lists into 2, then 4, etc. then merges those lists
    if len(l) <= 1:
        return l
    ex_num = 1
    count = 1
    while count < len(l):
        count *= 2
        ex_num += 1
    count = 1
    for i in range(ex_num):
        # Section off parts of array (count long), then merge them
        part_sorted =[]
        section = 0
        # Goes until all sections are accounted for
        while len(l)-section >0:
            # If there is an unmerged part in l that has a number of elements less than section
            if len(l)-(section+count) > count and len(l)-section < 2*count:
                part_sorted.extend(merge(l[section:(section+count)], l[(section+count):]))
            # If unmerged is equal to sort, then it is sorted and can't be merged, so add it to the new list
            elif len(l)-section == count:
                part_sorted.extend(l[section:])
            else:
                part_sorted.extend(merge(l[section:(section+count)], l[(section+count):(section+2*count)]))
            section += 2*count
        count *= 2
        l = part_sorted
        # end for
    return l

def rand_lists():
    '''Generates 100 lists of 100 positive numbers'''
    lists_100 = []
    for i in range(100):
        hundred_nums = []
        for b in range(100):
            hundred_nums.append(int(random.randint(0, 2**32)))
        lists_100.insert(0, "")
        lists_100[0] = hundred_nums
    return lists_100

# Prints sorted 100 lists
li = rand_lists()
for i in li:
    print("Radix followed by Merge")
    print(radix_sort(i))
    print(merge_sort(i), "\n")

def compare():
    '''Returns sort time for radix and merge, list of times, 
    if radix wins, return 1 also.
    '''
    ten_thousand_nums = []
    for i in range(10000):
        ten_thousand_nums.append(random.randint(100000, 999999))
    ten_thousand_copy = ten_thousand_nums[:]
    
    starting_time_r = time.time()
    radix_sort(ten_thousand_nums)
    time_r = time.time() - starting_time_r
    
    starting_time_m = time.time()
    merge_sort(ten_thousand_copy)
    time_m = time.time() - starting_time_m
    
    radix_win = 0
    if time_r < time_m:
        radix_win =1
    
    return [time_r, time_m, radix_win]

def avg_time(n):
    '''Calculates and prints the average sort time of radix and merge'''
    time_list = []
    for i in range(n):
        # Pseudo loading bar
        print("|", end = "")
        time_list.insert(0, "")
        time_list[0] = compare()
    total_r = 0
    total_m = 0
    total_w = 0
    for t in time_list:
        total_r += t[0]
        total_m += t[1]
        total_w += t[2]
    print("\nAverage time for radix sort was", total_r/n,\
          "seconds. The avg. time for merge sort was", total_m/n,\
           "seconds. Radix won about", str(total_w//n *100)\
           + "% of the time.")

avg_time(1000)
        
