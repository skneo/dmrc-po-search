import os
import pandas as pd
import pdfplumber

directory = 'files'

for filename in os.listdir(directory):
    if filename.endswith(".PDF"):
        pdf_file = os.path.join(directory, filename)
        all_dfs = []
        with pdfplumber.open(pdf_file) as pdf:
            for i, page in enumerate(pdf.pages):
                df = pd.DataFrame(page.extract_table())
                all_dfs.append(df)
        result = pd.concat(all_dfs)
        excel_file = pdf_file.replace('.PDF', '.xlsx')
        result.to_excel(excel_file, index=False)
        print(f"{pdf_file} converted to {excel_file}")
    else:
        continue

print("All PDF files converted to Excel successfully!")
 