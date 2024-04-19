from mpi4py import MPI
import numpy as np

def distributed_calculate_pi(N): #fuction that accepts N argument
    # N is the amount of division (rectangles) 
    comm = MPI.COMM_WORLD #communicator for all running processes
    rank = comm.Get_rank() #get the rank (unic id) 
    size = comm.Get_size() #get the total size of the communicator
    # size= amount of process in progress
    
    delta_x = 1.0 / N
    local_n = N // size #the number of local divisions per process
    local_sum = 0.0 #sum storage
    
    #Loop that iterates over the range of rectangle 
    #indices to be calculated by the current process
    for i in range(rank * local_n, (rank + 1) * local_n):
        xi = i * delta_x
        local_sum += np.sqrt(1 - xi**2) * delta_x
    
    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
    if rank == 0: #chekc if the current process is the root process
        return 4 * total_sum
    return None #non-root processes return None

N = 100000
pi_approx3 = distributed_calculate_pi(N)
if pi_approx3 is not None:
    print(f"Approximated Pi (Mpi4py): {pi_approx3}")
