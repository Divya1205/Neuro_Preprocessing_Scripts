# ABIDE .1D Downloader

Python script to download ABIDE preprocessed ROI time series files using the AWS CLI. Download the phenotypic data file as well. [Direct CSV download (raw)](https://raw.githubusercontent.com/preprocessed-connectomes-project/abide/master/Phenotypic_V1_0b_preprocessed1.csv)

## Requirements

pip install pandas tqdm wget

## Usage

python download_abide.py \
  --pheno_csv ./data/Phenotypic_V1_0b_preprocessed1.csv \
  --out_dir ./abide_data/cpac_cc200 \
  --pipe cpac \
  --roi cc200 \
  --fg filt_noglobal

# ABIDE FCN Generator

Python script to generate Functional Connectivity Networks (FCNs) from ABIDE preprocessed ROI time series `.1D` files using Nilearn.

## Requirements

pip install pandas tqdm nilearn numpy

## Usage

python generate_fcn.py \
  --ts_dir ./Abide/abide_dparsf_cc200 \
  --pheno_csv ./Abide/Phenotypic_V1_0b_preprocessed1.csv \
  --out_dir ./Abide/outputs/dparsf \
  --roi cc200 \
  --method correlation


