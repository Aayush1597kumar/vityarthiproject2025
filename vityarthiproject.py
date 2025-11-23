# The program is a pomodoro technique that  help students to study affectively 
# In pomodora technique we study 25 minute 
# and take 5 minute brake and it continuously work for 4 cycle and then 15 minute brake  
# we have imported three module 


import datetime         
import time 
import winsound

# we have used datetime module here 

print("the clock starts at " )
Date_time=datetime.datetime.now()
print(Date_time)
print ("lets start the study ")


# we have defined a function that make a countdown timer
# we have used time module

def time_minute (z):
    for x in range (z*60,0,-1):
        second=x%60
        minute=int(x/60)%60
        print(f"00:{minute:02}:{second:02}")
        time.sleep(1)

# for repetation of same function we have used for loop 4 times 
# and used winsound library

for rep_cycle in range (4):
    time_minute(25)
    print ("its time to take a 5 minute break")
    winsound.Beep(9000,5000)                         # here (9000,5000) is a frequency of beeping sound 
    time_minute (5)
    print ("its a time to start again")
    winsound.Beep(9000,5000)



print("its a time to take a 15 minute brake" )
time_minute (15)
winsound.Beep(10000,5000)


print ("the clocks end at")
print(datetime.datetime.now())

# 1 cycle of pomodoro has completed now you can start the program again for and sit for another round  