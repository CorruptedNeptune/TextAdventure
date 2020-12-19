

while True:
    player_name = input("""
What is your name? > """)
    if len(player_name) > 15 or len(player_name) < 3:
        print("ass name")
    elif input(f"Are you sure {player_name} is your name? > ").lower() == "yes":
        break
    else:
        pass
print(f"Welcome {player_name}")

print("""
You wake up to the sound of leaves rustling outside their window. Your bedroom is cluttered with junk
ranging from clothes to action figures. It seemed like you had awoken around midnight.
Being parched you decide to...
""")

while True:
    choice_1 = input("""
1. Go downstairs and take a drink.
2. Stay in bed and sleep the night.
> """)
    if choice_1 == "1":
        print("""
        You make your way down the stairs carefully as to not wake up your parents. You make your way towards the 
        kitchen after passing through the spacious living room. You grab your favorite Lightning McQueen water cup and
        drink out of it. Out of the corner of your eye you think you see a fleeting figure go past your kitchen window..
        You shrug it off thinking it's just your eyesight since you didn't grab your glasses. You quickly and quietly 
        make your way back upstairs into your bed...
        """)
        break
    elif choice_1 == "2":
        print("""
        You slowly fall back asleep. Closing your eyes and trying to resume the dream you were dreaming..""")
        break
    else:
        pass

print(f"""
"Wake up {player_name}!" """)
while True:
    choice_2 = input("""
    """)





