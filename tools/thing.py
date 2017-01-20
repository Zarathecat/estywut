#!/usr/bin/env python

import yaml
import os
import glob

def get_mappings():
    mappings_file = "../mappings/mappings.yaml"
    with open(mappings_file) as stream:
        try:
            return yaml.load(stream)
        except:
            pass


def get_all(entity):
    for filename in glob.glob("../" + entity + "/*.yaml"):

        with open(filename) as stream:
            try:
                return yaml.load(stream)
            except:
                pass

def get_one(entity, id):
    filename = "../" + entity + "/" + entity + "_" + id + ".yaml"
    with open(filename) as stream:
        try:
            return yaml.load(stream)
        except:
            pass

mappings =  get_mappings()


for key, value in mappings.iteritems():
    story = key
    story_id = story.split('_', 1)[-1]
    tasks_and_worklists = value
    print "Requirements:"
    print ""
    print get_one("story", story_id)
    for i in tasks_and_worklists:
        for key, values in i.iteritems():
            entity = key
            for value in values:
                id = str(value)
                print entity + ":"
                print get_one(entity, id)
