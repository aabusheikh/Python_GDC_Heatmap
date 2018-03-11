# Copyright (C) 2018  Ahmad A. A. (https://github.com/bbpgrs/)

import pandas as pd
import common as cmn
import os
import logging


def combine_corr_files():
    """
    """    
    combined_file_path = os.path.join(cmn.DL_DIR, cmn.PTEN_CORR_FNAME)    
    gene_list = [l[0] for l in pd.read_csv(cmn.GENE_REF_FILE, sep="\t", index_col=0).values[:20].tolist()]
    with open(combined_file_path, 'w') as out_file:
        out_file.write("\n".join(["0"]+list(gene_list)))

    cdf = pd.read_csv(combined_file_path, sep="\t", index_col=0)
    i = 0

    for cancer_type in cmn.list_dir(cmn.DL_DIR):
        for gender in cmn.list_dir(os.path.join(cmn.DL_DIR, cancer_type)):
            logging.info("Reading correlation files for '%s' > '%s' ..." % (cancer_type, gender))

            samples_path = os.path.join(cmn.DL_DIR, cancer_type, gender)            

            corr_file = cmn.CORR_FNAME % (cancer_type.lower(), gender.lower(), "rna", "normalized")
            corr_file_path = os.path.join(samples_path, corr_file)

            if os.path.isfile(corr_file_path):
                logging.info("Found correlation file, processing ...\n")

                df = pd.read_csv(corr_file_path, sep="\t", index_col=0)
                ver_dict = {key: value for (key, value) in [cc.split(".") for cc in df.index.values]}

                entries = [df.loc[".".join((gene_code, ver_dict[gene_code]))][0] for gene_code in gene_list]
                cdf.insert(i, "%s-%s" % (cancer_type, gender), entries)
                i += 1

                logging.info("Done.\n")

            else:
                logging.warning("No correlation file found for '%s' > '%s'.\n" % (cancer_type, gender))

    logging.info("Writing file ...")
    cdf.to_csv(combined_file_path, sep="\t")


def run():
    """
    """
    combine_corr_files()
