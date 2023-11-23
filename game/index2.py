import time

# Define variables
player_name = ""
player_health = 100
enemy_health = 50
inventory = []
stage = 1
item_found = False
is_key_used = False
max_time = 180  # 3 minutes in seconds

# Introduction and game objective
def game_intro():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious world...")
    time.sleep(1)
    print("Your objective is to reach the end of the adventure.")
    time.sleep(1)
    print("Be cautious with your choices!")
    time.sleep(1)
    print("=" * 40)
# Stage 1
def stage_one():
    global stage, item_found
    print("Stage 1: The Forest")
    time.sleep(1)
    choice = input("Do you want to go left or right? ").lower()
    if choice == "left":
        print("You discover a hidden path.")
        inventory.append("Map")
        item_found = True
        stage += 1
    elif choice == "right":
        print("You encounter a dangerous creature.")
        fail()
    else:
        print("Invalid choice. Try again.")
        stage_one()

def stage_two():
    global stage, is_key_used
    print("Stage 2: The Cave")
    time.sleep(1)
    print("You use the Map to navigate through the cave.")
    time.sleep(1)
    choice = input("Continue forward or go back? ").lower()
    if choice == "forward":
        print("You find a key and unlock a door.")
        inventory.append("Key")
        is_key_used = True
        stage += 1
    elif choice == "back":
        print("You encounter a collapsing tunnel.")
        fail()
    else:
        print("Invalid choice. Try again.")
        stage_two()


def win():
    print("Congratulations! You have successfully completed the Text Adventure Game.")

# Fail function
def fail():
    print("Game over! Better luck next time.")
    exit()


# Main game loop
def play_game():
    start_time = time.time()
    game_intro()

    while stage <= 5:
        if time.time() - start_time > max_time:
            print("Time's up! You did not complete the game in 3 minutes.")
            fail()

        if stage == 1:
            stage_one()
        elif stage == 2:
            stage_two()
        # Add more stages as needed

    # If the player reaches this point, they have won the game
    win()

play_game()
