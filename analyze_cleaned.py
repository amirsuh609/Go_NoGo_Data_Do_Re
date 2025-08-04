#!/usr/bin/env python3
"""
Part 2+3: Calculates Variables of Interest & Consolidating
Owner:    Hinton, Ph.D Laboratory
Version:  1.0

Usage:
    python analyze_cleaned.py 
    --input-dir cleaned_data/ 
    --exclude-file excluded_cleaning.txt 
    --output-file aggregate_metrics.xlsx
"""

import os
import glob
import argparse
import pandas as pd

def compute_metrics(df):
    """
    Given cleaned df (incl. P/R trials, Correct recoded),
    returns a dict of all required metrics.
    """
    return {
        'go_nogo_accuracy_t': 0,
        'go_nogo_hits_t': 0,
        'go_nogo_omission_t': 0,
        'go_nogo_comission_t': 0,
        'go_nogo_trueneg_t': 0,
        'go_nogo_120ms_t': 0,
        'go_nogo_RTmean_t': None,
        'go_nogo_RTmed_t': None,
        'go_nogo_RTstdev_t': None,
    }    
        
def main():
    """
    STUB: parse flags, load CSVs, apply compute_metrics, save Excel.
    """
    parser = argparse.ArgumentParser(description="Analyze cleaned Go/No-Go data")
    parser.add_argument('-i','--input-dir',   required=True,
                        help='Folder with per-subject cleaned CSVs')
    parser.add_argument('-e','--exclude-file',required=True,
                        help='Excluded IDs list')
    parser.add_argument('-o','--output-file', required=True,
                        help='Path for aggregated Excel metrics')
    args = parser.parse_args()
    
    #Load exclusion list
    excluded = set()
    if os.path.exists(args.exclude_file):
        with open(args.excluded_file) as f:
            excluded = {line.strip() for line in f if line.strip()}
    print(f"[analyze] Excluded: {sorted(excluded)}")
    
    #Find all clean .csv files
    rows = []
    pattern = os.path.join(args.input_dir, '*.csv')
    for fp in sorted(glob.glob(pattern)):
        subj = os.path.basename(fp).split('.')[0]
        if subj in excluded:
            print(f"[analyze] Skipping excluded {subj}")
            continue
        
        df = pd.read_csv(fp)
        metrics = compute_metrics(df)        # stub metrics
        metrics['study_id'] = subj
        rows.append(metrics)
    
    #Build and write aggregated table
    result_df = pd.DataFrame(rows)
    result_df.to_excel(args.output_file, index=False)
    print(f"✅ Saved aggregated metrics to {args.output_file}")

if __name__ == "__main__":
    main()
