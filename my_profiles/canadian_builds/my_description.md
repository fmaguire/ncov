# Canadian SARS-CoV-2 Evolutionary Analysis

An evolutionary and geographic analysis of all Canadian genome sequences in [GISAID](https://www.epicov.org/epi3/frontend#596041) (as of December 22nd). 
While it is theoretically possible to analyse every sequenced SARS-CoV-2 genome from the entire world (282,538 as of December 22nd) [simultaneously](https://github.com/roblanf/sarscov2phylo), this is very computationally intensive 
and complicates timely and detailed epidemiological analysis.
Therefore, we use Nextstrain's [augur](https://github.com/nextstrain/augur) tool and [ncov workflow](https://github.com/nextstrain/ncov) to subsample these sequences in a way that prioritises including genomes from our area of interest
(e.g., Canada) and genomes from the wider world that help us contextualise our genomes of interest.
These tools also enable removal of low quality or duplicate genomes taking us from 282,538 input genomes to 7,863 genomes (2,418 from Canada with 5,445 genomes from the rest of the world as context).

These analyses are then visualised in Nextstrain's [auspice](https://github.com/nextstrain/auspice) which includes many useful ways of interatively visualising features of the dataset e.g., distribution of mutation across the SARS-CoV-2 genome in Canada, possible international and interprovincial transmission events, diversity within each province and so on.

To explore this data for Canada, you can filter to just show Canadian genomes in the "Filter Data" window and selecting "Country -> Canada".

## Going from Sample to Analysis

### Sequencing 

Sequencing RNA viruses is difficult because there is a lot of other RNA in humans (both from our own cell's and sometimes other RNA viruses).
This means when we extract RNA (and convert it to DNA for sequencing) and sequence it our data will only contain a very small amount of SARS-CoV-2 information (even in highly infected patients).
Given that this is very inefficient we try to enrich the SARS-CoV-2 in our sample before sequencing.
This is most commonly achieved using PCR (similar but distinct from PCR's use in diagnostic testing) which amplifies the viral nucleic acids in a series of chunks covering the whole genome.
Other methods do exist ([compared here](https://www.mdpi.com/1999-4915/12/8/895)) but PCR enrichment using the "[ARTIC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7480024/)" is the de-facto standard worldwide.

![A summary of different sequencing/enrichment methods for SARS-CoV-2](https://finlaymagui.re/assets/sequencing.png)


### Assembling Genomes 

Even with enrichment our resulting sequencing data will often still contain some non-SARS-CoV-2 data (that just happened to be similar to SARS-CoV-2 sequences).
Therefore, the first step of assembly workflows like [SIGNAL](https://github.com/jaleezyy/covid-19-signal), which has been used to assemble many Canadian genomes, is to try and remove any left-over sequences from the patient/host.
This is important because we need to remove any human sequence data before we can upload the unassembled sequencing data to large databases like [NCBI](https://www.ncbi.nlm.nih.gov/) or [EBI-ENA](https://www.ebi.ac.uk/ena/browser/home).
We do this by comparing the unassembled reads to human genomes and viral genomes and then discarding any that are more similar to the human genome.
The remaining sequencing data is then aligned to a viral reference genome and based on similarities and differences to that reference wen can produce a consensus genome and any variants (using tools like [iVar](https://github.com/andersen-lab/ivar).
Finally, the results are carefully analysed for any quality control issues.

![Overview of a SARS-CoV-2 genome assembly workflow](https://finlaymagui.re/assets/assembly.png)


### Performing Phylogeographic Analyses

The assembled genomes are then uploaded to databases like [GISAID](https://www.gisaid.org/) along with accompanying tidy/consistent metadata.
Ideally, this metadata is organised following an international consensus [metadata specification](https://www.preprints.org/manuscript/202008.0220/v1), such as that developed by the Public Health Alliance For Genomic Epidemiology ([PHA4GE](https://pha4ge.org/)), and validated using tools like [DataHarmonizer](https://github.com/Public-Health-Bioinformatics/DataHarmonizer).
The resulting data is then analysed using customised versions of the Nextstrain [ncov workflow](https://github.com/nextstrain/ncov).
Briefly, data is filtered to focus on the priority area and geogrphic scale for the analysis (e.g., global, national, provincial, or even finer-grained).
These are then aligned so the any changes to a specific part of the SARS-CoV-2 genome line up with one another.
An evolutionary tree is then inferred (using tools like [IQ-Tree](http://www.iqtree.org/)) before being further refined ([treetime](https://github.com/neherlab/treetime)) using sampling metadata (especially sample collection dates).
This refinement also includes inference of ancestral traits in the tree such as potential transmission events or where and when certain mutations most likely appeared.
The final analysis is visualised via [auspice](https://github.com/nextstrain/auspice) to allow interactive exploration of the results by trained epidemiologists and virologists.

![Augur/ncov phylogeographic analysis workflow](https://finlaymagui.re/assets/augur.png)

