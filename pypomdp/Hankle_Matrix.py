# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 00:07:28 2022

@author: 53055
"""

from splearn.datasets.base import load_data_sample
from splearn.spectral import Spectral
from splearn  import Hankel
from splearn.automaton import Automaton

def Hankel_Matrix(filename):
    train = load_data_sample(adr = filename)
    
    est = Spectral()
    # est.set_params(lrows = 3, lcolumns = 3, smooth_method = 'trigram', version = 'factor', rank = 8)
    est.fit(X = train.data)
    # print(est.automaton.transitions)
    # print(train.fact)
    lhankel = est.hankel
    # WA = est.automaton
    WA = lhankel.to_automaton(rank = 8)
    print(WA.transitions)
    
    return lhankel, WA

if __name__ == "__main__":
    filename = "Test_store_noact.json"
    # filename = "0.spice.train"
    # auto = Automaton.SimpleExample()
    # print(auto.transitions)
    lhankel, WA = Hankel_Matrix(filename)