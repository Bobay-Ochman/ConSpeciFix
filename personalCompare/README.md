# Personal Genome Comparison

A comparison method to determine if all genomes in a particular folder are a member of the same species. Produces a `results.txt` file in the folder with relevant output, and keeps all working files within a `_conspecifix` folder.

## The Easy Way

The important files:
- `config.py` defines several important variables that must be configered before any other steps.
- `runner.py` When run, completes an analysis for the strains located in the folder.

To run your folder comparison:

1. `git clone https://github.com/Bobay-Ochman/ConSpeciFix.git`
2. Edit path variables in `ConSpeciFix/personalCompare/config`
3. `cd ConSpeciFix/personalCompare`
4. `python runner.py`

## The Hard Way

Also the "by-hand" way, this is identical to the Database Mining processes described [here](https://github.com/Bobay-Ochman/ConSpeciFix/tree/forRelease/database), but starting with the `usearch` phase, skipping initial preparations.