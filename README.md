# Bacteria Speciation Process

**For the most up-to-date _stable_ version of ConSpeciFix, please go to [releases](https://github.com/Bobay-Ochman/ConSpeciFix/releases).**

## About
An algorithm that detects bacterial and archaeal species based on the rates of gene flow across populations.

Bobay and Ochman. *Genome Biol Evol* 2017. 9(3): 491–501.

## Required Technologies

The following programs should be accessible from your command line (on your local path), or else the path to the program specified in `config.py`. Programs marked with a * must be on your local path.

- python*
- gunzip*
- wget*
- usearch https://www.drive5.com/usearch/
- mcl https://www.micans.org/mcl/index.html
- mafft http://mafft.cbrc.jp/alignment/software/
- RAxML https://sco.h-its.org/exelixis/web/software/raxml/index.html
- Rscript* https://cran.r-project.org/doc/manuals/r-release/R-admin.html

## Functionality

There are three variants of the current conspecifix process. They are:

- [**Analyze Your Own Genomes:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/master/personalCompare) for use on a single folder of genomes to determine if they are all the same species.
- [**Database Mining:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/master/database) used to build a large database of genomes. Initiates downloads and comparisons for species from NCBI, producing results similar to those found in our paper for the specified species.
- [**Web-based Database Comparison:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/master/web) A light-weight database comparison method designed for use in our website at www.conspecifix.com

## Personal Comparison

A comparison method to determine if all genomes in a particular folder are a member of the same species. Produces a `results.txt` file in the folder with relevant output, and keeps all working files within a `_conspecifix` folder. To run:

The important files:
- `config.py` defines several important variables that must be configured before any other steps.
- `runner_.py` When run, completes an analysis for the strains located in the folder.

To run your folder comparison:

1. Download the latest stable release from [our github](https://github.com/Bobay-Ochman/ConSpeciFix/releases).
2. Edit path variables in `ConSpeciFix-#.#.#/database/config`
3. `cd ConSpeciFix-#.#.#/database`
4. `python runner_personal.py /absolute/path/to/folder/with/genes/`

## Database Building

Produces a database of genomes, their comparisons, and result metrics for every species. Pulls data from NCBI.

The important files:
- `config.py` defines several important variables that must be configured before any other steps.
- `species.py` When run, this populates `species.txt` with a list of all species in the NCBI database. Only species on this list will be run in the next step.
- `runner_database.py` When run, takes this list and runs an analysis for that species to completion.

To produce your database:

1. download the most recent stable version [here](https://github.com/Bobay-Ochman/ConSpeciFix/releases)
2. Edit path variables in `ConSpeciFix-#.#.#/database/config`
3. `cd ConSpeciFix-#.#.#/database`
4. `python species.py`
5. Remove any unwanted species from `species.txt`
6. `python runner.py`

## Details

An explanation of every step in the pipeline is outlined in the README.md in the database folder.
