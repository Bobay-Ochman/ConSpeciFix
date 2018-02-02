# Web Process Readme

The scripts for web-based analysis are located here. These were have been developed for the www.conspecifix.com website.

### Resampling analysis

- `USEARCH` We will only need to usearch against the new genome in the set (O(n) rather than O(n^2))
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