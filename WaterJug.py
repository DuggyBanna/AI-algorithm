j1=int(input("Enter the capacity of jug 1:"))
j2=int(input("Enter the capacity of jug 2:"))
g=int(input("Enter the goal to be achieved:"))

def apply_rule(ch,x,y):
    if ch==1:
        if x<j1:
            return j1,y
        else:
            print("Rule cannot be applied")
            return x,y

    elif ch==2:
        if y<j2:
            return x,j2
        else:
            print("Rule cannot be applied")
            return x,y

    if ch==3:
        if x>0 and x+y<=j2:
            return 0,x+y
        else:
            print("Rule cannot be applied")
            return x,y

    if ch==4:
        if y>0 and x+y<=j1:
            return x+y,0
        else:
            print("Rule cannot be applied")
            return x,y

    if ch==5:
        if x>0 and x+y>=j2:
            return x-(j2-y),j2
        else:
            print("Rule cannot be applied")
            return x,y

    if ch==6:
        if y>0 and x+y>=j1:
            return x-(j1-x),j1
        else:
            print("Rule cannot be applied")
            return x,y
    if ch==7:
        if x>0:
            return 0,y
        else:
            print("Rule cannot be applied")
            return x,y

    if ch==8:
        if y>0:
            return x,0
        else:
            print("Rule cannot be applied")
            return x,y

    else:
        print("INVALID CHOICE")

x=y=0
while(True):
    if (x==g) or (y==g):
        print("Goal Achieved")
        break
    else:
        print("Rule 1:Fill jug 1")
        print("Rule 2:Fill jug 2")
        print("Rule 3:Transfer all water from jug1 to jug2")
        print("Rule 4:Transfer all water from jug2 to jug1")
        print("Rule 5:Transfer some water from jug1 to jug2 until jug2 is full")
        print("Rule 6:Transfer some water from jug2 to jug1 until jug1 is full")
        print("Rule 7:Empty jug1")
        print("Rule 8:Empty jug2")
        ch=int(input("Enter rule to apply:"))
        x,y=apply_rule(ch,x,y)
        print("=========================STATUS=========================")
        print("CURRENT STATE:",end=" ")
        print(x,y)
        
