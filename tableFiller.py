import pyautogui
import csv
import argparse
import sys
from os.path import exists
from time import sleep
import signal

# Catch ctrl-c
def handler(signum, frame):
    print()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

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
parser.add_argument('-p', action='store_true', help='Print mouse position.')
parser.add_argument('-s', help='Seek to this entry')

# Parse the arguments
args = parser.parse_args()

# Print the mouse position
if(args.p):
    while(1):
        print(pyautogui.position())
        sleep(1)

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

        # Seek to entry s
        if(args.s != None):
            if(rowCount < int(args.s)):
                rowCount = rowCount + 1
                continue

        # Exit after n rows
        if(args.n != None):
            endCount = int(args.n)

            # Account for the seek 
            if(args.s != None):
                endCount = endCount + int(args.s)
            
            if(rowCount == endCount):
                sys.exit(0)


        # Click the location to add each row
        pyautogui.click(int(xLocation), int(yLocation))

        # Delay between rows
        if(args.delay != None):
            sleep(float(args.delay))
        else:
            sleep(0.01)

        print(row)

        for item in row:
            pyautogui.typewrite(item)
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')

        rowCount = rowCount + 1

sys.exit(0)


