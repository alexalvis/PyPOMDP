# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:42:23 2022

@author: hma2
"""

import argparse
import os
import json
import multiprocessing
from pomdp_runner import PomdpRunner
from util import RunnerParams
from test_simulator import Simulator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve pomdp')
    parser.add_argument('config', type=str, help='The file name of algorithm configuration (without JSON extension)')
    parser.add_argument('--env', type=str, default='GridWorld.POMDP', help='The name of environment\'s config file')
    parser.add_argument('--budget', type=float, default=float('inf'), help='The total action budget (defeault to inf)')
    parser.add_argument('--snapshot', type=bool, default=False, help='Whether to snapshot the belief tree after each episode')
    parser.add_argument('--logfile', type=str, default=None, help='Logfile path')
    parser.add_argument('--random_prior', type=bool, default=False,
                        help='Whether or not to use a randomly generated distribution as prior belief, default to False')
    parser.add_argument('--max_play', type=int, default=100, help='Maximum number of play steps')

    args = vars(parser.parse_args())
    params = RunnerParams(**args)
    
    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        trajlist = []
        for i in range(10):
            simulator = Simulator(params)
            traj = simulator.simulate(**algo_params)
            trajlist.append(traj)