import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from nilearn.connectome import ConnectivityMeasure
import argparse

def load_time_series(file_path):
    """Load .1D time series (T × ROIs)"""
    return np.loadtxt(file_path)

def compute_fcns(ts_dir, pheno_csv, roi='cc200', method='correlation'):
    """Compute FCNs from ABIDE .1D files"""
    df = pd.read_csv(pheno_csv)
    df["SUB_ID"] = df["SUB_ID"].astype(str).str.zfill(7)
    df["filename"] = df["SITE_ID"] + "_" + df["SUB_ID"] + f"_rois_{roi}.1D"

    ts_list = []
    valid_subjects = []

    for fname in tqdm(df["filename"]):
        fpath = os.path.join(ts_dir, fname)
        if os.path.exists(fpath):
            ts = load_time_series(fpath)
            ts_list.append(ts)
            valid_subjects.append(fname)
        else:
            print(f" Missing: {fpath}")

    print(f"\n Loaded {len(ts_list)} time series")

    # Compute FC
    conn = ConnectivityMeasure(kind=method, standardize="zscore_sample")
    fc_matrices = conn.fit_transform(ts_list)

    return valid_subjects, fc_matrices

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ts_dir", required=True, help="Directory containing .1D time series files")
    parser.add_argument("--pheno_csv", required=True, help="Path to ABIDE phenotypic CSV file")
    parser.add_argument("--out_dir", default="./outputs", help="Directory to save output .npy and .csv files")
    parser.add_argument("--roi", default="cc200", help="Atlas name (e.g., cc200, aal)")
    parser.add_argument("--method", default="correlation", help="FC method: correlation | partial correlation | tangent")

    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    subjects, fcns = compute_fcns(args.ts_dir, args.pheno_csv, roi=args.roi, method=args.method)

    np.save(os.path.join(args.out_dir, f"abide_fc_matrices_{args.roi}.npy"), fcns)
    pd.Series(subjects).to_csv(os.path.join(args.out_dir, f"abide_subjects_{args.roi}.csv"), index=False)
