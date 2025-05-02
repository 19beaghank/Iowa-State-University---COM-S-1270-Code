#Kevin Beaghan 2/21/2025
#Week 5 Lab - Creating a story using if statements and inputs

def main():
    print("""Adventure Story - Kevin Beaghan
          """)
    hall = input("""You find yourself in a old mansion with hallways ahead of you.
Do you want to go [left] or [right]?:""")
    if hall == "left":
        left =  input("""You walk down the left hallway and come across a locked door.
Do you want to [break] down the door, or [find] another way?:""")
        if left == "break":
            Break = input("""You break down the door and gop through, only to find that it's a giant library!
Do you want to go [back], or [explore] the library?:""")
            if Break == "back":
                print("""You turn back the way you came.
As you are walking you hear something behind you.
You start running but its gaining on you!
You race to the front door and just barely get out before jaws snap behind you before you slam the front door shut.
Relief washes over you now that you are free, never planning to returning.""")
            if Break =="explore":
                print("""This is the greatest library on Earth.
You love reading so you could spend some time down here.
It's only too late do you realize you have gotten lost in an infinite maze of books, never to escape.""")
        if left == "find":
            print("""You look around but only see a large ornate mirror!
Wait, you see more than just your reflection, you see something behind you.
Then everything goes blank, you have become possesed and are now one of the entities haunting the mansion.""")
    if hall == "right":
        right = input("""You walk down the right hallway and come to a dead end.
Do you want to [turn] back, or [look] clues?:""")
        if right == "turn":
            turn = input("""You head back to the enterence.
Do you want to go down the [left] hall or [leave]?""")
            if turn == "left":
                print("""A bat flies down scaring you half to death.
You trun and leave before anything else can get you.""")
            if turn == "leave":
                print("""You trun to go, I guess the rumors weren't true.
There is nothing special about this old house.""")
        if right == "look":
            print("""You look for clues and find nothing, but you do hear some strange noises behind the walls.
You run away scared and leave the mansion. Turns out the rumors were true, it is haunted.""")

if __name__ == "__main__":
    main()