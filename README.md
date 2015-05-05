# BindIt
A small tool for searching many genome sequences for possible binding site sequence templates

Biologists looking for specific subsequence templates in large gene sequence data files often do so visually.
Finding many occurences of these certain sequences in a gene may lead to faster experimentation.

Bindit is a simple tool where researchers may specify datafiles and templates for potential subsequences that may occur in the data and can search the data for matches on these templates computationally.

## Example
A researcher hypothesizes that binding sites for a process may occur on certain genes with the following generic nucleotide sequence:

TCTG[0-4 of any character]CAGA

and the gene sequence data is thousands of lines of:

GTGGAGTGCTGAGGGACTCTGCCTCCAACGTCACCACCATCCACACCCCGGACACCCAGTGATGGGGGAGGATGGCACAGTGGTCAAGAGCACAGACTCTAGAGACTGTCAGAGCTGACCCCAGCTAAGGCATGGCACCGCT

Instead of searching by hand, they may instead specify the generic sequence as a list of subsequences:

TCTG,4,CAGA

BindIt will take this sequence, convert it to the appropriate regular expression and search all of the data for occurences matching this template.

###TODO:
* Breakdown of where matched sequences occured in the gene
* Print out how many matches in first 800 and after
* Match 1-edit-distance permutations of sequence templates, Only one wild card per entire sequence at a time
* Compatibility with filetypes other than docx
* Bindings to enumberable to eliminate the need for data in file form
