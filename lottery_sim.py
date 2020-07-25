import random
import plotly.graph_objects as go
from plotly import offline

# A simple lottery simulator drawing numbers 1,000,000 times and results recorded on a histogram.

# Establish range of numbers to select balls from

numbers = list(range(1, 50))

# Match variables corresponding to number of matches after each draw has been made

matches_0 = 0
matches_1 = 0
matches_2 = 0
matches_3 = 0
matches_4 = 0
matches_5 = 0
matches_6 = 0

# Populate a list before while loop to set the ''customer's'' ticket

ticket = []
while len(ticket) < 6:
  draw = random.choice(numbers)
  if draw in ticket:
    continue
  ticket.append(draw)



i = 0

while i < 1_000_000:


	lottery = []
	while len(lottery) < 6:
		draw = random.choice(numbers)
		if draw in lottery:
			continue
		lottery.append(draw)

    
	same = []
	for x in lottery:
		for y in ticket:
			if x == y:
				same.append(y)

	matches = len(same)
  
	if matches == 0:
		matches_0 += 1

	elif matches == 1:
  		matches_1 += 1

	elif matches == 2:
  		matches_2 += 1

	elif matches == 3:
  		matches_3 += 1

	elif matches == 4:
  		matches_4 += 1

	elif matches == 5:
  		matches_5 += 1

	elif matches == 6:
  		matches_6 += 1

	i += 1

  
# Print at intervals to ensure program is running and working.

	if i == 10000:
	  	print(i)

	elif i == 100000:
		print(i)

	elif i == 200000:
	    print(i)

	elif i == 300000:
		print(i)

	elif i == 400000:
		print(i)

	elif i == 500000:
		print(i)

	elif i == 750000:
		print(i)

	elif i == 1000000:
		print(i)

# Record number of matches and frequency of matches to use as the x/y axis on histogram

x_values = [0, 1, 2, 3, 4, 5, 6]
y_values = [matches_0, matches_1, matches_2, matches_3, matches_4, matches_5, matches_6]

fig = go.Figure(data=[go.Bar(x=x_values, y=y_values, text=y_values, textposition='outside')])

# Configure x/y axis titles and plot

fig.update_layout(
    title="Results of running a 6 ball (1-50) lottery simulator 1,000,000 times",
    xaxis_title="Lottery Ball Matches",
    yaxis_title="Frequency of Matches",
    legend_title="Legend Title",
    font=dict(
        family="Droid Serif, monospace",
        size=14,
        color="Black"
    ))

offline.plot(fig)

