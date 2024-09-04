# There is no block level scope in Python. Global Scope 
# and Function Scope are the primary scopes. 

# MODIFYING a global scope variable within a function 
# can only be done using the global keyword. Otherwise, 
# you will be creating a local scope variable and modifying 
# that instead. 

# GLOBAL SCOPE - BASICS
print("GLOBAL SCOPE - BASICS:")
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function (local scope): {enemies}")

increase_enemies()
print(f"enemies outside function (global scope): {enemies}")

# GLOBAL SCOPE - MODIYFING

print("\nGLOBAL SCOPE - MODIFYING:")
enemies = 1

def increase_enemies():
    print(f"enemies inside function (global scope): {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function (global scope): {enemies}")

# Global Scope - Modifying inside function using global keyword
print("\nGLOBAL SCOPE - Modifying inside function using global keyword:")
player_health = 10
def game():
    global player_health
    player_health += 1
print(f"player_health before function call (Global Scope): {player_health}")
game()
print(f"player_health after function call (Global Scope): {player_health}")

# Local Scope
print("\nLOCAL SCOPE:")
def drink_potion():
    potion_strength = 2
    print(f"potion_strength inside function (Local Scope): {potion_strength}")

drink_potion()
print(f"potion_strength is undefined outside of the function")
# print(potion_strength)  # not defined error

# There is no Block Scope
print("\nBLOCK SCOPE - there is no such thing in Python:")
game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(f"new_enemy defined inside a block has the same value outside the block: {new_enemy}")
create_enemy()

#Global Constants
print("\nGLOBAL CONSTANTS - Capitalized by convention:")
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@onefamilysblog"
print(f"Global Constant Examples - PI: {PI}, URL: {URL}, TWITTER_HANDLE: {TWITTER_HANDLE}")
