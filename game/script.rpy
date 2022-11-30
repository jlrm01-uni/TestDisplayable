
define e = Character("Eileen")

style dramatic_text is text:
    size 90

image big_text = ParameterizedText(style="dramatic_text")

label start:

    show big_text "This is dramatic" at truecenter
    pause 2
    
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
