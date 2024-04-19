from multiprocessing import Pool
import numpy as np
from workers import worker
"""
def f(x): #function f(x) which descirbes the cuarter of the curve
    #the result f(x) for the height of N at x position
    return np.sqrt(1 - x**2)

def worker(args): #thos function takes xi y get the area of N in the position usiong tuples
    xi, delta_x = args #nnpack the tuple
    return f(xi) * delta_x #get the area of N in xi position multiplying the high by the wid
    #f(xi) altura
    #delta_x ancho
"""
def parallel_calculate_pi(N): #functio for pi in parallel
    delta_x = 1.0 / N
    pool = pool = Pool() #process, allows several ionstances of the paralleler
    xi_values = [(i * delta_x, delta_x) for i in range(N)]
    #tuiple of xi values, each one represents tje x position of the left sdie
    areas = pool.map(worker, xi_values) #assign the tasks for calculate the area 
    #for each value of xi
    pool.close() #dont allow more tasks
    pool.join() #make to wait trhat all the process comple their tasks
    return 4 * sum(areas) #obtain the Pi aprox


if __name__ == '__main__':#Conditional that checks if the script is being executed directly (not imported as a module)
    N = 100000 
    pi_approx = parallel_calculate_pi(N)
    print(f"Approximated Pi (Parallel): {pi_approx}")
