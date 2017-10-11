# Folder Comparison

A comparison method to determine if all genomes in a particular folder are a member of the same species. Produces a `results.txt` file in the folder with relevant output, and keeps all working files within a `_conspecifix` folder.

## The Easy Way

The important files:
- `config.py` defines several important variables that must be configered before any other steps.
- `runner.py` When run, completes an analysis for the strains located in the folder.

To run your folder comparison:

1. `git clone https://github.com/Bobay-Ochman/ConSpeciFix.git`
2. Edit path variables in `folderCompare/config`
3. `cd ConSpeciFix/folderCompare`
4. `python runner.py`

## The Hard Way

Also the "by-hand" way. This describes every script and what it does to complete the comparison.

### Resampling analysis

- USEACH
    - `usearch_build.py` makes a list in `todo/usearch.txt` with all usearch comparisons needing to be performed.
    - `usearch_multi.py` creates parallell processes to do the work listed by comparing all the genome pairs with eachother using USEARCH.
    
- `parse_multiple_usearch.py` Finds the pair of orthologs genes
    - creates input for MCL in  `PATH_TO_OUTPUT/(sp)/input.txt`
    
- `launch_mcl.py` Cluster orthologs into families
	- creates input for get_core in `PATH_TO_OUTPUT/(sp)/out.input_(sp).txt.I12`

- `get_core.py` Define the core genome at 85% and extract core proteins into the folder `PATH_TO_OUTPUT/(sp)/align/`
    - generates output of core genomes and puts it in: `PATH_TO_OUTPUT/(sp)/orthologs.txt`
	- also puts all orthologs genes and corresponding ids into `PATH_TO_OUTPUT/(sp)/align/ortho(#)`
	- also generates our list of `selectedSpecies.txt` which will be used for the rest of the process.

- MAFFT
    - `launch_mafft_build.py` builds a list in `todo/mafft.txt`
    - `launch_mafft_multi.py` Align the core proteins with MAFFT.
        - produces output in `PATH_TO_OUTPUT/(sp)/align/(gene).align`
    - `launch_mafft_verify.py` If MAFFT is killed mid-proceess, it will leave incomplete files in the database. To remove them and add the particular alignments back to the todo list, run this script.

- `concat85.py` Merges the core genes into a single alignment
	- produces output in `PATH_TO_OUTPUT/(sp)/concat.fa`
	
- `raxml_distance.py` Compute the distances between genomes with RAxML using the total genome listed in the `concat.fa`

- `sample.py` Remove nearly identical strains and generate random combinations of strains
	- produces `sample.txt` and `family_(sp).txt`
	
- `calcHM.py` Compute the h/m ratios across all the combinations of strains

### Graphing the data
- `graph.py` Generate the input files to generate the graphs
- `big_graph.py` Generate the script for R
- `big_graph.R` Generate the graphs

### Testing

Exclusion Criterion are defined in the following scripts and can be run in-order to produce a list of genomes not believed to be a member of the species.

- `distrib.py`
- `kmeans.py`
- `split_kmeans.py`
- `criterion.py`