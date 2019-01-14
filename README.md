# ConSpeciFix: a Speciation Process

**For the most up-to-date _stable_ version of ConSpeciFix, please go to [releases](https://github.com/Bobay-Ochman/ConSpeciFix/releases).**

## About
An algorithm that detects bacterial and archaeal species based on the rates of gene flow across populations. Has also been used with good results on viral species.

Bobay and Ochman. *Genome Biol Evol* 2017. 9(3): 491–501.

## Required Technologies

The following programs should be accessible from your command line (on your local path), or else the path to the program specified in `config.py`. Programs marked with a * must be on your local path.

- python* (must call python 2.7 from typing 'python')
	- numpy (optional, used to generate maps of recombination across genome)
	- matplotlib (optional, same as above)
- gunzip* (used in database building)
- wget* (used in database building)
- usearch https://www.drive5.com/usearch/ (v.6.1)
- mcl https://www.micans.org/mcl/index.html
- mafft http://mafft.cbrc.jp/alignment/software/
- RAxML https://sco.h-its.org/exelixis/web/software/raxml/index.html
- Rscript* https://cran.r-project.org/doc/manuals/r-release/R-admin.html
	- outliers package, installed by running `install.packages('outliers')` in R.

## Functionality

There are three variants of the current conspecifix process. They are:

- **Analyze Your Own Genomes:** for use on a single folder of genomes to determine if they are all the same species.
- **Database Mining:** used to build a large database of genomes. Initiates downloads and comparisons for species from NCBI, producing results similar to those found in our paper for the specified species.
- **Web-based Database Comparison:** A light-weight database comparison method designed for use in our website at www.conspecifix.com

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

An additional flag can be added `-t` to limit the number of threads. The default is the number of cores on the machine, but can be changed like this:
```
python runner_personal.py -t 4 /absolute/path/to/folder/with/genes/
```


### Test Data

Test data sets and examples of completed analysis can be found [here](https://github.com/Bobay-Ochman/Test-Data)

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
6. `python runner_database.py`

## Analyzing Results

See [our website](http://www.conspecifix.com/#!/results).

## Details

An explanation of every step in the pipeline is outlined in the README.md in the database folder.
