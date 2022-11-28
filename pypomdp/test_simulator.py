# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:32:43 2022

@author: 53055
"""

import os

from models import RockSampleModel, Model
from solvers import POMCP, PBVI
from parsers import PomdpParser, GraphViz
from logger import Logger as log

class Simulator():
    def __init__(self, params):
        self.params = params
        if params.logfile is not None:
            log.new(params.logfile)
    
    def create_model(self, env_configs):
        """
        Builder method for creating model (i,e, agent's environment) instance
        :param env_configs: the complete encapsulation of environment's dynamics
        :return: concrete model
        """
        MODELS = {
            'RockSample': RockSampleModel,
        }
        return MODELS.get(env_configs['model_name'], Model)(env_configs)
    
    def create_solver(self, algo, model):
        """
        Builder method for creating solver instance
        :param algo: algorithm name
        :param model: model instance, e.g, TigerModel or RockSampleModel
        :return: concrete solver
        """
        SOLVERS = {
            'pbvi': PBVI,
            'pomcp': POMCP,
        }
        return SOLVERS.get(algo)(model)
    def snapshot_tree(self, visualiser, tree, filename):
        visualiser.update(tree.root)
        visualiser.render('./dev/snapshots/{}'.format(filename))  # TODO: parametrise the dev folder path
    
    def simulate(self, algo, T, **kwargs):
        visualiser = GraphViz(description='tmp')
        params, pomdp = self.params, None
        total_rewards, budget = 0, params.budget
        
        with PomdpParser(params.env_config) as ctx:
            # creates model and solver
            model = self.create_model(ctx.copy_env())
            pomdp = self.create_solver(algo, model)

            # supply additional algo params
            belief = ctx.random_beliefs() if params.random_prior else ctx.generate_beliefs()

            if algo == 'pbvi':
                belief_points = ctx.generate_belief_points(kwargs['stepsize'])
                pomdp.add_configs(belief_points)
            elif algo == 'pomcp':
                pomdp.add_configs(budget, belief, **kwargs)
        log.info('''
        ++++++++++++++++++++++
            Starting State:  {}
            Starting Budget:  {}
            Init Belief: {}
            Time Horizon: {}
            Max Play: {}
        ++++++++++++++++++++++'''.format(model.curr_state, budget, belief, T, params.max_play))
        
        for i in range(params.max_play):
            actions = model.get_legal_actions(model.curr_state)
            action = choose_action(actions)