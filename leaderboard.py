turtle_object.penup()
  turtle_object.goto(-200,100)
  turtle_object.hideturtle()
  turtle_object.down()
  leader_index = 0

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while leader_index < len(leader_names):
    turtle_object.write(str(leader_index + 1) + "\t" + leader_names[leader_index] + "\t" + str(leader_scores[leader_index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-200,int(turtle_object.ycor())-50)
    turtle_object.down()
    leader_index = leader_index + 1

  # Display message about player making/not making leaderboard based on high_scorer
  if (high_scorer):
    turtle_object.write("Congratulations! You made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry, you didn't make the leaderboard. Maybe next time!", font=font_setup)

  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-200,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  # TODO 10: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal

  if (player_score >= bronze_score and player_score < silver_score):
    turtle_object.write("... Bronze medal!", font=font_setup)
  elif (player_score >= silver_score and player_score < gold_score):
    turtle_object.write("... Silver medal!", font=font_setup)
  elif (player_score >= gold_score):
    turtle_object.write("... Gold medal!", font=font_setup)
