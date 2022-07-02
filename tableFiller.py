import pyautogui
import csv
import argparse
import sys
from os.path import exists
from time import sleep

# Setup the arguments
parser = argparse.ArgumentParser(description='Fill table from a CSV file.', add_help=True, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('tablefile', help='CSV file with the table.')
parser.add_argument('location', help='''
	Location to move the mouse to. Top left corner of screen is 0_0, bottom right is 1919_1079. 
	X axis is along the top of the monitor, Y axis is along the left.
	eg: 100_100''')
parser.add_argument("--test",'-t', action='store_true', help='Test the mouse location and exit.')
parser.add_argument('-n', help='Number of rows to enter.')
parser.add_argument('--delay', '-d', help='Delay between rows.')

# Parse the arguments
args = parser.parse_args()

# Make sure the file exists
print(args.tablefile)
if(not exists(args.tablefile)):
	print("File does not exist")
	parser.print_help()
	sys.exit(1)

# Parse the x and y location
xLocation=args.location.split('_')[0]
yLocation=args.location.split('_')[1]

# Move the mouse to the location
print(pyautogui.size())
print("xLocation:", xLocation)
print("yLocation:", yLocation)
pyautogui.moveTo(int(xLocation), int(yLocation), duration = 1)

# Test the mouse location
if(args.test):
	sys.exit(0)

with open(args.tablefile, newline='') as csvfile:
	csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
	rowCount = 0
	for row in csvReader:

		# Exit after n rows
		if(args.n != None):
			if(rowCount == int(args.n)):
				sys.exit(0)
		rowCount = rowCount + 1

		# Click the location to add each row
		pyautogui.click(int(xLocation), int(yLocation))

		# Delay between rows
		if(args.delay != None):
			sleep(int(args.delay))
		else:
			sleep(0.1)

		print(row)

		for item in row:
			pyautogui.typewrite(item)
			pyautogui.keyDown('tab')
			sleep(0.01)
			pyautogui.keyUp('tab')
			sleep(0.1)

sys.exit(0)


