class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Binary_Tree:
    def __init__(self):
        self.root = None
    '''
    @param current: the current node
    @param value: the value to be inserted
    Inserts value into the tree whose root is current
    '''
    def insert_node(self, current, value):
        if current == None:
            current = Node(value)
            return current
        else:
            if current.data == value:
                return current
            elif current.data < value:
                current.right = self.insert_node(current.right, value)
            else:
                current.left = self.insert_node(current.left, value)
        return current
    '''
    Wrapper function
    '''
    def insert(self, value):
        self.root = self.insert_node(self.root, value)
        return self.root

    '''
    @param root: the root of the binary search tree
    @param height: The current height of the node
    Traverse goes through the whole tree, and each of the node's
    heights are added to the total height.
    '''
    def traverse(self, root, height):
        if root == None:
            return 0;
        height = height + 1
        heightSum = height
        heightSum = heightSum + self.traverse(root.left, height)
        heightSum = heightSum + self.traverse(root.right, height)
        return heightSum
    '''
    Wrapper function
    '''
    def get_total_height(self):
        height = -1;
        return self.traverse(self.root, height)
    '''
    Wrapper function
    '''
    def delete(self, value):
        self.delete_node(self.root, value)
    '''
    @param current: the current node
    @param value: the value to be removed
    Removes the value from a binary search tree with currant as its root
    '''
    def delete_node(self, current, value):
        if current == None:
            return current
        if value < current.data:
            current.left = self.delete_node(current.left, value)
        elif value > current.data:
            current.right = self.delete_node(current.right, value)
        else:
            if current.left == None:
                current = current.right
                return current
            elif current.right == None:
                current = current.left
                return current

            if self.root.right == None:
                minNode = self.root
            else:
                minNode = self.root.right
            while(minNode.left != None):
                minNode = minNode.left
            current.data = minNode.data
            current.right = self.delete_node(current.right, current.data)

        return current
    '''
    Saves a preorder traversal with the None pointers. When the None pointers
    are included, each preorder is unambiguous.
    '''
    def preOrder(self, current):
        if current == None:
            return "None,"
        toString = str(current.data) + ","
        toString = toString + self.preOrder(current.left)
        toString = toString + self.preOrder(current.right)
        return toString
    '''
    Wrapper function
    '''
    def save(self):
        saveString = self.preOrder(self.root)
        # Always ends with an extra ',', so remove it
        return saveString[:len(saveString)-1]
    '''
    @param current: current node
    @param data: Data for new node
    Creates a new child node with data that's either left or right
    '''
    def create_node(self, current, data):
        if current == None and data != "None":
            current = Node(int(data))
        elif current == None and data == "None":
            current = Node(0)
        if data == "None":
            if current.left == None:
                current.left = None
            elif current.right == None:
                current.right = None
        else:      
            if current.data > int(data):
                current.left = self.create_node(current.left, int(data))
            if current.data < int(data):
                current.right = self.create_node(current.right, int(data))
        return current

    '''
    @param input_string: the save string of a binary search tree
    Creates a new binary search tree with the save string. Overwrites
    whatever instance of Binary_Tree called it.
    '''
    def restore(self, input_string):
        # Runs into a problem if the root of the bst is None. Root is replaced anyways
        if self.root == None:
            self.root = Node(0)
        ordered_nodes = input_string.split(",")
        i = 0
        while (i < len(ordered_nodes)):
            self.create_node(self.root, ordered_nodes[i])
            i += 1

def main():
    bst = Binary_Tree()
    bst.insert(100)
    bst.insert(20)
    bst.insert(200)
    bst.insert(10)
    bst.insert(30)
    bst.insert(150)
    bst.insert(300)
    print("current tree:", bst.save())
    bst.delete(300)
    print("300 deleted:", bst.save())
    bst.insert(300)
    print("300 inserted:", bst.save())
         
    print("Total node heights:",bst.get_total_height())
    save = bst.save()
    print("original save:", save)
    bst.restore(save)
    print("restored save (second save):", bst.save())

if __name__=="__main__":
    main()

