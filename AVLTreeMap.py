import re
import string
from nltk.corpus import stopwords

# AVL Tree that stores a sentence in a tree (removing stopwords)
class Node:

  def __init__(self, word):
    self.left = None
    self.right = None
    self.word = word
    self.height = 1
    self.frequency = 1


class AVL_Tree:

  def __init__(self):
    self.root = None
    self.stop_words = set(stopwords.words('english'))

  def parse_file(self, file):
    with open(file, 'r') as input:
      content = input.readlines()
    preprocessed = []
    for line in content:
      line = line.strip().lower()
      #remove punctuation
      line = line.translate(str.maketrans('', '', string.punctuation))
      #remove stop words that care no specific meaning
      line = self.remove_stopwords(line)  #remove numbers
      line = re.sub('\d+', '', line)  #remove extra white space
      line = re.sub(' +', ' ', line)
      if line:
        preprocessed.extend(line.split(" "))
    print(" ".join(preprocessed))
    return preprocessed

  def remove_stopwords(self, text):
    return " ".join(
      [word for word in str(text).split() if word not in self.stop_words])

  def getHeight(self, current):
    if current == None:
      return 0
    return current.height

  def getBalance(self, current):
    if current == None:
      return 0
    return self.getHeight(current.left) - self.getHeight(current.right)

  def rotate_left(self, current):
    right_child = current.right
    left_grand = right_child.left

    right_child.left = current
    current.right = left_grand

    current.height = 1 + max(self.getHeight(current.left),
                             self.getHeight(current.right))
    right_child.height = 1 + max(self.getHeight(right_child.left),
                                 self.getHeight(right_child.right))
    return right_child

  def rotate_right(self, current):
    left_child = current.left
    right_grand = left_child.right

    left_child.right = current
    current.left = right_grand

    current.height = 1 + max(self.getHeight(current.left),
                             self.getHeight(current.right))
    left_child.height = 1 + max(self.getHeight(left_child.left),
                                self.getHeight(left_child.right))
    return left_child

  def insert_node(self, current, word):
    if current == None:
      current = Node(word)
      return current
    elif word < current.word:
      current.left = self.insert_node(current.left, word)
    elif word > current.word:
      current.right = self.insert_node(current.right, word)
    else:
      current.frequency += 1

    current.height = 1 + max(self.getHeight(current.left),
                             self.getHeight(current.right))

    bal = self.getBalance(current)

    # Balancing 4 cases
    if bal > 1 and word < current.left.word:
      return self.rotate_right(current)
    if bal < -1 and word > current.right.word:
      return self.rotate_left(current)
    if bal > 1 and word > current.left.word:
      current.left = self.rotate_left(current.left)
      return self.rotate_right(current)
    if bal < -1 and word < current.right.word:
      current.right = self.rotate_right(current.right)
      return self.rotate_left(current)
    return current

  def insert(self, word):
    self.root = self.insert_node(self.root, word)
    return self.root

  def load_from_file(self, path):
    words = self.parse_file(path)

    for i in words:
      self.insert(i)

  def traverse(self, current):
    if current == None:
      return ""
    toString = current.word + " (x" + str(current.frequency) + "), "
    toString += self.traverse(current.left)
    toString += self.traverse(current.right)
    return toString

  def to_string(self):
    toString =  self.traverse(self.root)
    return toString[:len(toString) - 2]


def main():
  avl = AVL_Tree()
  avl.load_from_file("test.txt")
  print("\n", avl.to_string())


if __name__ == "__main__":
  main()
