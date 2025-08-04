#!/usr/bin/env python3
""" 
Part 1: Preparing the dataset (Data Cleaning)
Owner: Hinton, Ph.D Laboratory
Version 1.0

Usage:
    python data_cleaner.py \
    --input-dir raw_data/ \
    --output-dir cleaned_data/ \ 
    --exclude-file excluded_cleaning.txt
"""

import os
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
    
    # 1a. (Debug) show columns if you need to verify
    # print("Available columns:", df.columns.tolist())
    
    # 2. Normalize headers and prune
    df.columns = df.columns.str.strip()             # strip whitespace
    df = df[REQUIRED_COLS].copy()                   # retain only necessary columns
    
    # 3. Filter to only P/R trials
    df = df[df['display'].isin(['P Trials', 'R Trials'])] \
           .reset_index(drop=True)

    # 4. Recode any RT <120ms as incorrect (Correct=0)
    df.loc[df['Reaction Time'] < 120, 'Correct'] = 0

    # 5. Exclusion flag: count incorrect (Correct==0)
    n_incorrect = int((df['Correct'] == 0).sum())
    exclude_flag = (n_incorrect >= 80)

    return df, exclude_flag
    
def main():
    parser = argparse.ArgumentParser(description="Clean unzipped raw dataset inmport from Gorilla")
    parser.add_argument('-i','--input-dir',   required=True, help='Raw exports folder')
    parser.add_argument('-o','--output-dir',  required=True, help='Cleaned output folder')
    parser.add_argument('-e','--exclude-file',required=True, help='Excluded IDs file')
    args = parser.parse_args()

    # Ensure that output folder exists
    os.makedirs(args.output_dir, exist_ok=True)

    # Discern and group raw files by subject ID prefix
    groups = {}
    pattern = os.path.join(args.input_dir, '**', '*.*')
    for filepath in glob.glob(pattern, recursive=True):
        subj = os.path.basename(filepath).split('_')[0]
        groups.setdefault(subj, []).append(filepath)
        
    excluded = []
    for subj, files in sorted(groups.items()):
        files = sorted(files, key=os.path.getsize, reverse=True)[:2]
        # call the stub clean_subject
        df_clean, flag = clean_subject(files)        

        # write out stub CSV (will be empty)
        out_path = os.path.join(args.output_dir, f"{subj}.csv")
        df_clean.to_csv(out_path, index=False)
        
        if flag:
            excluded.append(subj) 
            print(f"[data_cleaner] Flagged {subj} for exclusion (>=80 incorrect).")
            
    # write excluded IDs (will be empty)
    with open(args.exclude_file, 'w') as fout:
        for s in excluded:
            fout.write(s + '\n')
                
        print(f"✅ Cleaning completed. Exclude subjects: {excluded}")
        
if __name__ == "__main__":
    main()    