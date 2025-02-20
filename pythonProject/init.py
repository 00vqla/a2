class BST:

    # init method or constractor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print("Hello my name is", self.name)


# Creating different objects
b1 = BST('Monkey1')
b2 = BST('Monkey2')
b3 = BST('Monkey3')

b1.say_hi()
