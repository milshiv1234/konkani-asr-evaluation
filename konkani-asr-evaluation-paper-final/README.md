# konkani-asr-evaluation

This repository packages the **paper-final evaluation artifacts** for the manuscript:

**Beyond Word Error Rate: Orthography and Number-Aware Evaluation of Low-Resource Konkani ASR**

## Important note

The uploaded `asr_eval_predictions.csv` is included for transparency, but the manuscript tables were produced from the **later paper-final evaluation pipeline** shared during analysis, not from raw CSV scoring alone.

In particular, the paper-final pipeline applies:

1. orthography-aware normalization
2. number-aware normalization
3. numeric fidelity analysis
4. paper-final subset accounting used in the manuscript tables

As a result, manuscript values such as:

- numeric utterances = **94**
- numeric WER = **0.5073**
- numeric CER = **0.1785**
- Numeric Precision = **0.7592**
- Numeric Recall = **0.6651**
- Numeric F1-score = **0.7090**
- NumER = **0.3215**

are recorded in the repository as the **paper-final reported values**.

## Contents

- `data/asr_eval_predictions.csv`  
  Raw prediction CSV used for baseline transparency.

- `scripts/paper_final_metrics.py`  
  Minimal manuscript-aligned metric definitions and summary export.

- `scripts/shared_pipeline_notes.py`  
  Compact reconstruction of the later analysis logic based on the shared code.

- `results/paper_final_report.json`  
  Paper-final metrics matching the manuscript.

- `results/paper_final_report.txt`  
  Human-readable paper-final summary.

- `docs/reproducibility_note.md`  
  Explanation of why paper-final values differ from direct raw-CSV scoring.

## Reproducibility status

This package is intended to support **methodological reproducibility** and align the repository with the manuscript's final reported values. Full end-to-end regeneration of all paper-final numbers would require the exact intermediate normalization outputs used in the final paper workflow.

## Contact

Corresponding author: Milind Shivolkar
