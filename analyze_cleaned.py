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
    pass

if __name__ == "__main__":
    main()
