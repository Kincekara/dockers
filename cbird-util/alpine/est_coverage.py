#!/usr/bin/env python3

"""
Covarerage calculating script for C-BIRD workflow
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
    
    # get assembly stats file
    gs_df = pd.read_csv(stats_file, sep = '\t')
    
    ## Coverage ##
    # get total base number
    with open(q30_bases, "r") as q30:
        basenum = q30.readline()
        
    # find top hit's expected genome size
    x = gs_df.loc[gs_df ["#species_taxid"]==top_taxid, "expected_ungapped_length"]
    if (len(x) != 0):
        exp_gs = x[0]
    else:
       with open(alt_gs, "r") as f:
           exp_gs = f.readline()
        
    # calculate & write sequencing depth
    with open("COVERAGE", "w") as cov:
        coverage = str(round(int(basenum) / int(exp_gs))) + "X"
        cov.write(coverage)

if __name__ == "__main__":
    main()