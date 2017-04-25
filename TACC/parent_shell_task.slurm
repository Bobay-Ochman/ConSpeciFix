#!/bin/bash


#----------------------------------------------------
# Generic SLURM script -- MPI Hello World
#
# This script requests 2 nodes and all 16 cores/node
# for a total of 32 MPI tasks.
#----------------------------------------------------
#SBATCH -J shell_task          # Job name
#SBATCH -o out/shell_task.%j.out   # stdout; %j expands to jobid
#SBATCH -e out/shell_task.%j.err   # stderr; skip to combine stdout and stderr
#SBATCH -p development    # queue
#SBATCH -N 2              # Number of nodes, not cores (16 cores/node)
#SBATCH -n 2              # Total number of MPI tasks (if omitted, n=N)
#SBATCH -t 00:30:00       # max time (HH:MM:SS)

#SBATCH --mail-user=brian.ellis@utexas.edu
#SBATCH --mail-type=ALL

#SBATCH -A Ape_Microbiomes       # class project/account code;
                          # necessary if you have multiple project accounts

ibrun ./mpi_shell_task        # Use ibrun only for MPI codes. Don't use mpirun or srun.
                        # Do not add "-n" or "-np" options here. SLURM infers the
                        # process count from the "-N" and "-n" directives above.