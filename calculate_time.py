#!/usr/bin/env python3
seconds = int (input("Please enter the remaining time for the deadline in seconds: \n"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remained_seconds = seconds % 60
print(f"For the deadline, the remained time is: {hours} hours, {minutes} minutes, and {remained_seconds} seconds.")
