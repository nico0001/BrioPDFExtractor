import time
import os
import PDFPlumber
import pdfplumber
import config
import pandas as pd

def test_pattern(input_folder="data\\OneDrive_1_02-01-2026\\Vivium 85310 01 a 08.pdf", pattern = r"RELEVE\s*DE\s*COMPTE\s*PRODUCTEUR\s*DE\s*(\b\d{2}-\d{4}\b)"):
    with pdfplumber.open(input_folder) as pdf:
        for page in pdf.pages[:1]: 
            #page.to_image(resolution=150).draw_rects(page.chars).show()
            text = page.extract_text(keep_blank_chars=True)
            print(text)
            print(page.search(pattern, regex=True, case=False)[0]["groups"][0])


def test_extract(folder="input", output_file="output_combined.csv"):
    batch = []
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if not os.path.isfile(file_path):
            continue
        base_name = os.path.splitext(filename)[0].lower()
        for comp,settings in config.company_lst.items():
            if comp.lower() in base_name:
                batch.append((comp, file_path, settings))
                base_name = ""
    PDFPlumber.extract_data_batch(batch, output_file)

t0 = time.time()
#test_pattern(input_folder="data\\OneDrive_1_02-01-2026\\Vivium 85310 01 a 08.pdf")
test_extract("data\\OneDrive_1_02-01-2026","output_combined.csv")
#PDFPlumber.extract_data_batch([("DKV","data/organized/DKV/01_DKV.pdf",config.DKV_settings)])
print(f"Execution time: {time.time() - t0} seconds")