-- migration for adding categories of data types
ALTER TABLE `types_database_app_datatype` ADD COLUMN `category` varchar(180);
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="Plain Nucleotide Sequence";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="Protein paiwise alignment in fasta format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="DNA MSA in ClustalW Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="DNA MSA in ClustalX Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="DNA MSA in HTML Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="DNA MSA in Phylip Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="DNA Sequences in FASTA Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="Protein Plain Text Sequence";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="Protein Sequence in FASTA Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="RNA Sequence in FASTA Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="DNA Sequence in FASTA Format //";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="DNA Sequence in FASTA Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="CLUSTAL Multiple Sequence Alignments";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="RNA Sequences in FASTA Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="Plain Nucleotide Sequence";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="DNA sequence in FASTQ format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="DNA sequence in Stackholm format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="Protein Sequences in FASTA Format";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="Protein Sequence in PHYLIP Format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="RNA secondary structure vienna format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="RNA secondary structure in bpseq fomat";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in JME molecular Editor Format ";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Hyperchem format (HIN)";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="GROMACS Structure file";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="GAUSSIAN output format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Alchemy or Alchemy2000 format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Crystallographic Information File (CIF format)";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in XYZ format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in MOL2 format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in SDF format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in MOL V3000 format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in MOL V2000 format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Electron density map in sit format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="SAX data GNOM output";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="SAX raw data";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in ZINDO input format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in XYZ cartesian coordinates format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in XED format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in ViewMol format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in UniChem XYZ format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Alchemy format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in MSI BGF format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Dock 3.5 Box format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Ball and Stick format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Chem3D Cartesian 1 format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Chem3D Cartesian 2 format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Cacao Cartesian format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in CAChe MolStruct format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Cacao Internal format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Chemtool format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Gaussian 98/03 Cartesian Input";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Chemical Resource Kit diagram format (2D)";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Chemical Resource Kit 3D format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in CSD CSSR format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in ChemDraw Connection Table format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in DMol3 coordinates format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Protein Data Bank format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Feature format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Fenske-Hall Z-Matrix format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in SMILES FIX format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Fingerprint format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Free Form Fractional format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in GAMESS Input";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Ghemical format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in GROMOS96 format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in HyperChem HIN format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in InChI format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Jaguar input format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in MDL MOL format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in MacroModel format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Sybyl Mol2 format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in MOPAC Cartesian format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Sybyl descriptor format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in MPQC simplified input format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in NWChem input format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in PCModel Format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in POV-Ray input format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Parallel Quantum Solutions format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Q-Chem input format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Open Babel report format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in SMILES format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in TurboMole Coordinate format";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Structure in Tinker MM2 format";
UPDATE  `types_database_app_datatype` SET category="phylogenetic trees"  WHERE name="Phylogenetic tree in Newick format";
UPDATE  `types_database_app_datatype` SET category="phylogenetic trees"  WHERE name="Ttree information by GO ID";
UPDATE  `types_database_app_datatype` SET category="phylogenetic trees"  WHERE name="Phylogenetic Tree";
UPDATE  `types_database_app_datatype` SET category="phylogenetic trees"  WHERE name="Phylogenetic Tree in ClustalX Format";
UPDATE  `types_database_app_datatype` SET category="phylogenetic trees"  WHERE name="Phylogenetic Tree in Nexus Format";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Protein Substitution Matrix";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="BLAST Output in Tabular Format";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="BLAST Output in Flat Query-anchored Showing Identities Format";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="BLAST Output in Query-anchored Showing Identities Format ";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="BLAST Output in Pairwise Format";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Search ontology by function or gene name against GO database";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Search Records Against OMIM database";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Search lineages from multiple genera and species against INSD";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Search viruses against GIBV database";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Search features against GIBV database";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Search features against GTPS database";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="BLAST Output in XML Format";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Search entries by XML path aginst DDBJ";
UPDATE types_database_app_datatype SET name="Nucleotide BLAST complete result" WHERE name="Nucleotide BlastComplete";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Nucleotide BLAST complete result";
UPDATE types_database_app_datatype SET name="Nucleotide BLAST short result" WHERE name="Nucleotide BlastView";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Nucleotide BLAST short result";
UPDATE types_database_app_datatype SET name="Protein BLAST complete result" WHERE name="Protein BlastComplete";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Protein BLAST complete result";
UPDATE types_database_app_datatype SET name="Protein BLAST short result" WHERE name="Protein BlastView";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Protein BLAST short result";
UPDATE types_database_app_datatype SET name="Nucleotide BLAST short result with alignment" WHERE name="Nucleotide BlastAlignment";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="Nucleotide BLAST short result with alignment";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="DNA PDB Structure";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="Protein PDB Structure";
UPDATE  `types_database_app_datatype` SET category="structures, Structural biology"  WHERE name="PDB entry with Flat File Format by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="DDBJ entry with Flat File Format";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="Detailed feature information of a DDBJ entry";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="Related features between start and stop position in a DDBJ entry";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="Related features and DNA in a DDBJ entry";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="DDBJ entry with XML format";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="BLOCKS entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="DDBJ entry by clone information";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="DAD entry with Flat File Format by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="DDBJ contig entry with Flat File Format by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="DDBJ entry list by gene name";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="IMGT entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="DDBJ entry by locus information";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="PFAMA entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="PFAMB entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="PFAMHMMFS entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="PFAMHMMLS entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="PFAMSEED entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="DAD entry by protein ID";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="DDBJ entry by protein ID";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="PRF entry with flat file format by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="PRINTS entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="PRODOM entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="PROSITE entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="quality value of DDBJ entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="SWISSPFAM entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="SWISSPROT entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="TrEMBL entry by accession number";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="UNIPROT entry with Flat File Format by accession number";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="FASTA searches a protein or DNA sequence data bank";
UPDATE  `types_database_app_datatype` SET category="blast, homology and database searching"  WHERE name="VecScreen Search Results in HTML Format";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="CDS features of a chromosome ID";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="RefSeq Entry with Flat File Format";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="ENSEMBL Gene Information";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="ENSEMBL List of Genes on a Genome of Organism";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="NCBI Gene Information";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="NCBI List of Genes of Organism";
UPDATE  `types_database_app_datatype` SET category="Various database entries"  WHERE name="OMIM record";
UPDATE  `types_database_app_datatype` SET category="sequences, alignments"           WHERE name="Protein MSA in FASTA Format";















