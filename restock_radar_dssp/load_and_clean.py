"""
Steps 1-2: Problem framing, data loading and cleaning
Dataset: Kaggle "Store Item Demand Forecasting Challenge" (use train.csv only)
Columns expected: date, store, item, sales
 
Run:  python step1_2_load_and_clean.py
"""

from pathlib import Path
import pandas as pd

RAW_PATH = Path('train.csv')
CLEAN_PATH = Path('clean_train.csv')

def load_raw(path: Path):


def main():
    df = load_raw(RAW_PATH)



if __name__ == "__main__":
    main()