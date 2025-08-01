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
    'Display',
    'Answer'
]

def clean_subject(file_paths):
    """
    STUB: merge, prune columns, filter trials, recode, flag exclusion.
    #Returns: (cleaned_df, exclude_flag)
    """  
    return pd.DataFrame(), False
    
def main():
    parser = argparse.ArgumentParser(description="Clean Go/No-Go datasets")
    parser.add_argument('-i','--input-dir',   required=True, help='Raw exports folder')
    parser.add_argument('-o','--output-dir',  required=True, help='Cleaned outputs folder')
    parser.add_argument('-e','--exclude-file',required=True, help='Excluded IDs file')
    args = parser.parse_args()

    # confirm output folder exists
    os.makedirs(args.output_dir, exist_ok=True)

    # group raw files by subject ID prefix
    groups = {}
    for fp in glob.glob(os.path.join(args.input_dir, '*.*')):
        sid = os.path.basename(fp).split('_')[0]
        groups.setdefault(sid, []).append(fp)
        
    excluded = []
    for sid, files in sorted(groups.items()):
        # call the stub clean_subject
        df_clean, flag = clean_subject(files)        

        # write out stub CSV (will be empty)
        out_path = os.path.join(args.output_dir, f"{sid}.csv")
        df_clean.to_csv(out_path, index=False)
        
        if flag:
            excluded.append(sid)
            
    # write excluded IDs (will be empty)
    with open(args.exclude_file, 'w') as fout:
        for s in excluded:
            fout.write(s + '\n')    
        
if __name__ == "__main__":
    main()    