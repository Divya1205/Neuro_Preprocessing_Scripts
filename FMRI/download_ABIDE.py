import pandas as pd
import os
from tqdm import tqdm
import wget
import argparse

def create_url(site, sub_id, pipe, roi, fg):
    base = "https://s3.amazonaws.com/fcp-indi/data/Projects/ABIDE_Initiative/Outputs"
    return f"{base}/{pipe}/{fg}/rois_{roi}/{site}_{sub_id}_rois_{roi}.1D"

def download_abide_roi(pheno_csv, out_dir, pipe="cpac", roi="cc200", fg="filt_noglobal"):
    df = pd.read_csv(pheno_csv)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for _, row in tqdm(df.iterrows(), total=len(df)):
        sub_id = str(row["SUB_ID"]).zfill(7)
        site = row["SITE_ID"]
        url = create_url(site, sub_id, pipe, roi, fg)
        out_file = os.path.join(out_dir, f"{site}_{sub_id}_rois_{roi}.1D")
        try:
            wget.download(url, out_file)
        except:
            print(f"Failed to download: {url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pheno_csv", required=True, help="Path to ABIDE phenotypic CSV file")
    parser.add_argument("--out_dir", required=True, help="Directory to store downloaded .1D files")
    parser.add_argument("--pipe", default="cpac", help="Pipeline name (default: cpac)")
    parser.add_argument("--roi", default="cc200", help="Atlas name (default: cc200)")
    parser.add_argument("--fg", default="filt_noglobal", help="Filtering strategy (default: filt_noglobal)")
    args = parser.parse_args()

    download_abide_roi(
        pheno_csv=args.pheno_csv,
        out_dir=args.out_dir,
        pipe=args.pipe,
        roi=args.roi,
        fg=args.fg
    )
