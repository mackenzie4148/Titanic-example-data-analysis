# survial statitics
survive_female = 223
non_survive_female =81
survive_male = 109
non_survive_male = 468

import pygal
# Survival statistics of Titanic
line_chart = pygal.Bar()
line_chart.title = 'Survival Statistics of Titanic'
line_chart.x_labels = map(str, ["Survival","Victim"])
line_chart.add('Female',  [survive_female, non_survive_female])
line_chart.add('Male',  [survive_male, non_survive_male])
line_chart.render()
