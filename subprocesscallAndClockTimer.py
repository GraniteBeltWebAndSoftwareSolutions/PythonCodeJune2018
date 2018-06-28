
# import subprocess
import os
import time
# Control-c to quit Python
# this command line works too 
# os.system(r'C:\Users\Tim\Downloads\WinVICE-2.4-x64\WinVICE-2.4-x64\x64.exe')

def procedure():
    time.sleep(4.5) # time must be at least a few seconds or the Emulator 
                    # starts too quickly and makes the computeralmost crash
    print "WARNING! Don't leave program to run too long - Control-c to quit Python "
    st = os.startfile(r'C:\Users\Tim\Downloads\WinVICE-2.4-x64\WinVICE-2.4-x64\x64.exe')
    
    
# measure process time
t0 = time.clock()
procedure()
print (time.clock()), "seconds process time"

# measure wall time
while True:
    t0 = time.time()
    procedure()
    print (time.time()) - t0, "Seconds wall time"
    
