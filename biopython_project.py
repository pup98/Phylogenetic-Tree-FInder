
import Bio
from Bio import SeqIO
from Bio.SeqUtils import GC
import os 
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
from Bio import Phylo

# Code to get all the fasta files in the directory '''
file = [] 
dir = os.getcwd()
for filename in os.listdir(dir):
    if filename.endswith(('.fasta')):
        file.append(filename) # storing the list of files in a list
print('Found these list of files:', file)

# Code to handle the error in the input the user gives 

class Input_error(Exception):
    def __str__(self):
        return f'Numbering starts from 0, for the list of files. Give right file'

#Letting the user choose which fasta file he or she wants to use

user_input = int(input('Which file you want to use?\nGive input as number according to list above: '))
if user_input > len(file):
    raise Input_error

# Providing basic information about the file like length and GC content

print('Brief description about the content file ')
for seq_record in SeqIO.parse(file[user_input], 'fasta'):
    print(seq_record.description,', Length:', len(seq_record),', GC content: %.2f'%GC(seq_record.seq))

# Initializing the clustal object for fasta file to run the multiple allignment for phylogenetic analysis

clustalw_exe = r"C:/Program Files (x86)/ClustalW2/clustalw2.exe"
clustalw_cline = ClustalwCommandline(clustalw_exe, infile="p53_new.fasta")
assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
stdout, stderr = clustalw_cline()

# Reading the allignment using AlignIO tool of biopython and printing it

align = AlignIO.read('p53_new.aln', 'clustal')
print('\n', align)

# Printing the phylogenetic tree for the allignment '''

tree = Phylo.read('p53_new.dnd', 'newick')
print('Phylogenetic tree:')
Phylo.draw_ascii(tree)
