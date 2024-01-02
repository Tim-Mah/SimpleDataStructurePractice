import re
import string
import random
from nltk.corpus import stopwords

'''
@auther Tim Mah
Date: 2022
Generates a hash that stores the word and its frequency from a text file.
'''
stopWords = set(stopwords.words('english'))

'''
    Node that stores a key, value, and points to the next node
'''
class HashNode:
  '''
    @param key: the word stored
    @param value: the word frequency

    Initializes and creates a new Node
  '''

  def __init__(self, key, value):
    self.key = key
    self.value = value

'''
    Creates a Hash table
'''
class HashTable:

  '''
    @param capacity: number of buckets hash table has
    
    Tnitializes a hash table with specified buckets
  '''
  def __init__(self, capacity):
    ## Fized size of the hash
    self.capacity = capacity
    self.bucket = [None] * capacity
  '''
      Prints each word and it's requency
  '''
  def printString(self):
    totalValues = 0
    for i in self.bucket:
      if (i != None):
        print(str(i.key), str(i.value) + " ")
        totalValues += i.value
      else:
        print("None")
    print("\n", "Wordcount", totalValues, "\n")

  '''
    @param key: the key to be hashed

    Generates a hash based on each letter of the key

    @return: The newly generated hash
  '''
  def hashFunction(self, key):
    hash = 0
    ##Sum of all (char * index+1)
    for i in range(len(key)):
      hash += ord(key[i]) * (i + 1)
    hash = hash % self.capacity
    return hash

  '''
    @param key: word to insert into hash table

    Inserts key into hash table. If it exists, it adds
    one to the associtated frequency. If it is full, it
    prints a statement.
  '''
  def insert(self, key):
    targetIndex = self.hashFunction(key)
    ## Empty HashNode is being used as a deletion flag
    if self.bucket[targetIndex] == None or self.bucket[
        targetIndex] == HashNode(None, None):
      ## If key isn't in, add new node with key and               frequency of 1
      self.bucket[targetIndex] = HashNode(key, 1)
    elif self.bucket[targetIndex].key == key:
      ## If the key is already in, increment the value
      self.bucket[targetIndex].value += 1
    else:
      ## There's a collision
      origTarIdx = targetIndex
      ## Look to next index, keep going until wrap around to original generated index
      while (self.bucket[targetIndex] != None
             and self.bucket[targetIndex] != HashNode(None, None)):

        targetIndex += 1
        targetIndex = targetIndex % self.capacity

        ## Check if the rehash is the key we inster
        if (self.bucket[targetIndex] != None
            and self.bucket[targetIndex].key == key):
          self.bucket[targetIndex].value += 1
          origTarIdx = -2
          break

        ## If we've wrapped around, array is full
        if (targetIndex == origTarIdx):
          origTarIdx = -1
          break

      if (origTarIdx == -1):
        ## Array is full
        print("Hash Table Full, Insert Failed")
      elif (origTarIdx == -2):
        ## We've already incremented frequency for the key
        return
      else:
        ## Insert new key and value
        self.bucket[targetIndex] = HashNode(key, 1)

  '''
    @param key: The word to lookup in the hash table

    Searches for the key in the hashtable and calculates
    the number of search steps
    
    @return: the word frequency, and the number of search steps. 
    If key doesn't exist, returns -1 for frequency
  '''
  def search(self, key):
    steps = 1
    targetIndex = self.hashFunction(key)
    if (self.bucket[targetIndex] == None):
      return (-1, steps)
    elif (self.bucket[targetIndex] != None
          and self.bucket[targetIndex].key == key):
      return (self.bucket[targetIndex].value, steps)
    else:
      origTarIdx = targetIndex
      while (self.bucket[targetIndex].key != key):
        steps += 1
        targetIndex += 1
        targetIndex = targetIndex % self.capacity
        ## If it is None, it's empty and isn't deleted as well
        if (self.bucket[targetIndex] == None or targetIndex == origTarIdx):
          origTarIdx = -1
          break
      if (origTarIdx != -1):
        return (self.bucket[targetIndex].value, steps)
      else:
        return (-1, steps)
  '''
      @param key: The word to delete from the table

      Deletes the given key from the hast table and
      returns it's frequency
      
      @return: the deleted word frequency
  '''
  def delete(self, key):
    targetIndex = self.hashFunction(key)

    if (self.bucket[targetIndex].key == key):
      val = self.bucket[targetIndex].value
      self.bucket[targetIndex] = HashNode(None, None)
      return val

    else:
      origTarIdx = targetIndex
      while (self.bucket[targetIndex].key != key):
        targetIndex += 1
        targetIndex = targetIndex % self.capacity
        if (targetIndex == origTarIdx):
          origTarIdx = -1
          break
      if (origTarIdx != -1):
        val = self.bucket[targetIndex].value
        self.bucket[targetIndex] = HashNode(None, None)
        return val
      else:
        print("Key not in table, couldn't be deleted")
        return None
    '''
  @param file: the text file to parse
  Parses the textfile and removes puncuation
  and insignificant words
  '''

  def parseFile(self, file):
    with open(file, 'r') as input:
      content = input.readlines()
    preprocessed = []
    for line in content:
      line = line.strip().lower()
      #remove punctuation
      line = line.translate(str.maketrans('', '', string.punctuation))
      #remove stop words that care no specific meaning
      line = self.removeStopwords(line)  #remove numbers
      line = re.sub('\d+', '', line)  #remove extra white space
      line = re.sub(' +', ' ', line)
      if line:
        preprocessed.extend(line.split(" "))
    return preprocessed

  '''
  @param text: a line with words
  Removes insignificant words from the given line
  '''

  def removeStopwords(self, text):
    return " ".join(
      [word for word in str(text).split() if word not in stopWords])

  '''
  @param path: The file path of target text file
  Inserts all the significant words from the given file
  into the tree
  '''

  def loadFromFile(self, path):
    words = self.parseFile(path)

    for i in words:
      self.insert(i)

  '''
      @param k: number of items to search
      @param path: The file to pick words from

      This function generates a list of k words,
      half of them are in the hash table, and half
      are not.

      @return: a list of strings
  '''
  def searchList(self, k, path):
    words = self.parseFile(path)
    wordList = []
    for i in words:
      wordList.append(i)
    searchList = []
    while (len(searchList) < k / 2):
      randItem = random.choice(wordList)
      if (randItem not in searchList):
        searchList.append(randItem)
    while len(searchList) != k:
      ## Append some string that isn't a word
      searchList.append(str(random.random()))
    return searchList


def main():
  ## Capacity of 100
  hTable = HashTable(100)
  file = "A3test.txt"
  hTable.loadFromFile(file)
  hTable.printString()
  test1 = hTable.searchList(10, file)
  test2 = hTable.searchList(20, file)
  test3 = hTable.searchList(30, file)
  test4 = hTable.searchList(40, file)
  test5 = hTable.searchList(50, file)

  print("Test 1, (Frequency, Search Steps)")
  for i in range(len(test1)):
    print("Search", test1[i])
    print(hTable.search(test1[i]))
  print("\n")

  print("Test 2, (Frequency, Search Steps)")
  for i in range(len(test2)):
    print("Search", test2[i])
    print(hTable.search(test2[i]))
  print("\n")

  print("Test 3, (Frequency, Search Steps)")
  for i in range(len(test3)):
    print("Search", test3[i])
    print(hTable.search(test3[i]))
  print("\n")

  print("Test 4, (Frequency, Search Steps)")
  for i in range(len(test4)):
    print("Search", test4[i])
    print(hTable.search(test4[i]))
  print("\n")

  print("Test 5, (Frequency, Search Steps)")
  for i in range(len(test5)):
    print("Search", test5[i])
    print(hTable.search(test5[i]))
  print("\n")


if __name__ == "__main__":
  main()
