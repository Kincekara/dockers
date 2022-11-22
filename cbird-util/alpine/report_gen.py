#!/usr/bin/env python3

"""
Report generating script for C-BIRD workflow
Created on Thu Aug  4 13:43:46 2022

@author: Kutluhan Incekara
email: kutluhan.incekara@ct.gov
"""
import sys
import pandas as pd
from datetime import date

# report_generator.py \
# ~{samplename} \
# ~{taxon_report} \
# ~{mlst_report} \
# ~{amr_report} \
# ~{plasmid_report} \
# ~{version}

def main():
    samplename = sys.argv[1]
    taxon_report =sys.argv[2]
    mlst_report =sys.argv[3]
    amr_report = sys.argv[4]
    plasmid_report = sys.argv[5]
    version = sys.argv[6]
    footer_note = sys.argv[7]

    ## Bracken ##
    # get bracken report
    b_df = pd.read_csv(taxon_report, sep = '\t')
    b_df = b_df.sort_values(by=['fraction_total_reads'], ascending=False)

    # find top tax id & write
    with open("taxid.txt", "w") as f:
        taxid = b_df["taxonomy_id"][0]
        f.write(str(taxid))

    # Species
    b_df2 = b_df[["name", "fraction_total_reads" ]].copy()
    b_df2['fraction_total_reads'] = b_df2['fraction_total_reads'].apply(lambda x: round(x*100, 2))
    b_df2 = b_df2.rename(columns={"name": "Microorganism", "fraction_total_reads": "Abundance(%)"})

    ## MLST##
    mlst_df = pd.read_csv(mlst_report, sep="\t", skiprows=1, header=None)
    mlst_df = mlst_df.drop(columns=0)
    columns = ['Scheme','Type (ST)','Alleles']
    if len(mlst_df.columns) < 3:
        mlst_df = pd.DataFrame(columns=columns)
    else:
        for i in range(3,len(mlst_df.columns)):
            columns.append('')
        mlst_df.columns = columns

    ## AMR ##  
    r_df =  pd.read_csv(amr_report, sep = '\t')
    amr_df = r_df.loc[r_df['Element type'] == "AMR"]
    amr_df2 = amr_df[['Gene symbol','Sequence name','Class','Subclass','% Coverage of reference sequence','% Identity to reference sequence']]
    amr_df2 = amr_df2.rename(columns={'Gene symbol':'Gene','Sequence name':'Description','Class':'AR Class',
                                      'Subclass':'AR Subclass','% Coverage of reference sequence':'Coverage(%)',
                                      '% Identity to reference sequence':'Identity(%)'})
    amr_df2 = amr_df2.sort_values(by=['AR Class','AR Subclass'], ascending=True)

    ## Plasmid ##
    p_df = pd.read_csv(plasmid_report, sep = '\t')
    p_df2 = p_df[['Plasmid','Identity','Query / Template length', 'Accession number']].copy()
    p_df2 = p_df2.sort_values(by=['Identity','Plasmid'], ascending=False)
    p_df2 = p_df2.rename(columns={'Identity':'Identity(%)'})


    ## Report template ##
    page_title = samplename
    title = "Report"
    stitle1 = "Sample Information"
    stitle2 = "Taxonomic Estimation"
    stitle3 = "MLST Typing"
    stitle4 = "Resistance"
    stitle5 = "Plasmids Detected"
    today = date.today()
    
    
    if mlst_df.empty:
        mlst_txt = "No MLST scheme is found!"
    else:
        mlst_txt = mlst_df.to_string(index=False)
    
    if amr_df2.empty:
        amr_txt = "No resistance gene detected!"
    else:
        amr_txt = amr_df2.to_string(index=False)
    
    if p_df2.empty:
        plasmid_txt = "No plasmid is found!"
    else:
        plasmid_txt = p_df2.to_string(index=False)
    
    # write txt file
    with open(samplename + "_txt_report.txt", "w") as f:
        f.write(title + "\n\n")
        # Sample Information
        f.write(stitle1 + "\n")
        f.write("Report date: " +  today.strftime("%B %d, %Y") + "\n")
        f.write("Laboratory ID: " + samplename + "\n\n")
        # Microorganisms
        f.write(stitle2 + "\n")
        f.write(b_df2.to_string(index=False) + "\n\n")
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
    {b_df2.to_html(index=False, justify="left")}
    <h2>{stitle3}</h2>
    {mlst_df.to_html(index=False, justify="left")}
    <h2>{stitle4}</h2>
    {amr_df2.to_html(index=False, justify="left")}
    <h2>{stitle5}</h2>
    {p_df2.to_html(index=False, justify="left")}
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
    main()