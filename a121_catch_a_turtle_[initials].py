#   a121_TR_catch_a_turtle_complete.py

#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#-----game configuration-----

colors = ["forestgreen", "mediumseagreen", "khaki", "yellowgreen", "olive drab"]
font_setup = ("Arial", 20, "normal")
spot_size = 2
spot_color = "green"
spot_shape = "turtle"
timer = 30
counter_interval = 1000 
timer_up = False
score = 0

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

#-----initialize the turtles-----
spot = trtl.Turtle() 
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(160, 160)
score_writer.pendown()
#score_writer.showturtle()

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-160, 160)
counter.pendown()
#counter.showturtle()

#-----game functions-----

# countdown function
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# update and display the score
def update_score():
  global score
  score = score + 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

# what happens when the spot is clicked
def spot_clicked(x,y):
  global timer_up
  if (not timer_up):
    update_score()
    change_position()
  else:
    spot.hideturtle()
  
# resize the turtle
def resize():
  sizes = [1, 1.5, 2, 2.5]
  spot.shapesize(rand.choice(sizes))

# stamp turtle
def leave_a_mark():
  spot.color(rand.choice(colors[1:]))
  spot.stamp()
  spot.fillcolor(colors[0])

# change the position of spot
def change_position():
  leave_a_mark()
  resize()
  new_xpos = rand.randint(-150, 150)
  new_ypos = rand.randint(-150, 150)
  spot.penup() 
  spot.hideturtle()
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()
  spot.pendown()
 
# starting the game
def start_game():
  spot.onclick(spot_clicked)
  counter.getscreen().ontimer(countdown, counter_interval)

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


#----------events----------
start_game()
wn = trtl.Screen()
wn.bgcolor("mediumturquoise")
wn.mainloop()
