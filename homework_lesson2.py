#Nested Decisions: The Adventure Game

#Task1 buggy_code
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!") #grammatical error from hw question -- not mine
    
    
#Task2 setting_the_scene
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
            print("You found a boat!")
elif place == "cave":  
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You found some hidden treasure on your path!")
    elif action == "proceed in the dark":
        print("Oh no! You walked straight into a trap set by exiled trolls!")
    


#Task3 default_path
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    print("You found a hidden treasure!")
else:
    pass


#Quick Decisions: The Event Planner
#Task1 code_correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
    
#Task2 venue_selection
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
facilities = "audio system" if attendees > 100 else "small speakers"
print("the venue will be the" , venue)
print("and based on your party size we recommend the" , facilities)


#Task3 catering_choices
vegetarian = input("Do you want a vegetarian only menu? answer, yes or no: ")
if vegetarian == "yes":
    print("We recommend Veggie Delight Caterers!")
else:
    print("We recommend Gourmet Meals Caterers!")