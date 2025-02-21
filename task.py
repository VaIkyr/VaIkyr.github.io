print(r'''*******************************************************************************
⠀⠀⠀⠀⠀⠀⠀⠀
*******************************************************************************
''')
print("DARK SOULS. PREPARE TO SUFFER EDITION")
print("Oh the hollow one.")
print("You're at a cross road, which way do you want to go?")
direction = input("Type east or west").lower()
if direction == "east" or direction != "west":
    print ("YOU DIED")
else:
    print("You collected Estus Flask and found a broken sword along the way.")
    print("After defeating some skeletons, you came across the shore, there is an island not so far away.")
    print("What would you do? Try to swim to there or wait?")
    island = input("Type swim or wait").lower()
    if island == "swim" or island != "wait":
        print("YOU DIED")
    else:
        print("With the insight of your patience, a small boat starts to appear with rows in it. You get into it and start rowing.")
        print("As you get closer to the island, the land behind you starts shifting into a void.")
        print("You reach the island and get off the boat. There are three vague paths leading into unknown.")
        print("One with a shiny red glow, one with e dark blue, and the last one with a flowery yellow color.")
        print("Which one would you try?")
        path = input("Type red, blue or yellow").lower()
        if path == "red" or path != "blue":
            print("SOUL INCINERATED")
        elif path == "blue" or path != "yellow":
            print("SOUL SHATTERED")
        else:
            print("You see the remains of the Elder Ones, suddenly a form completely unknown to you embraces you.")
            print("You are transcending into a higher being. As your memories and old existence fades away;\n You finally feel alive.")
