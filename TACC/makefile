EXECS=mpi_shell_task
MPICC?=mpicc

all: ${EXECS}

mpi_shell_task: mpi_shell_task.c
	${MPICC} -o mpi_shell_task mpi_shell_task.c

clean:
	rm -f ${EXECS}
