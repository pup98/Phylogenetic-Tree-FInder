# Phylogenetic-Tree-Finder
The *Biopython project* is an open-source collection of non-commercial Python tools for computational biology and bioinformatics, created by an international association of developers.[1][3][4] It contains classes to represent biological sequences and sequence annotations, and it is able to read and write to a variety of file formats. It also allows for a programmatic means of accessing online databases of biological information, such as those at NCBI. Separate modules extend Biopython's capabilities to sequence alignment, protein structure, population genetics, phylogenetics, sequence motifs, and machine learning. 

The program uses Biopython package and its inbuilt functions to give a phlogenetic tree as output. 

## **Steps are as follows:**

1. First block of code looks for fasta files in the directory, as the program requires a fasta file of many sequences for multiple sequence allignment.

2. It then appends all the fasta files into a list and asks the user which fasta file does he want to use. 

3. After taking the input it performs the MSA on the sequenes in the file using clustal tool provided by Biopython. To use this tool we have to install a executable file of the software and use as shown in the code. 

4. The ouptput of the clustal allignment is .aln file and .dnd file. Former is the allignement file and later one is a dendrogram file. 

5. We use Allign.IO tool module to read the allignments and Phylip to ouput the phylogenetic tree from the .dnd file. 
