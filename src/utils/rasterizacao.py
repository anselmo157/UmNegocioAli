# -*- coding: utf-8 -*-
import turtle as tt
from PyQt5.QtCore import pyqtSlot, QObject
import math
import os

class Rasterizacao(QObject):

	def __init__(self):
		QObject.__init__(self)

	@pyqtSlot()
	def algoritimoBresenham(self):
		
		arrayPontos = [
			[0, 0],
			[20,0],
			[10,20],
			[0,20]
		]

		for i in range(len(arrayPontos)):
			
			x0 = arrayPontos[i][0]
			y0 = arrayPontos[i][1]
			try:
				x1 = arrayPontos[i+1][0]
				y1 = arrayPontos[i+1][1]
			except IndexError:
				x1 = arrayPontos[0][0]
				y1 = arrayPontos[0][1]
			
			dx = abs(x1 - x0)
			dy = abs(y1 - y0)
			x, y = x0, y0
			sx = -1 if x0 > x1 else 1
			sy = -1 if y0 > y1 else 1
			if dx > dy:
				err = dx / 2.0
				while x != x1:
					print(x,y)
					# set_pixel(x,y)
					err -= dy
					if err < 0:
						y += sy
						err += dx
					x += sx
			else:
				err = dy / 2.0
				while y != y1:
					print(x,y)
					# set_pixel(x,y)
					err -= dx
					if err < 0:
						x += sx
						err += dy
					y += sy

			print(x,y)
			# set_pixel(x,y)