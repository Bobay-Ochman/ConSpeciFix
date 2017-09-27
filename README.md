# Bacteria Speciation Process

A process that produces a database that, when tested against an instance of a bacteria, can determine with a certain confidence level whether or not the genome in question is a member of a particular species.

## Required Technologies

The following programs should be accessable from your command line, or else the path to the program specified in `config.py`

- python (everything is in python)
- gunzip
- wget
- usearch https://www.drive5.com/usearch/
- mcl https://www.micans.org/mcl/index.html
- mafft http://mafft.cbrc.jp/alignment/software/
- RAxML https://sco.h-its.org/exelixis/web/software/raxml/index.html

## Building the Database

The scripts to build the database are found in the `/scripts` folder

### The Easy Way

The important files:
- `config.py` defines several important variables that must be configered before any other steps.
- `species.py` populates `species.txt` with a list of all species in the NCBI database. Only species on this list will be run in the next step.
- `runner.py` takes this list and runs an analysis for that species to completion.

### The Hard Way

Also the "by-hand" way. This describes every script and what it does to complete the databse build.

### Preparing the data

- `species.py` creates species.txt with all species that will be applicable. (all the species with more than 15 complete genomes)
- `folders.py` Prepare one folder for each species. Within that folder, creates folders for other portions of the process, including `genes`, `genomes`, `align` and `BBH`.
- `download_*.py` Download genomes from NCBI into respective folders
    - `download_build.py` sets up the 'todo list' in `todo/*` containing all the download commands
    - `download_multi.py` initiates the downloads, pulling in all genomes of all species in species.txt
- `unzip.py` unzips the genomes
- Parse GFF
    - `parse_gff_build.py` makes a list in `todo/parse_gff.txt` with all parsing work that needs to be done
    - `parse_gff_multi.py`	creates multiple parallel processes to parse the gff files listed in 'todo/parse_gff.txt' through fasta files into the species' folder. We just utilize .fa

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

## Testing against the Database

Scripts for testing against the database can be found in `/web` as they were initially developed for the www.conspecifix.com website.

### Preparing the data (WEB)

- TODO: in the far future, we will have it test against the most likely species so we may make an informed guess. For now, it will simply be placed in `PATH_TO_OUTPUT/trial(trial number)/(genomeName).fa`
-

### Resampling analysis

- `USEACH` We will only need to usearch against the new genome in the set (O(n) rather than O(n^2))
    - `todo/usearch.txt` will instead be `PATH_TO_OUTPUT/trial(no.)/todo/usearch.txt`
    
- `parse_multiple_usearch.py` Finds the pair of orthologs genes
    - creates input for MCL in  `PATH_TO_OUTPUT/trial(no.)/input.txt`
    - This needs to be modified to match path, as well as copy from the origional data and simply add to input.txt
    
- `launch_mcl.py` Cluster orthologs into families
    - creates input for get_core in `PATH_TO_OUTPUT/trial(no.)/out.input_(sp).txt.I12`
    -Will need to be re-done for every trial upload. No previous work can be saved.

- `get_core.py` same as before, different paths.
    - generates output of core genomes and puts it in: `PATH_TO_OUTPUT/trial(no.)/orthologs.txt`
    - also puts all orthologs genes and corresponding ids into `PATH_TO_OUTPUT/trial(no.)/align/ortho(#)`

- MAFFT
    - `launch_mafft_build.py` builds a list in `PATH_TO_OUTPUT/trial(no.)/todo/mafft.txt`
    - `launch_mafft_multi.py` Align the core proteins with MAFFT.
        - produces output in `PATH_TO_OUTPUT/trial(no.)/align/(gene).align`
    
- `concat85.py` 
    - produces output in `PATH_TO_OUTPUT/trial(no.)/concat.fa`
    
- `raxml_distance.py`

- `sample.py` Remove nearly identical strains and generate random combinations of strains
    - will need some serious edditing to make properly functional for how it could best sample.
    - produces `sample.txt` and `family.txt`

- `calcHM.py`
