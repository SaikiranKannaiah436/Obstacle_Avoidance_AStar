<<<<<<< HEAD
#!/usr/bin/env python3
=======
#!/usr/bin/env python
>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57
import rospy
import subprocess
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion

import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
import csv
<<<<<<< HEAD
import AStar_Grid3
from AStar_Grid3 import *
import pygame
=======
>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57


#global occList	
#occList = []

def callback(data):
	occupancyMap = data.data
#	print(occupancyM

	occList = []
	occList.append(occupancyMap)
	print("c")

<<<<<<< HEAD

	out = open('/home/viki/rosRoboticsByExample_WS/src/astar_ttbot/rrl_custom_small_map_data.txt', 'w')
	for row in occList:
		for column in row:
			out.write('%d,' % column)
		out.write('\n')
	out.close()
=======
	out = open('/home/akshaybajaj/catkin_ws/src/astar_ttbot/rrl_custom_small_map_data.txt', 'w')
	for row in occList:
		for column in row:
        		out.write('%d,' % column)
    		out.write('\n')
	out.close()
	
>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57

def callback2(data):
	res = data.resolution
	w = data.width
	h = data.height
	o = data.origin

	mapData = []
<<<<<<< HEAD
	mapData.append(res)
	mapData.append(w)
	mapData.append(h)
=======
	mapData.append(res)	
	mapData.append(w)
	mapData.append(h)	
>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57
	mapData.append(o)

#	print("global occList from callback 1: ", occList)

#	rate = rospy.rate(10)
#	while not rospy.is_shutdown():
#		self.callback_pub.publish(data)	
#		rate.sleep()

	print("res: ",res, "     W: ", w, "    H: ", h)
#	print( "o: ")
#	print(self.o)
#	print("occupancy Map: ", self.xyz)
	

#def function1():
#	print(occList)


def gridConversion():
#	print(self.res)
	
<<<<<<< HEAD
#	files = open("/home/viki/rosRoboticsByExample_WS/src/astar_ttbot/rrl_custom_small_map_data.txt", "r")
	files = open("/home/viki/rosRoboticsByExample_WS/src/astar_ttbot/mapData.txt", "r")
	
=======
	files = open("/home/akshaybajaj/catkin_ws/src/astar_ttbot/rrl_custom_small_map_data.txt", "r")
>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57
	lines = files.readlines()
	files.close()
	
	lines = lines[0]
#	print(lines)

#	lines = lines[0:len(lines)-2] #removing garbage value present at the end of the list (in string form)
	
<<<<<<< HEAD
#	lines = lines.split(",")
	lines = lines.split(" ")

#	print(lines)

	lines = [x for x in lines if x != '\n'] #remove all ','
#	lines = [x for x in lines if x != ']'] #remove all ' '
	lines = [x for x in lines if x != ''] #remove all '''
	lines = [x for x in lines if x != ' '] #remove all '''

#	print(lines)
	lines = list(map(int, lines))	#converting string elements in the list to int
#	print(lines)

=======
	lines = lines.split(",")

#	lines = [x for x in lines if x != '\n'] #remove all ','
#	lines = [x for x in lines if x != ']'] #remove all ' '
	lines = [x for x in lines if x != ''] #remove all '''

	lines = list(map(int, lines))	#converting string elements in the list to int
#	print(lines)

	print(len(lines))
>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57
#	print(lines[16653])

#	lines = lines[0:278528] #reduce the size to toal grid elements
			
#	print("lines After removing things: ", lines)
<<<<<<< HEAD
	print(len(lines))

	# Made a grid of 512*544
	totalRow = 512
	'''		
	i=0
	while (i < totalRow):
		j = 0
		while (j < totalCol):
			row.append(lines[j])
=======

	# Made a grid of 512*544
	row = []
	grid = []
	totalRow = 512
	totalCol = 544
		
	i=0
	while (i < totalRow):	
		j = 0
		while (j < totalCol):
			row.append(lines[i])
>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57
			j+=1
		grid.append(row)			
		row = []
		i += 1
<<<<<<< HEAD
	'''

	row = []
	grid = []
	totalCol = 544
	count = 0

	for i in lines:
		count += 1
		row.append(i)

		if ((count%totalRow) == 0):
			grid.append(row)
			row = []

#	print(len(grid), ": ", len(grid[511]))
#	print(grid)
=======

>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57
#	nodeList = []
#	print("nodelist", nodelist)

#	print(grid[2])
#	count = 0
#	for i in grid:
#		count+=1
#		for j in grid[count]:
#			nodeList.append((i,j))		
#		print(nodeList)

	return grid

	'''
	occW = []
	occH = []
	count = 0

	for i in occupancyMap:
		count+=1
		if (count <= w):
			accW.append(i)
		if (count > w):
			accH.append(i)
	
	print("Width List: ", accW)
	print("Height List: ", accH)
	'''
<<<<<<< HEAD
	

grid = gridConversion()
#print(grid)
#		print(len(grid[0]))
z = 0
for i in grid:
	print("Row: ", z)
	print(i)	
	z += 1

#Convert grid into list of tuples:
finalMap = []
row =0
col =0
for i in grid:
	row += 1
	col = 0
	for j in i:
		col += 1
		finalMap.append((row-1, col-1, j))


obstaclePoints = []
print(obstaclePoints)

for i in finalMap:
	if (i[2] == 0):
		obstaclePoints.append((i[0],i[1]))

print(obstaclePoints)
#print(finalMap)
#for i in finalMap:
#	if (i[2] != -1):
#		print(i)
#print(len(finalMap))



# Calling A Star Algorithm
completeTable = aStar(obstaclePoints)
print(" ")
print(completeTable)
# Getting nodes for final Path from the table
finalNode = G
n = []
n.append(G)
print(" DONE ")

while(finalNode != x1):
    temp = completeTable[finalNode][4]
    n.append(temp)
    finalNode = temp
=======

>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57



if __name__ == '__main__':
	try:
<<<<<<< HEAD

=======
#		global occList
		
>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57
		rospy.init_node('map_listener', anonymous=True)	#initialze node named"map_listener"

		rospy.Subscriber("/map", OccupancyGrid, callback) #subscribe to /map	

		rospy.Subscriber("/map_metadata", MapMetaData, callback2)  #subscribe to /map_metadata
<<<<<<< HEAD
=======
		
		grid = gridConversion()
		print(grid)

>>>>>>> a4739d82d2fc215e5df2219f26ab10e21f002f57

		rospy.spin()   # spin() simply keeps python from exiting until this node is stopped


	except rospy.ROSInterruptException:
		pass
