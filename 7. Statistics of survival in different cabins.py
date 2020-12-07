import pygal

bar_chart = pygal.Bar()
# the title of bar_chart is：Statistics of passengers in different cabins
bar_chart.title = "Statistics of passengers in different cabins"
bar_chart.x_labels = map(str, ["first class","second class","third class"])
bar_chart.add('survivors', [136,87,119])
bar_chart.add('victims', [80,97,372])
bar_chart.render()
