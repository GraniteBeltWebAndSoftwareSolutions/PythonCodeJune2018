
# import subprocess
import os
import time

# os.system(r'C:\Users\Tim\Downloads\WinVICE-2.4-x64\WinVICE-2.4-x64\x64.exe')

def procedure():
    time.sleep(3.5)
    st = os.startfile(r'C:\Users\Tim\Downloads\WinVICE-2.4-x64\WinVICE-2.4-x64\x64.exe')
    
    
# measure process time
t0 = time.clock()
procedure()
print time.clock(), "seconds process time"

# measure wall time
while True:
    t0 = time.time()
    procedure()
    print time.time() - t0, "Seconds wall time"
    
