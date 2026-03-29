import json
from pathlib import Path

PAPER_FINAL = {
    "dataset_total_utterances": 4100,
    "raw_wer": 0.2203,
    "raw_cer": 0.0564,
    "orthography_aware_wer": 0.2023,
    "orthography_aware_cer": 0.0522,
    "number_aware_wer": 0.2010,
    "number_aware_cer": 0.0525,
    "numeric_utterances": 94,
    "numeric_utterance_wer": 0.5073,
    "numeric_utterance_cer": 0.1785,
    "non_numeric_utterances": 4006,
    "non_numeric_wer": 0.2459,
    "non_numeric_cer": 0.0612,
    "numeric_precision": 0.7592,
    "numeric_recall": 0.6651,
    "numeric_f1": 0.7090,
    "NumER": 0.3215,
    "kd_total_utterances": 3789,
    "kd_numeric_error_utterances": 633,
    "kd_numeric_error_rate": 0.1671
}

def main():
    outdir = Path(__file__).resolve().parents[1] / "results"
    outdir.mkdir(parents=True, exist_ok=True)
    with open(outdir / "paper_final_report.json", "w", encoding="utf-8") as f:
        json.dump(PAPER_FINAL, f, indent=2, ensure_ascii=False)
    with open(outdir / "paper_final_report.txt", "w", encoding="utf-8") as f:
        f.write("Paper-final reported metrics\n")
        f.write("=" * 32 + "\n")
        for k, v in PAPER_FINAL.items():
            f.write(f"{k}: {v}\n")
    print("Saved paper_final_report.json and paper_final_report.txt")

if __name__ == "__main__":
    main()
