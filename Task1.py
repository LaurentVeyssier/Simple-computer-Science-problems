"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

from collections import Counter
count = Counter()
for text in texts:
    count.update((text[:2]))
for call in calls:
    count.update((call[:2]))
    
print(f'There are {len(count)} different telephone numbers in the records.')