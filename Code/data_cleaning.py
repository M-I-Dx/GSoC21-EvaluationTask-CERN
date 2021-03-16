import numpy as np
import pandas as pd 

raw_data = "Data/monojet_Zp2000.0_DM_50.0_chan3.csv"


def data_conversion(dataset):
    with open(dataset, 'r') as temp_f:
        col_count = [len(l.split(",")) for l in temp_f.readlines()]
    column_names = [i for i in range(max(col_count))] 

    data = pd.read_csv(dataset, header = None, names=column_names, sep=";")
    data = data.drop([0, 1, 2, 3, 4], axis=1)
    data.columns = range(len(data.columns))

    dataset_clean = []
    for i in range(len(data.columns)):
        for j in range(len(data.index)):
            if not pd.isna(data[i][j]):
                data_pt = [j] + data[i][j].split(',')
                if data_pt[1] == 'j':
                    dataset_clean.append(data_pt)
    dataset_clean = pd.DataFrame(dataset_clean, columns=["Experiment", "Particle", "E1", "pt1", "eta1", "phi1"])
    dataset_clean.to_csv("Data/Dataset.csv", index=False)


data_conversion(raw_data)