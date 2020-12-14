"""
    çarpım tablosu kodu 
"""

# 10 kere dönen bir döngü 
for x in range(1,11):
    print(" ------------------- ")
    # 10 kere dönen bir - alt - döngü 
    for i in range(1,11):
        print( str(x) + " x " + str(i) + " = " + str( x * i ) )
