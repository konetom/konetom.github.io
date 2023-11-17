## Working with Biological Data

#### Read a FASTA file using BioPython:
```
from Bio import SeqIO

for record in SeqIO.parse("example.fasta", "fasta"):
    print(record.id)
    print(record.seq)

```
<br>


#### Count the frequency of each base in a DNA sequence:
```
def count_bases(dna):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in dna:
        counts[base] += 1
    return counts

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(count_bases(dna))

```
<br>


#### Count GC content of a DNA sequence:
```
def calculate_gc_content(seq):
    return (seq.count('G') + seq.count('C')) / len(seq)

dna_seq = "GCTAGCTAGCTAGCTAGCTA"
print(calculate_gc_content(dna_seq))

```
<br>


#### Count the Hamming distance between two DNA sequences:
```
def hamming_distance(seq1, seq2):
    return sum(base1 != base2 for base1, base2 in zip(seq1, seq2))

dna1 = "GAGCCTACTAACGGGAT"
dna2 = "CATCGTAATGACGGCCT"
print(hamming_distance(seq1, seq2))

```
<br>


#### Transcribe and translate DNA *in silico*
```
from Bio.Seq import Seq

# Create a sequence
dna_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# Transcribe the DNA sequence to mRNA
mRNA_seq = dna_seq.transcribe()
print("mRNA sequence:", mRNA_seq)

# Translate the mRNA sequence to a protein sequence
protein_seq = mRNA_seq.translate()
print("Protein sequence:", protein_seq)


```
<br>


#### Fetch gene info from NCBI database:
```
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your.email@example.com"  # Always tell NCBI who you are

handle = Entrez.efetch(db="nucleotide", id="600", rettype="gb", retmode="text")
record = handle.read()
handle.close()
print(record)
```
<br>


#### Fetch DNA sequence from NCBI database:
```
from Bio import Entrez, SeqIO

Entrez.email = "your.email@example.com"  # Always tell NCBI who you are

handle = Entrez.efetch(db="nucleotide", id="NC_005816", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

print(record.description)
print(record.seq)

```
<br>


### Additional links:
<a href src="https://prod.liveshare.vsengsaas.visualstudio.com/join?71BF9E85EE695EEF6EA86C2E53D5E6A06DED">See GitHub CodeSpace Live Share</a>
<br>

<a href src="https://www.programiz.com/python-programming/online-compiler">See online compilers</a>
