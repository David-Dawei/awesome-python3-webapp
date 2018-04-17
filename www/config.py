# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:47:46 2018

@author: wdw
"""
import config_default


def merge(d0,d1):
    d=d0
    for k, v in d0.items():
        if k in d1:
            if isinstance(v,dict):
                d[k] = merge(v,d1[k])
            else:
                d[k] = d1[k]
    return d


configs = config_default.configs
try:
    import config_override
    configs = merge(configs,config_override.configs)
except ImportError:
    pass