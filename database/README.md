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

- USEARCH
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

- `sample.py` Removes nearly identical strains and generates random combinations of strains. Generates:
	- `sample.txt` with all strains USED for the sampling
    - `family.txt` with all combinations of strains in sample.py of differing sizes. 
    - `removed.txt` with strains REMOVED for analysis for being drastically different or too similar.
	
- `calcHM.py` Computes h/m ratios across all the combinations of strains

### Graphing the data
- `graph.py` Generates the input files to generate the graphs
- `big_graph.py` Generates the script for R
- `big_graph.R` Generates the graphs

### Testing

The following scripts allow the Exclusion Criterion to run in order to identify strains that are sexually isolated from the other members of the species.

- `distrib.py` creates the distribution file
- `kmeans.py` creates the Rscript that identfies two modes in the distribution with a kmeans test and produces graphs of the distribution file, as well as `vector.txt` and `key.txt`.
- `split_kmeans.py` analyses the results of kmeans.py and produces `kmeans.txt`
- `kmeansGraph.py` generates Rscript that graphs the result of `kmeans.txt` and identifies outliers, outputing `kmeans.pdf` and `for_removal.txt`
- `criterion.py` writes the final results into `criterion.txt`