# Table Filler
Fills a SQL table from a CSV file.

Moves the mouse to press a button. Enters each item from the CSV with a tab between entries.
Presses the button after each row.

``` bash
usage: tableFiller.py [-h] [--test] [-n N] [--delay DELAY] tablefile location

Fill table from a CSV file.

positional arguments:
  tablefile             CSV file with the table.
  location              Location to move the mouse to. Top left corner of screen is 0_0, bottom right is 1919_1079. X axis is along
                        the top of the monitor, Y axis is along the left. eg: 100_100

optional arguments:
  -h, --help            show this help message and exit
  --test, -t            Test the mouse location and exit.
  -n N                  Number of rows to enter.
  --delay DELAY, -d DELAY
                        Delay between rows.
```