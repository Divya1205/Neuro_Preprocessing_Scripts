# ABIDE .1D Downloader

Python script to download ABIDE preprocessed ROI time series files from the AWS public dataset.

## Requirements

pip install pandas tqdm wget

## Usage

python download_abide.py \
  --pheno_csv ./data/Phenotypic_V1_0b_preprocessed1.csv \
  --out_dir ./abide_data/cpac_cc200 \
  --pipe cpac \
  --roi cc200 \
  --fg filt_noglobal


