
# Agar file ose directory ma ha, ose level ma ha
f = open("example/e1.txt","w")

# read, write, append
# r   ,  w   ,  a (arguments)
f.write("I opened this file in a sub directory")
print(f.read())


# sub-directory ma ha
f2 = open("Code and Slides/example/a.txt","r")
print(f2.read())

f2.close()


# f3 = open("../Dummy Data.txt","r")
# print(f3.read())
# # f3.write("I made a fiel")

# f3.close()


# for i in "yahan koi sequence hona chahiya":
# for i in [1,2,3,4]:
#     #     i
#     #       i
#     #          i
#     print(i)

# print(type(range(4)))
# rage(4)
# 0 1 2 3 (4)

# print(list(range(c))


list_01 = [2,3,4]
#          0 1 2

# print(len(list_01)) -> 3
for i in range(len(list_01)): # 0 1 2 (3)
    print(list_01[i]) # O(1)
    
    
for i in range(4,4):
# for i in []:
    print(i)


def range(stop):
    pass

def range(start,stop):
    pass

def range(start,stop,step):
    pass


# 2 -> data-structure
# 3 -> leetcode

# for 30%