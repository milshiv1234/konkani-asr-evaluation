"""
Compact reconstruction of the later analysis logic described during manuscript preparation.

This file is not presented as a fully exact regeneration of the manuscript tables.
Instead, it documents the paper-final workflow stages that were used conceptually:

1. raw reference / hypothesis scoring
2. orthography-aware normalization
3. number-aware normalization (nWER / numeric fidelity)
4. numeric subset analysis
5. paper-final table assembly

The exact manuscript values are saved in results/paper_final_report.json.
"""

import re

ASCII_DIGIT_RE = re.compile(r"\d+")

def extract_numeric_tokens(text: str):
    return ASCII_DIGIT_RE.findall(str(text))

def numeric_utterance(text: str) -> bool:
    return bool(ASCII_DIGIT_RE.search(str(text)))

def notes():
    return {
        "pipeline": [
            "raw evaluation",
            "orthography-aware normalization",
            "number-aware normalization",
            "numeric fidelity analysis",
            "paper-final subset reporting"
        ],
        "manuscript_alignment": {
            "numeric_utterances": 94,
            "numeric_precision": 0.7592,
            "numeric_recall": 0.6651,
            "numeric_f1": 0.7090,
            "NumER": 0.3215
        }
    }

if __name__ == "__main__":
    import json
    print(json.dumps(notes(), indent=2))
