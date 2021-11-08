# a121_catch_a_turtle.py
 
 
#-----import statements-----
import turtle as trtl
import random as rand
import learderboard as lb
#-----game configuration----
spot_color = "lightcoral"
spot_size = int(2)
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20,"normal")
timer=5
counter_interval = 1000
timer_up= False
colors = ["forestgreen", "mediumseagreen", "khaki", "yellowgreen", "olive drab"]
sizes = [0.5, 1, 1.5, 2, 2.5]
start_font_setup = ("Arial", 30, "normal")
# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

#-----initialize turtle-----
spot = trtl.Turtle()
score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.goto(-290,190)
counter = trtl.Turtle()
counter.speed(0)
counter.penup()
counter.goto(-290,100)
bgshape = trtl.Turtle()
bgshape.shape("turtle")
bgshape.shapesize(int(2))
bgshape.color("palegreen")
#-----game functions--------
spot.color(spot_color)
spot.shapesize(spot_size)
spot.shape(spot_shape)

def change_position ():
  new_xpos = rand.randint(-300,300)
  new_ypos = rand.randint(-300,300)
  spot.goto(new_xpos, new_ypos)
  bgshape.penup()
  bgshape.goto(new_xpos, new_ypos)

def add_color():
  bgshape.hideturtle()
  bgshape.penup()
  newcolor = rand.choice(colors)
  bgshape.color(newcolor)
  bgshape.left(20)
  bgshape.forward(100)
  bgshape.stamp()

def change_size():
  newsize = rand.choice(sizes)
  spot.shapesize(newsize)

def spot_clicked(x,y):
  global timer_up
  if timer_up == False:
    spot.hideturtle()
    spot.penup()
    change_size()
    update_score()
    change_position()
    spot.showturtle()
    add_color()
  else:
    spot.hideturtle()
    bgshape.color("palegreen")
    bgshape.stamp()

def update_score():
  score_writer.clear()
  global score
  score += 1
  score_writer.write(score, font=font_setup)
 
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up=True
    manage_leaderboard()
  else:
    counter.write("timer: " + str(timer), font=font_setup)
    timer -=1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)


spot.onclick(spot_clicked)
wn=trtl.Screen ()
wn.bgcolor("mediumturquoise")
wn.ontimer(countdown, counter_interval)
wn.mainloop ()

