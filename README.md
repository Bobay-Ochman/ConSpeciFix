# Bacteria Speciation Process

An algorithm that detects bacterial and archaeal species based on the rates of gene flow across populations.

Bobay and Ochman. *Genome Biol Evol* 2017. 9(3): 491–501.

## Required Technologies

The following programs should be accessable from your command line (on your local path), or else the path to the program specified in `config.py`. Programs marked with a * must be on your local path.

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

- [**Analyze Your Own Genomes:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/forRelease/personalCompare) for use on a single folder of genomes to determine if they are all the same species.
- [**Database Mining:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/forRelease/database) used to build a large database of genomes. Initiates downloads and comparisons, producing results for several species.
- **Web-based Database Comparison:** A light-weight database comparison method designed for use in our website at www.conspecifix.com. Not in the standard release.

These are all found in their respective folders with respective README files to describe specific functions.