# The script of the game goes in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image BG city a ="BG bedroom.jpg"
image yuzu_smile1 = "yuzu0.png"
image yuzu_smile2 = "yuzu1.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Yuzuha")
define unk = Character("???")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    unk "Wake up."

    unk "C'mon, wake up."

    unk "I SAID WAKE UP!"

    scene BG city a with dissolve

    show yuzu_smile1
    s "What are you spacing out for?"
    s "We're going to be late for the limited-edition Madoka Magica DVD set!"
    show yuzu_smile2
    s "This is going to be the only time we'll ever get it!"
    "This is Sayori, my childhood friend."
    "She's a really huge anime fan, especially her favorite anime of all time: Madoka Magica."
    "I usually just tag along with her because I don't have anything better to do."
    "I would usually just chill at home and read manga."
    "But today is special, according to Sayori."
    "The special edition of Madoka Magica releases today."
    ""
    "I made a change"
    # This ends the game.

    return
