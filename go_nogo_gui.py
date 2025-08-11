#!/usr/bin/env python3
import os
import tkinter as tk 
from tkinter import filedialog, messagebox
import pandas as pd
from data_cleaner import clean_subject  
from analyze_cleaned import compute_metrics  

def main():
    root = tk.TK(); root.withdraw() 
    
    # 1) Select raw data files to be cleaned
    raw_files = filedialog.askopenfilenames(
        title="Select raw Gorilla exports (unzipped)",
        filetypes=[("Data files","*.csv *.xlsx")]
    )
    if not raw_files:
        messagebox.showinfo("Cancelled","No .csv or .xlsx files selected.")
        return
    
    # 2) Choose where to save clean CSVs (allow multiple selection)
    clean_dir = filedialog.askdirectory(
        title="Select folder for cleaned CSVs"
    )
    if not clean_dir:
        messagebox.showinfo("Cancelled","No output folder chosen.")
        return
    
    # 3) Clean ea. subject 
    # Group by sibject ID
    groups = {}
    for fp in raw_files:
        sid = os.path.basename(fp).split('_')[0]
        groups.setdefault(sid, []).append(fp)

    excluded = []
    cleaned = []
    for sid, fps in groups.items():
        if len(fps) != 2:
            messagebox.showwarning("Skipping", f"{sid} missing files.")
            continue
        dfc, flag = clean_subject(fps)
        outp = os.path.join(clean_dir, f"{sid}.csv")
        dfc.to_csv(outp, index=False)
        cleaned.append((sid, outp))
        if flag:
            excluded.append(sid)
            
    # 4) Choose destination folder for cleaned data
    agg_fp = filedialog.asksaveasfilename(
        title="Save aggregated",
        defaultextension=".xlsx",
        filetypes=[("Excel","*.xlsx")]
    )
    if not agg_fp:
        messagebox.showinfo("Cancelled","No save location.")
        return
    # 5) Analyze clean data
    rows = []
    for sid, path in cleaned:
        if sid in excluded: continue
        df = pd.read_csv(path)
        m = compute_metrics(df)
        m['study_id'] = sid
        rows.append(m)
    pd.DataFrame(rows).to_excel(agg_fp, index=False)
    
    # 6) Report status
    messagebox.showinfo("Done", f"Excluded: {excluded}")
    
if __name__ == "__main__":
    main()