#!/usr/bin/env python

from issueapi import *

def print_all_issues():
    for requirement, tasks_and_intents in mappings.iteritems():
        requirement_id = requirement.split('_', 1)[-1]
        print ""
        print "------------------------------------"
        print "Requirement:"
        print ""
        print get_one("requirement", requirement_id)
        for i in tasks_and_intents:
            for key, values in i.iteritems():
                entity = key
                for value in values:
                    id = str(value)
                    print ""
                    print entity + ":"
                    print ""
                    print get_one(entity, id)
                    print ""
                    print ""

def print_one_issue(our_requirement):
    for requirement, tasks_and_intents in mappings.iteritems():
        if requirement == our_requirement:
            requirement_id = requirement.split('_', 1)[-1]
            print "Requirement:"
            print ""
            print get_one("requirement", requirement_id)
            print ""
            for i in tasks_and_intents:
                for key, values in i.iteritems():
                    entity = key
                    for value in values:
                        id = str(value)
                        print entity + ":"
                        print ""
                        print get_one(entity, id)
                        print ""
                        print ""

def print_task_or_intent(entity, id):
    for requirement, tasks_and_intents in mappings.iteritems():
        for thing in tasks_and_intents:
            for keys, values in thing.iteritems():
                if entity in keys and id in values:
                    print_one_issue(requirement)

