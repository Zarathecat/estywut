#!/usr/bin/env python

# Copyright 2017 Codethink Limited

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import yaml
import os
import glob
import sys

""" This utility provides information about the tasks, requirements and
intents recorded in this repo, and the relations between them. 
The runnable script currently requires the user to submit a type
of entity (task, requirement or intent) and its ID in order to get
further information. At the moment, the script must be run from this
directory, as the path to 'mapping' is relative."""


def get_mappings():
    """ parse yaml content of mappings file, which defines relationships between
    our entities (intent, requirement and task), and return it """
    mappings_file = "../mappings/mappings.yaml"
    with open(mappings_file) as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as e:
            print e


def get_all(entity):
    """ parse all yaml files describing entities of a certain type (intent,
    requirement or task) and return a list of all instances of the entity.
    """
    entity = str(entity)
    instances = []
    for filename in glob.glob("../" + entity + "/*.yaml"):

        with open(filename) as stream:
            try:
                instances.append(yaml.load(stream))
            except yaml.YAMLError as e:
                print e
    return instances


def get_one(entity, id):
    """ parse the yaml file of the relevant type (intent, requirement, task)
    with the matching id, and return its content. """
    filename = "../" + entity + "/" + entity + "_" + id + ".yaml"
    with open(filename) as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as e:
            print e

mappings =  get_mappings()
