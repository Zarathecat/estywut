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

