class Trinode():
    def __init__(self, v = None, l = None, r = None):
        self.value = v
        self.left = l
        self.right = r



class Tree:
    def __init__(self):
        self.root = None


    def __find_recursive(self, trinode, value):
        if trinode == None:
            return None
        if value > trinode.value:
            return self.__find_recursive(trinode.right, value)
        elif value < trinode.value:
            return self.__find_recursive(trinode.left, value)
        return trinode

    def find(self, value):
        return self.__find_recursive(self.root, value)


    def __insert_recursive(self, trinode, value):
        if trinode == None:
            trinode = Trinode(value)
            return trinode
        if value == trinode.value:
            return
        elif value > trinode.value:
            trinode.right = self.__insert_recursive(trinode.right, value)
            return trinode
        elif value < trinode.value:
            trinode.left = self.__insert_recursive(trinode.left, value)
            return trinode

    def insert(self, value):
        self.root = self.__insert_recursive(self.root, value)


    def __find_min(self, trinode):
        current = trinode
        while current.left != None:
            current = current.left
        return current


    def __eliminating_recursive(self, trinode, value):
        if trinode == None:
            return None

        if value < trinode.value:
            trinode.left = self.__eliminating_recursive(trinode.left, value)
        elif value > trinode.value:
            trinode.right = self.__eliminating_recursive(trinode.right, value)
        else:
            if trinode.left == None and trinode.right == None:
                return None
            if trinode.left == None:
                return trinode.right
            elif trinode.right == None:
                return trinode.left

        tmp = self.__find_min(trinode.right)
        trinode.value = tmp
        trinode.right = self.__eliminating_recursive(trinode.right, tmp.value)

    def eliminating(self, value):
        self.root = self.__eliminating_recursive(self.root, value)


    def __print_tree_recursive(self, trinode):
        if trinode != None:

            self.__print_tree_recursive(trinode.left)
            self.__print_tree_recursive(trinode.right)
            print(trinode.value)

    def print_tree(self):
        self.__print_tree_recursive(self.root)

    def draw(self):
        # Мы используем обычные символы, чтобы они отображались везде
        self.__draw_simple(self.root, "", "")

    def __draw_simple(self, trinode, prefix="", children_prefix=""):
        if trinode is None:
            return

        # Сначала правое
        if trinode.right is not None:
            self.__draw_simple(trinode.right, children_prefix + "|-- ", children_prefix + "|   ")

        # Корень
        if prefix == "":
            print(f"{trinode.value}")
        else:
            print(f"{prefix}{trinode.value}")

        # Потом левое
        if trinode.left is not None:
            self.__draw_simple(trinode.left, children_prefix + "L-- ", children_prefix + "    ")


tree = Tree()
tree.insert(10)
tree.insert(15)
tree.insert(20)
tree.insert(5)
tree.insert(13)
tmp = tree.find(15)
tree.print_tree()
tree.draw()