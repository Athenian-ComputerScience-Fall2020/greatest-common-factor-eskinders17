# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def find_gcf(x,y):   # Do not change function name!
    # User code goes here
    if x > y:
        x, y = y, x
    for gcf in range (x, 0, -1):
        if x % gcf == 0 and y % gcf == 0:    

          return gcf


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    
    print(find_gcf(30,15))

    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

