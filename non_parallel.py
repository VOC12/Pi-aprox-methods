import math 

def calculate_pi_nonparallel(N): #fuction that accepts N argument
    # N is the amount of division (rectangles) 
    #which are used to get aproach to the area under the curve
    delta_x = 1.0 / N #get the widhtr of each rectangle
    #divides 1 by hte total numner of rectangles(N)
    sum_area = 0 #variable that will store the cumulative sum of the areas of the rectangles
    for i in range(N): #loop that will iterate N times
    #Each iteration calculates the area of a rectangle and adds it to the total
        xi = i * delta_x #the x position of the left side of N
        fi = math.sqrt(1 - xi**2) #this is the value of the fucntion f(x)
        #which is the height of the rectangle at that position
        sum_area += fi * delta_x #multiply the height of N by its wiodt (area)
    return 4 * sum_area #multipies the total sum of all the area by 4 to obtain the Pi aprox


N = 100000
pi_approx1 = calculate_pi_nonparallel(N)
print(f"Approximated Pi by non-parallel: {pi_approx1}")
