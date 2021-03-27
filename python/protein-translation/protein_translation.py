from textwrap import wrap

codons_map = {'AUG':'Methionine',
            'UUU':'Phenylalanine',
            'UUC':'Phenylalanine',
            'UUA': 'Leucine', 
            'UUG': 'Leucine',
            'UCU': 'Serine',
            'UCC': 'Serine',
            'UCA': 'Serine',
            'UCG': 'Serine',
            'UAU':'Tyrosine',
            'UAC':'Tyrosine',
            'UGU': 'Cysteine',
            'UGC': 'Cysteine',
            'UGG':'Tryptophan'}

stop_codons = ['UAA', 'UAG', 'UGA' ]


def proteins(strand):
    
    protein = []
    for codon in wrap(strand,3):
        if codon in stop_codons: break
        protein.append(codons_map[codon])
    
    return protein
    


