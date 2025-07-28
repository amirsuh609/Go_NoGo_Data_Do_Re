#!/usr/bin/env python3
"""
Part 2 + 3: Calculating Variables of Interest & Consolidating
Usage:
    python analyze_cleaned.py 
    --input-dir cleaned_data/ 
    --exclude-file excluded_cleaning.txt 
    --output-file aggregated_metrics.xlsx
"""
import os
import glob
import argparse
import pandas as pd

METRIC_COLS = [
    'go_nogo_accuracy_t',
    'go_nogo_hits_t',
    'go_nogo_omission_t',
    'go_nogo_comission_t',
    'go_nogo_trueneg_t',
    'go_nogo_120ms_t',
    'go_nogo_RTmean_t',
    'go_nogo_RTmed_t',
    'go_nogo_RTstdev_t',
    'go_nogo_accuracy_p',
    'go_nogo_hits_p',
    'go_nogo_omission_p',
    'go_nogo_comission_p',
    'go_nogo_trueneg_p',
    'go_nogo_120ms_p',
    'go_nogo_RTmean_p',
    'go_nogo_RTmed_p',
    'go_nogo_RTstdev_p',
    'go_nogo_accuracy_r',
    'go_nogo_hits_r',
    'go_nogo_omission_r',
    'go_nogo_comission_r',
    'go_nogo_trueneg_r',
    'go_nogo_120ms_r',
    'go_nogo_RTmean_r',
    'go_nogo_RTmed_r',
    'go_nogo_RTstdev_r',
]

def compute_metrics(df):
    """
    Given cleaned df (only P/R trials, Correct recoded),
    returns a dict of all required metrics.
    """
    out = {}
    # helper to tally counts & RT stats

    # Total
    
    # P‑only
    
    # R‑only
    
    # Exclusion Criteria
    # Load exclude list
    
    # Consolidate
    
