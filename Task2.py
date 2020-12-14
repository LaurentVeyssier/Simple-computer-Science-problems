"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phone = time = 0
time_over_phone = {}
"""for call in calls:
    if call[0] in time_over_phone.keys():
        time_over_phone[call[0]]+=int(call[3])
    else:
        time_over_phone[call[0]]=int(call[3])
    
    if call[1] in time_over_phone.keys():
        time_over_phone[call[1]]+=int(call[3])
    else:
        time_over_phone[call[1]]=int(call[3])"""

# more efficient alternative: use .get() method, initiate with 0 if key does not exist
for i in range(len(calls)):
    time_over_phone[calls[i][0]] = time_over_phone.get(calls[i][0],0)+int(calls[i][3])
    time_over_phone[calls[i][1]] = time_over_phone.get(calls[i][1],0)+int(calls[i][3])


phone = max(time_over_phone, key=time_over_phone.get)
time = time_over_phone[phone]       

print(f'{phone} spent the longest time, {time} seconds, on the phone during September 2016.')

