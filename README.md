# FMRI

## ABIDE .1D Downloader

Python script to download ABIDE preprocessed ROI time series files using the AWS CLI. Download the phenotypic data file as well. [Click here to download the phenotypic CSV file](https://raw.githubusercontent.com/preprocessed-connectomes-project/abide/master/Phenotypic_V1_0b_preprocessed1.csv)  

Right-click and choose “Save As” if it opens as text.


### Requirements

pip install pandas tqdm wget

### Usage

python download_abide.py \
  --pheno_csv ./data/Phenotypic_V1_0b_preprocessed1.csv \
  --out_dir ./abide_data/cpac_cc200 \
  --pipe cpac \
  --roi cc200 \
  --fg filt_noglobal

# FCN

## ABIDE FCN Generator

Python script to generate Functional Connectivity Networks (FCNs) from ABIDE preprocessed ROI time series `.1D` files using Nilearn.

### Requirements

pip install pandas tqdm nilearn numpy

### Usage

python generate_fcn.py \
  --ts_dir ./Abide/abide_dparsf_cc200 \
  --pheno_csv ./Abide/Phenotypic_V1_0b_preprocessed1.csv \
  --out_dir ./Abide/outputs/dparsf \
  --roi cc200 \
  --method correlation

# MRI

To install dependencies for MRI preprocessing, use one of the following:

pip install -r requirements_mri_preproc.txt
conda create -n mri_env --file requirements_mri_preproc.txt


## download-kaggle-series-folder-wise.ipynb

Run in Kaggle https://www.kaggle.com/competitions/rsna-intracranial-aneurysm-detection to zip and download a specific DICOM series folder along with train.csv metadata.
Outputs: {SeriesInstanceUID}.zip and train.csv with download links.

## Dicom_Loading_Preprocessing.ipynb 

Inspects raw DICOM MRI data for one patient, extracts metadata, orientation, voxel spacing, calculates isotropy/anisotropy and visualizes a slice.
Prepares data for downstream NIfTI conversion or deep learning tasks in the RSNA aneurysm challenge.

