# Declare images below this line, using the image statement.
image hunky men = "hunky_men.png"
image fans = "fans.png"
image schedule demo = "schedule_demo.png"

# Declare characters used by this game.
define n = Character('Narrator', color="#AA0000")

init python:
  register_stat("Beauty", "beauty", 1, 200)
  register_stat("Charm", "charm", 1, 200)
  register_stat("Wit", "wit", 1, 200)

  dp_period("Afternoon", "afternoon_act")
  dp_choice("go shopping", "shopping")
  dp_choice("take a surfing lesson", "surfing")
  
  dp_period("Evening", "evening_act")
  dp_choice("take a yoga class", "yoga")
  dp_choice("go to the beach", "beach")
  dp_choice("go to the bar", "bar")
  
  dp_period("Night", "night_act")
  dp_choice("go clubbing", "nightclub")
  dp_choice("stay in", "stay_in")

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
      hide hunky men
      jump you_know_the_drill

  label explain_like_im_five:
    "ミス美人, the \"Ichiban Bijin Miss Contest\" is held every year on the
    island. The prettiest girls from all around the world come to compete."
    "There are 100 days until the contest. Your goal is to spend those days
    wisely and win the contest!"
    "You'll need wit, beauty, and charm to win the contest."
    "But more than anything else, you'll need fans."
    hide hunky men
    show fans
    "ミス美人 is decided by judges, but the fans also vote. The contest has
    traditionally been won by whichever girl wins the most votes."
    "You can gain fans like any other celebrity: by being seen in public."
    "Every day is broken down into morning, afternoon, and night. You can
    choose something to do in each period."
    show schedule demo

  label you_know_the_drill:

  jump day


label day:

  $ afternoon_act = None
  $ evening_act = None
  $ night_act = None

  "What will you do?"

  call screen day_planner(["Afternoon", "Evening", "Night"])

  return
