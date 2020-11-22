from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(self): pass


class MyBook(Book):
    #Has a parameterized constructor taking these  parameters
    def __init__(self,title,author,price):
        super(Book,self).__init__()#use supper class "super" calls the superclass's constructer (which is Book's constructor). We do this to initialize variables.
        #self.title = title
        #self.author = author
        self.price = price
    #lements the Book class' abstract display() method so it prints these lines
    def display(self):
        print("Title:", title)
        print("Author:", author)
        print("Price:", price)




#Write MyBook class

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()