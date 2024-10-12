# MatchCase is SwitchCase
# Break is not required in pyhton
x = int(input('=>'))
match x:
    case 1:
        print('X is 1')
    case 2:
        print('X is 2')
    case 3:
        print('X is 3')
    case _:  # '_' means default case 
        print('X is', x)
        
# case _ if(x>90):    #can be writtern like this too
#     print("   ")