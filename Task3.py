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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
import re

def is_bangalore(phone):
    if re.search(r'(080)', phone) is None:
        return False
    else:
        return True
    
def not_telemarketer(phone):
    if re.search(r'^140', phone) is None:
        return True
    else:
        return False

def get_code(phone):
    match = re.search('^\(0\d+\)', phone)
    if match is not None:
        return match.group()
    
    match = re.search(r'^(7|8|9)\d+\s', phone)
    if match is not None:
        return match.group()[:4]  # return the first 4 digits only (task A)

list_of_codes = set()
count_from = count_to = 0

for call in calls:
    if is_bangalore(call[0]):
        # track calls issued from landline Bangarole (task B)
        count_from += 1
         
        if not_telemarketer(call[1]):
            list_of_codes.add(get_code(call[1]))
            
            # track landline to landline bangalore calls (task B)
            if is_bangalore(call[1]):
                count_to += 1   

print('The numbers called by people in Bangalore have codes:')
for code in sorted(list_of_codes):
    print(code)

percentage = count_to / count_from * 100

print(f'{percentage:.02f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')