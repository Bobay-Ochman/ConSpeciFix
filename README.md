# Bacteria Speciation Process

A process that produces a database that, when tested against an instance of a bacteria, can determine with a certain confidence level whether or not the genome in question is a member of a particular species.

## Building the Database

### Preparing the data
probably something about downloading the NCBI cataloge that lists what all they have.
- `species.py` creates species.txt with all species that will be applicable. (all the species with more than 15 complete genomes)
- `folders.py` Prepare one folder for each species. Within that folder, creates folders for other portions of the process, including `genes`, `genomes`, `align` and `BBH`.
- `download.py` Download genomes from NCBI into respective folders
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
    
- `concat85.py` Merges the core genes into a single alignment
	- produces output in `PATH_TO_OUTPUT/(sp)/concat.fa`
	
- `raxml_distance.py` Compute the distances between genomes with RAxML using the total genome listed in the `concat.fa`

- `sample.py` Remove nearly identical strains and generate random combinations of strains
	- produces `sample.txt` and `family.txt`
	
- `calcHM.py` Compute the h/m ratios across all the combinations of strains

### Graphing the data
- `graph.py` Generate the input files to generate the graphs
- `big_graph.py` Generate the script for R
- `big_graph.R` Generate the graphs

### Testing

Exclusion Criterion

- `distrib.py`
- `kmeans.py`
- `split_kmaens.py`
- `criterion.py`


## Testing against the Database

### Preparing the data

- TODO: in the far future, we will have it test against the most likely species so we may make an informed guess. For now, it will simply be placed in `PATH_TO_OUTPUT/trial(trial number)/(genomeName).fa`
- This negates any pre-processing of the data, and we can jump right in to the number crunching.

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
