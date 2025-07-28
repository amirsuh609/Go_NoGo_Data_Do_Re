#!/usr/bin/env python3
import tkinter as tk 
from tkinter import filedialog, messagebox
import pandas as pd
from data_cleaner import clean_subject  
from analyze_cleaned import compute_metrics  

def main():
    root = tk.TK()
    root.withdraw() #Hide blank window
    
# 1) Select raw data files to be cleaned

# 2) Choose where to save clean CSVs (allow multiple selection)

# 3) Clean ea. subject 
# Group by sibject ID

# 4) Choose destination folder for cleaned data

# 5) Analyze clean data

# 6) Report status
    