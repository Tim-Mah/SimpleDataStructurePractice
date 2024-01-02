import random
import time

'''
@ param list_target: the list of elements to search for
@ param list_source: the list being searched
@return return a list of index locations of the target elements.
        -1 if it is not in the list.
'''
def linear_search(list_target, list_source):
    indexes = list()
    for element in range(len(list_target)):

        start_list_len = len(indexes)
        for i in range(len(list_source)):

            if(list_source[i] == list_target[element]):
                indexes.append(i)
                break

        # indicate element not found
        if len(indexes) == start_list_len:
            indexes.append(-1)

    return indexes


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
    #end while
        
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
            # end if/else
        #end while
        count *= 2
        l = part_sorted
        # end for
    return l
# end merge_sort

'''
@ param list_target: the list of elements to search for
@ param list_source: the list being searched
Sorts the source list, and returns a list of
the target indexes, -1 if it isn't in the source.
'''
def binary_search(list_target, list_source):
    list_source = merge_sort(list_source)
    indexes = list()
    
    for element in range(len(list_target)):

        min_index = 0
        max_index = len(list_source)-1
        middle_index = int((min_index + max_index)/2)
        start_list_len = len(indexes)
        
        while(max_index >= min_index):
        
            if(list_source[middle_index] == list_target[element]):
            
                indexes.append(middle_index)
                break
            
            elif(list_target[element] > list_source[middle_index]):
            
                min_index = middle_index + 1
                middle_index = int((min_index + max_index)/2)
                
            else: # element is less than
            
                max_index = middle_index - 1
                middle_index = int((min_index + max_index)/2)
            # end if/else
        # end while

        # element not in list
        if len(indexes) == start_list_len:
            indexes.append(-1)
        #end if
    # end for        
    return indexes
# end binary_search


'''Generates source list of random values,
    and target list of k values, 50% of which
    are in the source list
'''
def rand_lists(n, k):

    random.seed(12345)
    list_source = []
    list_target = []
    for b in range(n):
        list_source.append(int(random.randint(0, 2**31)))

    # Negative values wont be in the source list
    for i in range(round(k/2)):
        list_target.append(list_source[int(random.randint(0, n-1))])
    for i in range(k-len(list_target)):
        list_target.append(int(random.randint(-2**31, -1)))
        
    return [list_source, list_target]

'''Compares the 2 searches (based on avgerage time)
    @param n: how long the source list is
    @param k: how long the target list is
    @param sample: how many samples for the average
'''
def compare(n, k, sample):

    sum_time_linear = 0;
    sum_time_binary = 0;

    for i in range(sample):
        list_source = rand_lists(n, k)[0]
        list_target = rand_lists(n, k)[1]
        starting_time_linear = time.time()
        linear_search(list_target, list_source)
        sum_time_linear += time.time() - starting_time_linear
        
        starting_time_binary = time.time()
        binary_search(list_target, list_source)
        sum_time_binary += time.time() - starting_time_binary
        
    print("n = ",n ," avg. linear search time: ", sum_time_linear/sample, ". Avg. binary search time: ", sum_time_binary/sample)
compare(10000, 866, 1000)
