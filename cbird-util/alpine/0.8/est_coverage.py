#!/usr/bin/env python3

"""
Coverage calculating script for C-BIRD workflow
Created on Thu Aug  4 13:43:46 2022

@author: Kutluhan Incekara
email: kutluhan.incekara@ct.gov
"""
import argparse
import pandas as pd

def main(args):
    stats_file = args.stats_file
    total_bases = args.total_bases
    top_taxid = args.top_taxid
    alt_gs = args.alt_gs
    genome_length = args.genome_length

    # get assembly stats file
    gs_df = pd.read_csv(stats_file, sep = '\t')
    
    ## Coverage ##
    # get total base number
    with open(total_bases, "r") as tb:
        basenum = tb.readline()
        
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
    parser = argparse.ArgumentParser(description='Coverage calculating script for C-BIRD workflow')

    parser.add_argument('stats_file', type=str, help='genome size statistics file')
    parser.add_argument('total_bases', type=str, help='file containing the total number of bases')
    parser.add_argument('top_taxid', type=int, help='The tax ID of the top hit')
    parser.add_argument('alt_gs', type=str, help='file containing the expected genome size (alternative)')
    parser.add_argument('genome_length', type=int, help='The length of the genome being analyzed')

    args = parser.parse_args()

    main(args)
