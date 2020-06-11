import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty ('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    speak("Welcome in Dr.A P J Abdul Kalam Library. Please Enter Your Choice")


class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print ("We have following books in our library: ",self.name)
        speak("We have following books in our library")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        for i in self.lendDict.items():
            print(i)
        if book not in self.lendDict.keys():
            self.booksList.remove(book)
            self.lendDict.update({book:user})
            speak("Lender-Book database has been updated. You can take the book now")
            print("Lender-Book database has been updated. You can take the book now")

        else:

            print("Book is already being used by ",self.lendDict[book])
            speak (f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")
        speak("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)
        speak("Thanks for Returning a book. Have a good Day")
        self.booksList.append(book)
'''
if __name__ == '__main__':
    ash = Library(['Python', 'AI and ML', 'Cloud Computing By Aasim', 'Datastucture', 'Algorithms by CLRS','Data Science'],"APJ Abdul Kalam")
    wish()
    while(True):
        print(f"Welcome to the {ash.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            speak("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            ash.displayBooks()

        elif user_choice == 2:
            ash.displayBooks ()
            print ("Enter the name of the book you want to lend:-")
            speak ("Enter the name of the book you want to lend:-")

            book = input()

            print ("Enter your name:-")
            speak ("Enter your name:-")

            user = input()
            ash.lendBook(user, book)

        elif user_choice == 3:

            print ("Enter the name of the book you want to add:")
            speak ("Enter the name of the book you want to add:")

            book = input()
            ash.addBook(book)

        elif user_choice == 4:

            print ("Enter the name of the book you want to return:")
            speak ("Enter the name of the book you want to return:")
            book = input()
            ash.returnBook(book)

        else:
            print("Not a valid option")
            speak ("Not a vaild option")



        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                speak("Thank You For Coming in Our Library")
                exit()

            elif user_choice2 == "c":
                continue'''
ash = Library(['Python', 'AI and ML', 'Cloud Computing By Aasim', 'Datastucture', 'Algorithms by CLRS','Data Science'],"APJ Abdul Kalam")
wish()
while(True):
    print(f"Welcome to the {ash.name} library. Enter your choice to continue")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")
    user_choice = input()
    if user_choice not in ['1','2','3','4']:
        print("Please enter a valid option")
        speak("Please enter a valid option")
        continue

    else:
        user_choice = int(user_choice)


    if user_choice == 1:
        ash.displayBooks()

    elif user_choice == 2:
        ash.displayBooks ()
        print ("Enter the name of the book you want to lend:-")
        speak ("Enter the name of the book you want to lend:-")

        book = input()

        print ("Enter your name:-")
        speak ("Enter your name:-")

        user = input()
        ash.lendBook(user, book)

    elif user_choice == 3:

        print ("Enter the name of the book you want to add:")
        speak ("Enter the name of the book you want to add:")

        book = input()
        ash.addBook(book)

    elif user_choice == 4:

        print ("Enter the name of the book you want to return:")
        speak ("Enter the name of the book you want to return:")
        book = input()
        ash.returnBook(book)

    else:
        print("Not a valid option")
        speak ("Not a vaild option")



    print("Press q to quit and c to continue")
    user_choice2 = ""
    while(user_choice2!="c" and user_choice2!="q"):
        user_choice2 = input()
        if user_choice2 == "q":
            speak("Thank You For Coming in Our Library")
            exit()

        elif user_choice2 == "c":
            continue
