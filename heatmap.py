# Copyright (C) 2018  Ahmad A. A. (https://github.com/bbpgrs/)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import common as cmn
import os
import logging


def show_heatmap():
    """
    """
    #combined_file_path = os.path.join(cmn.DL_DIR, cmn.PTEN_CORR_FNAME)
    combined_file_path = os.path.join("ref", cmn.PTEN_CORR_FNAME)
    if os.path.isfile(combined_file_path):
        logging.info("Found combined PTEN correlation file, generating heatmap ...")

        df = pd.read_csv(combined_file_path, sep="\t", index_col=0)
        sbn.heatmap(df, cmap='RdYlGn', xticklabels=1, yticklabels=1)
        plt.subplots_adjust(bottom=0.21, top=0.98)
        plt.show()
    else:
        logging.warning("Combined PTEN correlation file not found.")


def run():
    """
    """
    show_heatmap()
