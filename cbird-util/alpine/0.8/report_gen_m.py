#!/usr/bin/env python3

"""
Report generating script for C-BIRD workflow
Created on Thu Aug  4 13:43:46 2022

@author: Kutluhan Incekara
email: kutluhan.incekara@ct.gov
"""
import argparse
import pandas as pd
from datetime import date

# Define functions

def read_bracken_report(taxon_report):
    # get bracken report
    df = pd.read_csv(taxon_report, sep = '\t')
    df = df.sort_values(by=['fraction_total_reads'], ascending=False)

    # find top tax id & write
    with open("taxid.txt", "w") as f:
        taxid = df["taxonomy_id"][0]
        f.write(str(taxid))

    # Species
    df2 = df[["name", "fraction_total_reads" ]].copy()
    df2['fraction_total_reads'] = df2['fraction_total_reads'].apply(lambda x: round(x*100, 2))
    df2 = df2.rename(columns={"name": "Microorganism", "fraction_total_reads": "Abundance(%)"})
    return df2

def read_mlst_report(mlst_report):
    df = pd.read_csv(mlst_report, sep="\t", skiprows=1, header=None)
    df = df.drop(columns=0)
    columns = ['Scheme','Type (ST)','Alleles']
    if len(df.columns) < 3:
        df = pd.DataFrame(columns=columns)
    else:
        for i in range(3,len(df.columns)):
            columns.append('')
        df.columns = columns    
    return df

def read_amr_report(amr_report):
    r_df =  pd.read_csv(amr_report, sep = '\t')
    amr_df = r_df.loc[r_df['Element type'] == "AMR"]
    amr_df2 = amr_df[['Gene symbol','Sequence name','Class','Subclass','% Coverage of reference sequence','% Identity to reference sequence']]
    amr_df2 = amr_df2.rename(columns={'Gene symbol':'Gene','Sequence name':'Description','Class':'AR Class',
                                      'Subclass':'AR Subclass','% Coverage of reference sequence':'Coverage(%)',
                                      '% Identity to reference sequence':'Identity(%)'})
    amr_df2 = amr_df2.sort_values(by=['AR Class','AR Subclass'], ascending=True)
    return amr_df2

def read_plasmidfinder_report(plasmid_report):
    df = pd.read_csv(plasmid_report, sep = '\t')
    df2 = df[['Plasmid','Identity','Query / Template length', 'Accession number']].copy()
    df2 = df2.sort_values(by=['Identity','Plasmid'], ascending=False)
    df2 = df2.rename(columns={'Identity':'Identity(%)'})
    return df2 

def read_mash_report(mash_report):
    df = pd.read_csv(mash_report, sep = '\t', header=None)
    df.columns = ['Microorganism', 'Identity(%)']
    return df

def read_blast_report(blast_report):
    df = pd.read_csv(mash_report, sep = '\t')


# Main
def main(args):
    samplename = args.samplename
    taxon_report = args.taxon_report
    mlst_report = args.mlst_report
    amr_report = args.amr_report
    plasmid_report = args.plasmid_report
    mash_report = args.mash_report
    version = args.cbird_version
    footer_note = args.footer_note
    blast_report = args.blast_report

    # read reports
    bracken = read_bracken_report(taxon_report)
    mlst = read_mlst_report(mlst_report)
    amr = read_amr_report(amr_report)
    plasmid = read_plasmidfinder_report(plasmid_report)
    mash = read_mash_report(mash_report)


    ## Report template ##
    page_title = samplename
    title = "Report"
    stitle1 = "Sample Information"
    stitle2 = "Taxonomic Profile of Reads"
    stitle3 = "MLST Typing"
    stitle4 = "Resistance"
    stitle5 = "Plasmids Detected"
    mtitle = "Predicted Organism"
    today = date.today()
      
    if mlst.empty:
        mlst_txt = "No MLST scheme is found!"
    else:
        mlst_txt = mlst.to_string(index=False)
    
    if amr.empty:
        amr_txt = "No resistance gene detected!"
    else:
        amr_txt = amr.to_string(index=False)
    
    if plasmid.empty:
        plasmid_txt = "No plasmid is found!"
    else:
        plasmid_txt = plasmid.to_string(index=False)

    # write txt file
    with open(samplename + "_txt_report.txt", "w") as f:
        f.write(title + "\n\n")
        # Sample Information
        f.write(stitle1 + "\n")
        f.write("Report date: " +  today.strftime("%B %d, %Y") + "\n")
        f.write("Laboratory ID: " + samplename + "\n\n")
        # Bracken
        f.write(stitle2 + "\n")
        f.write(bracken.to_string(index=False) + "\n\n")
        # Mash
        f.write(mtitle + "\n")
        f.write(mash.to_string(index=False) + "\n\n")
        # MLST
        f.write(stitle3 + "\n")
        f.write(mlst_txt + "\n\n")
        # AMR
        f.write(stitle4 + "\n")
        f.write(amr_txt + "\n\n")
        # Plasmid
        f.write(stitle5 + "\n")
        f.write(plasmid_txt + "\n")   
     

    # HTML #
    html = f'''
    <!DOCTYPE html>
    <html lang="en-us">
    <head>
        <meta charset="UTF-8">
        <title>{page_title}</title>
        <style>
        h1 {{
          font-family: Arial, Helvetica, sans-serif;
          font-size: 1.5em;
          text-align: center;
          color: #1e5c85
        }}

        h2 {{
          font-family: Arial, Helvetica, sans-serif;
          font-size: 1em;
          margin-top: 1em;
          margin-bottom: 0.4em;
          text-align: left;
          color: #D6672E 
        }}

        table {{
          border-collapse: collapse;
          border: none;
        }}
        
         th, td {{
          text-align: left;
          padding-left: 5px;
          padding-right: 5px;
          padding-top: 1px;
          padding-bottom: 1px;
          border: none;
        }}
        
        table.dataframe tr:nth-child(even) {{background-color: #f2f2f2;}}
        
        table.dataframe th {{
          background-color: #1e5c85;
          color: white;
        
        }}
        footer {{
			    font-size: 0.8em
		    }}      
        </style>
    </head>
    <body>
    <header>
      <h1>{title}</h1>
    </header>
    <hr>
    <article>
    <h2>{stitle1}</h2>
     <table>
      <tr>
       <td>Report date:</td>
       <td>{today}</td>
      </tr>
      <tr>
       <td>Laboratory ID:</td>
       <td>{samplename}</td>
      </tr>
     </table>
    <h2>{stitle2}</h2>
    {bracken.to_html(index=False, justify="left")}
    <h2>{mtitle}</h2>
    {mash.to_html(index=False, justify="left")}
    <h2>{stitle3}</h2>
    {mlst.to_html(index=False, justify="left")}
    <h2>{stitle4}</h2>
    {amr.to_html(index=False, justify="left")}
    <h2>{stitle5}</h2>
    {plasmid.to_html(index=False, justify="left")}
    <p></p>
    </article>
    <hr>
    <footer>
      <p><i>This report is created by <a href="https://github.com/Kincekara/C-BIRD">{version}</a> bioinformatics pipeline.</br>
      {footer_note}</i></p>
    </footer>
  </body>
</html>
'''
    # write html file
    with open(samplename + "_html_report.html", "w") as f:
        f.write(html)               
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Summary report generating script for C-BIRD workflow')

    # parser.add_argument('samplename', type=str, help='Sample name')
    # parser.add_argument('taxon_report', type=str, help='Bracken report file')
    # parser.add_argument('mlst_report', type=str, help='MLST report file')
    # parser.add_argument('amr_report', type=str, help='AMRFinderPlus report file')
    # parser.add_argument('plasmid_report', type=str, help='PlasmidFinder report file')    
    # parser.add_argument('version', type=str, help='C-BIRD version')
    # parser.add_argument('-m', '--mash_report', type=str, help='MASH report file')
    # parser.add_argument('-f', '--footer_note', type=str, help='Disclaimer text', default="")
    
    parser.add_argument('-s', '--samplename', type=str, help='Sample name', required=True)
    parser.add_argument('-t', '--taxon_report', type=str, help='Bracken report file', required=True)
    parser.add_argument('-st', '--mlst_report', type=str, help='MLST report file', required=True)
    parser.add_argument('-a', '--amr_report',  type=str, help='AMRFinderPlus report file', required=True)
    parser.add_argument('-p', '--plasmid_report', type=str, help='PlasmidFinder report file', required=True)
    parser.add_argument('-m', '--mash_report',  type=str, help='MASH report file')
    parser.add_argument('-c', '--cbird_version',  type=str, help='C-BIRD version', default="v1.0.0")
    parser.add_argument('-f', '--footer_note',  type=str, help='Disclaimer text', default="")
    parser.add_argument('-b', '--blast_report', type=str, help='Blast report file')

    args = parser.parse_args()

    main(args)