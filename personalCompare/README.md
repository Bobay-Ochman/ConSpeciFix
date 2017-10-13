# Folder Comparison

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

Also the "by-hand" way. This describes every script and what it does to complete the comparison.

### Resampling analysis

- USEACH
    - `usearch_build.py` makes a list in `todo/usearch.txt` with all usearch comparisons needing to be performed.
    - `usearch_multi.py` creates parallell processes to do the work listed by comparing all the genome pairs with eachother using USEARCH.
    
- `parse_multiple_usearch.py` Finds the pair of orthologous genes
    - creates input for MCL in  `PATH_TO_OUTPUT/(sp)/input.txt`
    
- `launch_mcl.py` Clusters orthologs into families
	- creates input for get_core in `PATH_TO_OUTPUT/(sp)/out.input_(sp).txt.I12`

- `get_core.py` Defines the core genome at 85% and extracts core proteins into the folder `PATH_TO_OUTPUT/(sp)/align/`
    - generates output of core genomes and puts it in: `PATH_TO_OUTPUT/(sp)/orthologs.txt`
	- also puts all orthologous genes and corresponding ids into `PATH_TO_OUTPUT/(sp)/align/ortho(#)`
	- also generates our list of `selectedSpecies.txt` which will be used for the rest of the process.

- MAFFT
    - `launch_mafft_build.py` builds a list in `todo/mafft.txt`
    - `launch_mafft_multi.py` Align the core genes with MAFFT.
        - produces output in `PATH_TO_OUTPUT/(sp)/align/(gene).align`
    - `launch_mafft_verify.py` If MAFFT is killed mid-proceess, it will leave incomplete files in the database. To remove them and add the particular alignments back to the todo list, run this script.

- `concat85.py` Merges the core genes into a single alignment
	- produces output in `PATH_TO_OUTPUT/(sp)/concat.fa`
	
- `raxml_distance.py` Computes the distances between genomes with RAxML using the genomes listed in `concat.fa`

- `sample.py` Removes nearly identical strains and generates random combinations of strains
	- produces `sample.txt` and `family_(sp).txt`
	
- `calcHM.py` Computes h/m ratios across all the combinations of strains

### Graphing the data
- `graph.py` Generates the input files to generate the graphs
- `big_graph.py` Generates the script for R
- `big_graph.R` Generates the graphs

### Testing

The following scripts allow the Exclusion Criterion to run in order to identify strains that are sexually isolated from the other members of the species.

- `distrib.py`
- `kmeans.py`
- `split_kmeans.py`
- `criterion.py`