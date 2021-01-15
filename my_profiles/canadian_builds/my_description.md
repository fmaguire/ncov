# Canadian SARS-CoV-2 Evolutionary Analysis

Analyses performed thanks to data sharing by [GISAID](gisaid.org), 
data pre-processing and open-source tools from [nextstrain](nextstrain.org) ([augur](https://github.com/nextstrain/augur), [auspice](https://github.com/nextstrain/auspice), and [ncov workflow](https://github.com/nextstrain/ncov)
computing infrastructure from the [McArthur Lab](mcarthurbioinformatics.ca) (Michael G. DeGroote Institute for Infectious Disease Research, McMaster University).

## Highlighting Variants of Concern

This webpage (created by an [auspice](https://github.com/nextstrain/auspice) server) includes many useful ways of interactively visualising features of the dataset e.g., distribution of mutations across the SARS-CoV-2 genome, potential international and interprovincial transmission events, diversity within each province and so on.
All the plots above are interactive and navigable, and the bar on the left provides many options to filter the data and colour the evolutionary tree and map plots using a variety of metadata categories.
For example, to just show Canadian genomes, click on the "Filter Data" box in the left-bar and select "Country -> Canada".

The "UK" variant of concern (VOC) genomes in this representative subset of Canadian genomes (and global contextualising genomes) can be highlighted by filtering for "B.1.1.7", the "South African" VOC using "B.1.351", or the Brazilian VOC using "P.1", and "P.2".
Alternatively, if you follow this [link](http://auspice.finlaymagui.re/ncov/north-america/canada?f_country=Canada&f_pangolin_lineage=B.1.1.7,B.1.351,B.1.1.28) 
it will show a version of this page that is already filtered to highlight any public Canadian genomes with these mutations.

## Background: Going from Sample to Analysis

### Sequencing 

Sequencing RNA viruses is difficult because there is a lot of other RNA in humans (both from our own cells and potentially other RNA viruses).
This means when we extract RNA (and convert it to DNA for sequencing) and sequence it our data will only contain a very small amount of SARS-CoV-2 information (even in highly infected patients).
If we don't try to enrich the extracted SARS-CoV-2 genomes in our sample before we sequence, we will waste a lot of effort.
Therefore, we use a method called PCR (similar but distinct from the way PCR is used in diagnostic testing) which uses small "tags" matching SARS-CoV-2 to amplify the SARS-CoV-2 genomes in our sample.
Other methods do exist ([compared here](https://www.mdpi.com/1999-4915/12/8/895)) but PCR enrichment using the "[ARTIC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7480024/)" is the current gold-standard worldwide.

![A summary of different sequencing/enrichment methods for SARS-CoV-2](https://finlaymagui.re/assets/sequencing.png)

### Assembling Genomes 

Even with enrichment the data we get out of the sequencer may still contain some non-SARS-CoV-2 data (that just happened to be very similar to SARS-CoV-2 sequences).
Therefore, the first step of assembly workflows like [SIGNAL](https://github.com/jaleezyy/covid-19-signal) (used to assemble many of the Canadian genomes), is to remove any left-over sequences from the person/host that was swabbed.
If this isn't done errors can occur and we can't share the raw sequencing data in databases like [NCBI](https://www.ncbi.nlm.nih.gov/) or [EBI-ENA](https://www.ebi.ac.uk/ena/browser/home).
We do this by comparing the unassembled sequencing data to human genomes and viral genomes and then discarding any data that is more similar to the human genome.
The remaining sequencing data is then aligned to a viral reference genome and based on similarities and differences to that reference we recover the consensus genome and identify any variants (using tools like [iVar](https://github.com/andersen-lab/ivar)).
Finally, the resulting SARS-CoV-2 genomes are carefully analysed for any quality control issues.

![Overview of a SARS-CoV-2 genome assembly workflow](https://finlaymagui.re/assets/assembly.png)


### Performing Phylogeographic Analyses

The assembled SARS-CoV-2 genomes are uploaded to databases like [GISAID](https://www.gisaid.org/) along with accompanying tidy/consistent metadata needed for epidemiological analyses like this one.
Ideally, this metadata is organised following an international consensus [metadata specification](https://www.preprints.org/manuscript/202008.0220/v1), such as that developed by the Public Health Alliance For Genomic Epidemiology ([PHA4GE](https://pha4ge.org/)), and checked using tools like the [DataHarmonizer](https://github.com/Public-Health-Bioinformatics/DataHarmonizer).

The genomes and metadata from these databases is then analysed using customised versions of the Nextstrain [ncov workflow](https://github.com/nextstrain/ncov).
Briefly, data is automatically filtered to focus on the priority area and geographic scale for the analysis (e.g., global, national, provincial, or even finer-grained).
This identifies a subset of genomes that captures the evolutionary diversity in our area of interest (e.g., Canada) as well as genomes from the rest of the world that best contextualise these Canadian genomes.
A representative subset like this is used because it is easier to interpret, less computationally demanding, and ultimately enables timely and detailed epidemiological analysis.
During this stage additional quality control and filtering is performed to remove low quality and duplicate genomes.

The resulting genomes are then aligned to the reference genome so any changes/mutations in a specific part of SARS-CoV-2 line up with one another.
This alignment is then used to work out how different each of the genomes are from one another.
We then use tools like [IQ-Tree](http://www.iqtree.org/) to create models of the most likely way these genomes are related (i.e., an evolutionary tree or phylogeny).
This model is then further refined ([treetime](https://github.com/neherlab/treetime)) using metadata such as sample collection dates.
Potential transmission events or where and when certain mutations most likely appeared can then be predicted using this evolutionary model.
Finally, all of these analyses are visualised via [auspice](https://github.com/nextstrain/auspice) to allow interactive exploration of the results by epidemiologists and virologists.

![Augur/ncov phylogeographic analysis workflow](https://finlaymagui.re/assets/augur.png)


