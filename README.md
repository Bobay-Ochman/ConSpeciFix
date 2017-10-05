# Bacteria Speciation Process

A process that produces a database that, when tested against an instance of a bacteria, can determine with a certain confidence level whether or not the genome in question is a member of a particular species.

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

There are four variants of the current conspecifix process. They are:

- [**Folder Comparison:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/master/folderCompare) for use on a single folder of genomes to determine if they are all the same species.
- [**Database Building:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/master/scripts) used to build a large database of genomes. Downloads, compares, and produces results for several species.
- [**Web-based Database Comparison:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/master/web) A light-weight database comparison method designed for use in our website at www.conspecifix.com
- [**TACC:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/master/TACC) Some scripts for variants on compute clusters in the Texas Advanced Computing Center

These are all found in their respective folders with respective README files to describe specific functions.