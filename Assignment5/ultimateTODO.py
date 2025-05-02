# Kevin Beaghan 4/8/2025
# [COMS 1270 1] Assignment 5

# Creating a to do list where things can be added, deleted, and moved to other 
#   sublists depending of the state of completion and priority

import sys
import pickle

def printTitleMaterial():
    print("The Ultimate TODO List!")
    print()
    print("By: Kevin Beaghan")
    print("[COM S 127 1]")
    print()

def initList():
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []
    return todoList

def checkIfListEmpty(todoList):
    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):
        return False
    return True

def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    return todoList

def checkItem(item, todoList):
    itemFound = False
    keyName = ""
    index = -1
    for key, lst in todoList.items():
        if item in lst:
            itemFound = True
            keyName = key
            index = lst.index(item)
            break
    return itemFound, keyName, index

def addItem(item, toList, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound:
        print(f"Error: The item '{item}' already exists in the list '{keyName}' at index {index}.")
    else:
        if toList in todoList:
            todoList[toList].append(item)
            print(f"Item '{item}' successfully added to the list '{toList}'.")
        else:
            print(f"Error: The list '{toList}' does not exist.")
    return todoList

def deleteItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound:
        todoList[keyName].pop(index)
        print(f"Item '{item}' successfully deleted from the list '{keyName}'.")
    else:
        print(f"Error: The item '{item}' does not exist in any list.")
    return itemFound, todoList

def moveItem(item, toList, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound:
        print(f"Error: The item '{item}' already exists in the list '{keyName}' at index {index}.")
    else:
        if toList in todoList:
            todoList[toList].append(item)
            print(f"Item '{item}' successfully added to the list '{toList}'.")
        else:
            print(f"Error: The list '{toList}' does not exist.")
    return todoList

def printTODOList(todoList):
    for key, value in todoList.items():
        print(f"{key}: {value}")
    return None

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()
        if choice == "a":
            item = input("Enter the item you want to add to 'backlog': ")
            todoList = addItem(item, 'backlog', todoList)
            printTODOList(todoList)
        elif choice == "m":
            if not checkIfListEmpty(todoList):
                print("No items to move!")
            else:
                item = input("Enter the item you want to move: ")
                itemFound, _, _ = checkItem(item, todoList)
                while not itemFound:
                    print(f"Error: The item '{item}' does not exist. Please enter a valid item.")
                    item = input("Enter the item you want to move: ")
                    itemFound, _, _ = checkItem(item, todoList)
                toList = input("Enter the name of the list to move the item to: ")
                while toList not in todoList:
                    print(f"Error: The list '{toList}' does not exist. Please enter a valid list name.")
                    toList = input("Enter the name of the list to move the item to: ")
                todoList = moveItem(item, toList, todoList)
                printTODOList(todoList)
        elif choice == "d":
            if not checkIfListEmpty(todoList):
                print("No items to delete!")
            else:
                item = input("Enter the item you want to delete: ")
                _, todoList = deleteItem(item, todoList)
                printTODOList(todoList)
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()
    return todoList

def main():
    taskOver = False
    printTitleMaterial()
    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()