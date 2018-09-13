## Files in Export:

- `stampede2.zip` contains all programs and scripts to run the analysis
- `databaseQuerySpecies.zip` is an example of the output
- `websiteOutput.zip` is the databank to compare against. Contains only the ten genomes needed for the comparison and other necessary files. 

## How to run the experiment:

A note on notation: `zipFileName->file/path/within.txt`

1) A todo list is built by running the script `stampede2->ConSpeciFix/databaseQuery/runner_build.py`. This produces a todo list in: `stampede2->ConSpeciFix/databaseQuery/todo/runner.txt`.

2) The multiprocessing is kicked off by initiating an MPI job. On TACC, this is done by submitting the job `parent_shell_task.slurm` to the TACC queue. The salient result of this is that `mpi_shell_task.c` launched once on every machine with two important arguments taken care of:
  - world_size (this is the same for everyone, and represents the total number of machines running)
  - world_rank (this is unique for everyone, and can be used as an ID.)

3) `mpi_shell_task` during its execution calls `python_shell_task.py` once on every computer, which prints some debug output and then calls `stampede2->ConSpeciFix/databaseQuery/runner_multi.py`.

4) `runner_multi.py` creates its own sub todolist of jobs to complete. This list will have every job with the index `n*W+R`, where `W` is world size, `R` is rank, and `n` is a positive integer. With this sub-todo list, it then figures out how many threads it has to work with (on TACC, this was 272 because each node was very powerful) and uses python's multiprocessing library to manage launching the one job for each thread. It launches several instances of the function `runTrial`.

5) Each `runTrial()` is called with the arguments of a specific todo-list item (a specific comparison to run). This function moves the test files into the correct locations, prints some debug information, and then calls `stampede2->ConSpeciFix/databaseQuery/web/runner.py` to begin the actual analysis.


## Changes
Files that will *need* to be changed:
- Most files within `stampede2->TACCRunner`
	- `python_shell_task.py` will need a new scriptDir. Additionally, for testing, the call of `os.system` can be removed to inspect ids and world ranks are all being called. An example of this happening properly is in `out/shell_task.1402559.out`
	- `mpi_shell_task.c` should be stable assuming the MPI installation is similar 
	- `parent_shell_task.slurm` will need to be changed completely to match your new systems job submittal form.
- `stampede2->ConSpeciFix/databaseQuery/web/config.py` -> The locations of programs and relative paths will all need to be adjusted to sit properly on longleaf
- `stampede2->ConSpeciFix/databaseQuery/config.py` -> will not need all the programs, but will need new paths to database scripts, etc.

