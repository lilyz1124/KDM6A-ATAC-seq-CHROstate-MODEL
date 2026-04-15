# KDM6A-ATAC-seq-CHROstate-MODEL
kdm6a_heart_model/
├── config.yaml
├── requirements.txt
├── README.md
├── scripts/
│   ├── 01_fetch_metadata.py
│   ├── 02_download_files.py
│   ├── 03_qc_and_align.sh
│   ├── 04_call_peaks.sh
│   ├── 05_build_consensus_peaks.py
│   ├── 06_make_chromhmm_input.py
│   ├── 07_train_model.py
│   ├── 08_eval_model.py
│   ├── 09_link_peaks_to_genes.py
│   └── 10_differential_report.py
├── models/
├── data/
│   ├── raw/
│   ├── processed/
│   └── metadata/
└── results/
    ├── tables/
    ├── figures/
    └── tracks/
