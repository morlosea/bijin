# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image hunky men = "hunky_men.png"

# Declare characters used by this game.
define n = Character('Narrator', color="#AA0000")

# The game starts here.
label start:

  "You arrive on the beautiful island カリフォニャ."
  "The sun is shining, and there are already hunky men everywhere."
  show hunky men
  "But look out! You need to focus if you're ever going to win the contest."
  "What contest, you may ask?"

  menu:
    "What contest?":
      jump explain_like_im_five

    "Get on with it, I'm just here for the guys.":
      jump you_know_the_drill

  label explain_like_im_five:
    "ミス美人, the \"Ichiban Bijin Miss Contest\" is held every year on the island."

  label you_know_the_drill:

    return
