#!/usr/bin/env python3
""" 
Part 1: Preparing the dataset (Data Cleaning)
Owner: Hinton, Ph.D Laboratory
Version 1.0

Usage:
    python data_cleaner.py\
    --input-dir ./raw_data\
    --output-dir ./cleaned_data\
    --exclude-file excluded_subjects.txt
    
    or
    
    python3 data_cleaner.py -i ./raw_data -o ./cleaned_data -e ./excluded_subjects.txt
"""

import os
import re
import glob
import argparse
import pandas as pd

REQUIRED_COLS = [
    'Trial Number',
    'Reaction Time',
    'Response',
    'Attempt',
    'Correct',
    'display',
    'Answer'
]

def subject_id_from_path(filepath: str) -> str:
    """Derive subject ID from suject's folder name.

    If the parent folder contains digits, return the first digit-run
    (e.g., '17 gonogo' -> '17'); otherwise return the entire folder name.
    """
    parent = os.path.basename(os.path.dirname(filepath))
    m = re.search(r'\d+', parent)
    return m.group(0) if m else parent

def clean_subject(file_paths):
    """
    1. Read & combine both task halves (CSV or XLSX)
    2. Normalize headers, prune to REQUIRED_COLS
    3. Filter to real trials (P Trials & R Trials)
    4. Recode RT <120ms as incorrect
    5. Flag exclusion if >=80 incorrect (25% of 320)
    Returns: (cleaned_df, exclude_flag)
    """
    # 1. Read & combine
    parts = []
    for fp in file_paths:
        if fp.lower().endswith('.csv'):
            parts.append(pd.read_csv(fp))
        else:
            parts.append(pd.read_excel(fp, engine='openpyxl'))
    df = pd.concat(parts, ignore_index=True)
    
    # 2. Normalize headers and prune
    df.columns = df.columns.str.strip()             
    df = df[REQUIRED_COLS].copy()                   # retain only necessary columns
    
    # 3. Filter to only P/R trials
    df = df[df['display'].isin(['P Trials', 'R Trials'])].reset_index(drop=True)

    # 4. Recode any RT <120ms as incorrect (Correct=0)
    df.loc[df['Reaction Time'] < 120, 'Correct'] = 0

    # 5. Exclusion flag: count incorrect (Correct==0)
    n_incorrect = int((df['Correct'] == 0).sum())
    exclude_flag = (n_incorrect >= 80)

    return df, exclude_flag
    
def main():
    parser = argparse.ArgumentParser(description="Clean Go/NoGo raw export: prune columns, filter P/R trials, recode fast RT's, flag exclusions.")
    parser.add_argument('-i','--input-dir',   required=True, help='Folder of raw export containing subject folders')
    parser.add_argument('-o','--output-dir',  required=True, help='Folder to accept cleaned output')
    parser.add_argument('-e','--exclude-file',required=True, help='Path to write excluded subject IDs (>=80 incorrect responses)')
    args = parser.parse_args()

    # Ensure that output folder exists
    os.makedirs(args.output_dir, exist_ok=True)

    # Discern and group raw files by subject ID prefix
    groups = {}
    pattern = os.path.join(args.input_dir, '**', '*.*')
    for filepath in glob.glob(pattern, recursive=True):
        if not filepath.lower().endswith(('.csv', '.xlsx', '.xls')):
            continue
        subj = subject_id_from_path(filepath)
        groups.setdefault(subj, []).append(filepath)
        
    excluded = []
    processed=0
    for subj, files in sorted(groups.items()):
        files = sorted(files, key=os.path.getsize, reverse=True)[:2]
        try:
            df_clean, flag = clean_subject(files)        
        except Exception as ex:
            print(f"[data_cleaner] ERROR processing {subj}: {ex}")
            continue
        
        out_path = os.path.join(args.output_dir, f"{subj}.csv")
        df_clean.to_csv(out_path, index=False)
        processed += 1
        
        if flag:
            excluded.append(subj) 
            print(f"[data_cleaner] Flagged {subj} for exclusion (>=80 incorrect).")
            
    # write excluded IDs 
    with open(args.exclude_file, 'w') as fout:
        for s in excluded:
            fout.write(s + '\n')
                
        print(f"✅ Cleaning completed. Exclude subjects: {excluded}")
        
if __name__ == "__main__":
    main()    