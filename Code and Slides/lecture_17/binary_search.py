list_01 = [1,2,3,4,5,6,7,8,9,10]
target = 3
def binary_search():
    s = 0
    e = len(list_01)-1
   
   # [1 2 3 4]
   #  s m    e
   #      s  e
   #      m
    
    
    while s<=e:
        m = int((s+e)/2)
        
        # agar target values os index value sa match kr rehe ha
        if list_01[m] == target:
            return m
        
        # agar target value bre ha, matlab element right half ma ha, 
        if list_01[m]<target:
            s = m+1
            
        # ya khud hi jo ka last choice ha, matlab target value left half ma ha,
        else:
            e=m-1

print(binary_search())
    