import logging
from codetiming import Timer

t = Timer("example", text="Time spent: {:.2f}", logger=logging.warning)

t.start()

for i in range(0,1000):
    print("Selam")
    
t.stop()
