#!/usr/bin/env python

import yaml
import os
import glob

mappings = 

def print_entity(entity):
    for filename in glob.glob("../" + entity + "/*.yaml"):

        with open(filename) as stream:
            try:
                print yaml.load(stream)
            except:
                pass

print_entity("worklists")
