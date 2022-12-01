# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:25:17 2022

@author: hma2
"""

import numpy as np
import json

def data_transfer(trajlist, st_len):
    store_data = []
    store_data.append([len(trajlist)])
    symbol_dict = {}
    max_len = 0
    for i in range(st_len):
        symbol_dict[str(i)] = i
    symbol_index = st_len
    for i in range(len(trajlist)):
        transfer_traj = [len(trajlist[i])]
        max_len = np.maximum(max_len, len(trajlist[i]))
        for j in range(len(trajlist[i])):
            if trajlist[i][j] not in symbol_dict.keys():
                symbol_dict[trajlist[i][j]] = symbol_index
                symbol_index += 1
            transfer_traj.append(int(symbol_dict[trajlist[i][j]]))
        store_data.append(transfer_traj)
    store_data[0].append(int(max_len))
    return store_data, symbol_dict

def store_json(data, filename):
    outputfile = open(filename, "w")
    for line in data:
        for i in range(len(line)): 
            outputfile.write(str(line[i]) + ' ')
        outputfile.write('\n')
    outputfile.close()