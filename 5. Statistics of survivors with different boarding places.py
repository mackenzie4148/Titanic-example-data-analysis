import pygal
line_chart = pygal.Line()
line_chart.title = "Statistics of survivors with different boarding places" 
line_chart.x_labels = map(str, ["Queenstown","Cherbourg","Southampton"])
line_chart.add('Survivors',[30, 93, 217])
line_chart.add('victims',[47, 75, 427])
line_chart.render()
