# Project Desription - brainScanClassifier
### This image classifier is built with TensorFlow and aims to identify neurological conditions using brain scan images sourced from studies available on the [IDAs](https://ida.loni.usc.edu/login.jsp) website. Currently, the classifier focuses on detecting Parkinson's disease, autism, or neither condition. The ultimate goal is to expand its capabilities by incorporating more neurological diseases and conditions into the classifier's repertoire. As well as, allowing the user to drop an entire MRI scan, identify problematic brain images, and determine the most likely condition of the patient or if they are fine.

# Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)
- [Configuration](#Configuration)
- [Documentaion](#Documentaion)
- [Acknowledgments](#Acknowledgments)

# Requirements
- git installed
- python installed
- jupyter installed
    - download anaconda (comes preinstalled)
    - pip install jupyter
- If planning to use GPU... CUDA installed
    - or use your CPU (expect slower image training)

# Installation
- Create Virtual Environment
    - python -m venv brainClassifier
    - .\brainClassifier\Scripts\activate
    - pip install ipykernel
    - python -m ipykernel install --name=brainClassifier

# Usage
- Start Jupyter lab
    - type command "jupyter lab"
    - select brainClassifier as your kernel
- Run Code up to the test section (this will train classifier)
- Type the file path to your brain image in Section 10 - Test

# Acknowledgments

## Classifer
- Most of the code is from Nicholas Renotte's Deep Learning tutorials
    - [tutorial 1](https://www.youtube.com/watch?v=19LQRx78QVU&list=PLgNJO2hghbmiXg5d4X8DURJP9yv9pgjIu&index=1)
    - [more in depth version of tutorial 1](https://www.youtube.com/watch?v=jztwpsIzEGc&list=PLgNJO2hghbmiXg5d4X8DURJP9yv9pgjIu&index=2)

## All data from [IDA](https://ida.loni.usc.edu/login.jsp)
### Parkinson Data
- Received from the PPMI study
- Used the dicom converter to create pngs

### Alzheimer Data
- Received from the ADNI study
- Used the dicom converter to create pngs

### Autism Data
- Received from the ABIDE study
- Used the nii converter to create pngs