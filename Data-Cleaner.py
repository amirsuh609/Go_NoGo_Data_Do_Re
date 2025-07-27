#!/usr/bin/env python3
""" 
Part 1: Preparing the dataset (Cleaning)
Owner: Hinton Laboratory
Version 1.0

Usage:
    python cleaning.py 
    --input-dir raw_data/ 
    --output-dir cleaned_data/ 
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
    
    #Merge two halves, prune columns, filter trials, recode RT<120ms as incorrect, and flag if incorrect trials >= 80 (25% of 320).
    #Returns: cleaned_df, exclude_flag (bool)
    
    #1. Read & combine
    
    
    #2. Keep only the required columns
    
    
    #3. Filter to real trials
    
    
    #4. Recode any RT < 120ms as incorrect
    
    
    #5. Flag exclusion if incorrect >= 80
    
    #a) Group files by subject ID (prefix before underscore)
    
    #b) Write excluded list