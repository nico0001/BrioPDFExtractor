import pdfplumber
import pandas as pd
import config

def crop_table(page, find_settings={}, data_row_top=1, data_row_bot=0):
    table = page.find_table(table_settings=find_settings)
    if not table:
        return None
    if data_row_bot == 0:
        data_row_bot = len(table.rows) - 1
    return page.crop((table.bbox[0], table.rows[data_row_top].bbox[1], table.bbox[2], table.rows[data_row_bot].bbox[3]))

def extract_table_data(cropped_page, extract_settings):
    table = cropped_page.extract_table(table_settings=extract_settings)
    if table:
        return pd.DataFrame(table)
    return None

def extract_data(pdf_path, format_settings):
    df = extract_data_d(pdf_path, format_settings["crop_settings"], format_settings["extract_settings"],
                    format_settings["columns"], format_settings["data_row_top"], format_settings["data_row_bot"],
                    format_settings["nb_pages"], format_settings["mandatory_columns"], format_settings["Emmision_format"],
                    agent_pat=format_settings["agent_pattern"])
    return df

def extract_data_d(pdf_path, crop_settings, extract_settings, columns, data_row_top=1, data_row_bot=1, n_pages=0, 
                   mandatory_columns=[], emmission_format="", agent_pat=""):
    with pdfplumber.open(pdf_path) as pdf:
        if n_pages == 0:
            n_pages = len(pdf.pages)
        df = pd.DataFrame()
        for page in pdf.pages[:n_pages]: 
            #page.to_image(resolution=150).debug_tablefinder(crop_settings).show()
            #page=crop_table(page, crop_settings, data_row_top, data_row_bot)
            if not page:
                continue
            df_page = extract_table_data(page, extract_settings)
            df = pd.concat([df, df_page], ignore_index=True) if df_page is not None else df
            #page.to_image(resolution=150).reset().debug_tablefinder(extract_settings).show()  # Display the image with bounding boxes
        
        df.columns = columns
        if agent_pat and len(pdf.pages) > 0 and pdf.pages[0].search(agent_pat, regex=True, case=False):
            df["N° Agent"] = pdf.pages[0].search(agent_pat, regex=True, case=False)[0]["groups"][0]
        df = df.replace(r'^\s*$', pd.NA, regex=True)
        df = df.dropna(subset=mandatory_columns, ignore_index=True)
        if emmission_format != "":
            df = df[pd.to_datetime(df["Emmission"], format=emmission_format, errors='coerce').notna()]
        df["Débit"] = pd.to_numeric(df["Débit"].str.replace('.','').str.replace(',','.'), errors='coerce')
        df["Crédit"] = pd.to_numeric(df["Crédit"].str.replace('.','').str.replace(',','.'), errors='coerce')
        #print(df)
        return df


def extract_data_batch(batch,output_file="output_combined.csv"):
    df = pd.DataFrame(columns=config.standard_columns)
    df.to_csv("output/"+output_file, index=False)
    for company,path,settings in batch:
        print(f"Processing {path} for company {company}")
        df_temp = extract_data(path, settings).reindex(columns=config.standard_columns)
        df_temp["Compagnie"] = company
        #df = pd.concat([df, df_temp], ignore_index=True)
        df_temp.to_csv("output/"+output_file, mode='a', header=False, index=False)
        print(f"Processed {len(df_temp)} transactions succesfully")
    print(f"Processed a total of {pd.read_csv('output/'+output_file).shape[0]} transactions.")