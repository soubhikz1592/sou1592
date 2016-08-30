import math
z=0;
for x in range(100,200):
        for y in range(2,int(math.sqrt(x))):
            if ((x%y)==0):
                #z=z+1;
                #print z;
                break;
        else:  
            z=0;
            print (x);

    
