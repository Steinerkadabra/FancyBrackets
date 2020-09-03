import numpy as np
from scipy.interpolate import interp1d
import sys



class CurlyBracket:
    def __init__(self, a, b, width, ax, lw = 2, color = 'b', ls = '-'):
        self.ax = ax
        self.lw = lw
        self.c = color
        self.ls = ls
        self.x_end = np.array([ 0.45959596, 0.45959596, 0.44949495, 0.3989899,
                                0.33838384, 0.26262626, 0.18181818, 0.0959596, -0])*width
        self.y_end = np.array([ 0.28184282, 0.22493225, 0.17615176, 0.12533333,
                                0.09214092, 0.05691057,0.02710027, 0.00813008, -0])*width
        self.x_start = np.array([1,0.90909091, 0.81313131, 0.72727273, 0.64141414, 0.56060606,
                                 0.49494949, 0.43666667, 0.40909091, 0.3989899, 0.3989899])*width
        self.y_start = np.array([1, 0.99457995, 0.98644986, 0.97289973, 0.95121951, 0.92411924,
                                 0.88888889, 0.84281843, 0.78861789, 0.73441734, 0.67208672])*width


        self.start = np.array(a)
        self.end = np.array(b)
        self.center = (self.start+self.end)/2
        self.w = width
        self.x_mid = None
        self.y_mid = None
        self.x = None
        self.y = None
        self.length = np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        self.degree = np.arccos(2*(a[1]-b[1])/(2*self.length))
        xlim = ax.set_xlim()
        ylim = ax.set_ylim()
        self.axes_ratio = (xlim[1]-xlim[0])/(ylim[1]-ylim[0])

        if self.axes_ratio > 1:
            self.stretch = np.max([abs(np.cos(self.degree)), 1/self.axes_ratio])
        else:
            self.stretch = np.max([abs(np.sin(self.degree)), self.axes_ratio])


        self.y_start = self.y_start / self.stretch
        self.y_end = self.y_end / self.stretch


        vector = self.start -self.end
        if vector[0] < 0:
            self.degree = -self.degree

        self.interpolate()
        self.draw()


    def interpolate(self):
        self.y_start = self.y_start + self.length/2 - self.w
        if self.length < -0.391*self.w +2* self.w:
            sys.exit(f'Length of Bracket is {self.length}, but may not be inferior to {-0.391*self.w +2* self.w} for a '
                     f'width of {self.w}')
        self.x_mid = np.linspace(self.x_start[-1], self.x_end[0], 10)[1:-1]
        self.y_mid = np.linspace(self.y_start[-1], self.y_end[0], 10)[1:-1]
        self.x = np.append(self.x_start, self.x_mid)
        self.x = np.append(self.x, self.x_end)
        self.y = np.append(self.y_start, self.y_mid)
        self.y = np.append(self.y, self.y_end)
        len = np.max(self.y) -np.min(self.y)
        self.y = self.y /len * self.length/2

        self.points = np.vstack((self.x, self.y)).T


        distance = np.cumsum( np.sqrt(np.sum( np.diff(self.points, axis=0)**2, axis=1 )) )
        distance = np.insert(distance, 0, 0)/distance[-1]

        alpha = np.linspace(0, 1, 150)

        interpolator =  interp1d(distance, self.points, kind='cubic', axis=0)
        interpolated_points = interpolator(alpha)
        self.interpolated_x = (interpolated_points.T)[0]
        self.interpolated_y = (interpolated_points.T)[1]
        self.interpolated_x = np.append(self.interpolated_x, np.flip(self.interpolated_x))
        self.interpolated_y = np.append(self.interpolated_y, np.flip(-self.interpolated_y))


    def draw(self):

        x = self.interpolated_x
        y = self.interpolated_y
        self.interpolated_x = x* np.cos(-self.degree) - y * np.sin(-self.degree)
        self.interpolated_y = x* np.sin(-self.degree) + y * np.cos(-self.degree)

        self.interpolated_x = self.interpolated_x + self.start[0] -self.interpolated_x[0]
        self.interpolated_y = self.interpolated_y + self.start[1] -self.interpolated_y[0]

        self.ax.plot(self.interpolated_x, self.interpolated_y, color = self.c, lw = self.lw, ls = self.ls, marker = '')
