#!/usr/bin/env python3

"""
Coverage calculating script for C-BIRD workflow
Created on Thu Aug  4 13:43:46 2022

@author: Kutluhan Incekara
email: kutluhan.incekara@ct.gov
"""
import sys
import pandas as pd

def main():
    stats_file = sys.argv[1]
    q30_bases = sys.argv[2]
    top_taxid = sys.argv[3]
    alt_gs = sys.argv[4]
    genome_length = sys.argv[5]

    # get assembly stats file
    gs_df = pd.read_csv(stats_file, sep = '\t')
    
    ## Coverage ##
    # get total base number
    with open(q30_bases, "r") as q30:
        basenum = q30.readline()
        
    # find top hit's expected genome size
    x = gs_df.loc[gs_df ["#species_taxid"]==int(top_taxid), "expected_ungapped_length"]
    if (len(x) != 0):
        exp_gs = str(x.values[0])
    else:
       with open(alt_gs, "r") as f:
           exp_gs = f.readline()
        
    # calculate sequencing depth & genome ratio
    coverage = 0.0
    ratio = 0.0
    try:
        coverage = round((int(basenum) / int(exp_gs)),2)
    except ValueError:
        print("Someting wrong in coverage calculation")
    finally:
         with open("COVERAGE", "w") as cov:
            cov.write(str(coverage))       

    try:                
        ratio = round((int(genome_length) / int(exp_gs)),2)
    except ValueError:
        print("Someting wrong in genome ratio calculation")
    finally:
        with open("GENOME_RATIO", "w") as r:
            r.write(str(ratio))
        
if __name__ == "__main__":
    main()