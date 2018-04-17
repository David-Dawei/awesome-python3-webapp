# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:47:46 2018

@author: wdw
"""
import config_default

class Dict(dict):
    '''
    simple dict but support access as x.y style
    '''
    def __init__(self,names=(), values=(), **kw):
        super(Dict,self).__init__(**kw)
        for k, v in zip(names,values):
            self[k] = v
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute %s " % key)
    def __setattr__(self,k,v):
            self[k] = v

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

def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v,dict) else v
    return D

configs = toDict(configs)
