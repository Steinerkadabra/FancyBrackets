import matplotlib.pyplot as plt
import numpy as np
import FancyBrackets.brackets as fb


# First, we need something to plot

fig, ax = plt.subplots()
x = np.linspace(0, 9.5*np.pi, 2000)

ax.plot(x, np.sin(x), 'k-')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ylim(-2, 2)
ax.set_xlim(0, 11* np.pi)

# To mark the first period below the signal, we draw a curly bracket from the position of the beginning of first period to the end
# To draw a bracket we call fb.CurlyBracket. There are some parameter we have to give the funktion:
# - the starting point as an array [x_start, y_start] and the ending point [x_end, y_end]
# - the widht of the bracket
# - the ax to which to draw it on
# additionally, we can change the color, linewidth, and linestyle
# Lets mark the first period with a blue curly bracket and add some text
fb.CurlyBracket([0, -1.2], [2* np.pi, -1.2], 0.2,  ax)
ax.text(np.pi, -1.6, 'Period 1', va = 'center', ha = 'center', color = 'blue')
# To mark the the next two  periods in red with a dotted line with stronge linewisth just change, color, ls and lw

fb.CurlyBracket([2*np.pi, -1.2], [8* np.pi, -1.2], 0.2,  ax, color = 'red', ls = ':', lw = 4)
ax.text(5*np.pi, -1.6, 'Period 2-4', va = 'center', ha = 'center', color = 'red')

# We can also easily change the widht and therefore the curlyess of the brackets. Lets mark period 1 and 2 with other widths
# on top of the signal. To have tha bracket point upside, just change the starting and the endpoint
fb.CurlyBracket( [2* np.pi, 1.2], [0,1.2], 0.3,  ax, color = 'g')
ax.text(np.pi, 1.6, 'Period 1', va = 'center', ha = 'center', color = 'g')
fb.CurlyBracket( [4* np.pi, 1.2], [2*np.pi, 1.2], 0.1,  ax, color = 'k')
ax.text(3*np.pi, 1.6, 'Period 2', va = 'center', ha = 'center', color = 'k')

# To draw the bracket in another direction, i.e. to mark the amplitude, just change the points. The width is alwys
# relativ to the axis. As the scale is different, we need to make the width higher
fb.CurlyBracket( [9.75* np.pi, -1], [9.75* np.pi, 1], 1,  ax, color = 'k')
ax.text(10.5* np.pi, 0, '2 x Amplitude', va = 'center', ha = 'center', color = 'k', rotation = 90)

#Of course we can also plot it in different positions, but currently there will be some streching/skewnness issue
#depending on the scaling of the axes.
fb.CurlyBracket( [27.5, -1], [34, -1.75], 0.2,  ax, color = 'k')

plt.show()