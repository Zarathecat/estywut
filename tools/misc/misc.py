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
from issueinfo import *

# If we have a better api later, we probably want a class-based thing
# This is a skeleton.

class Issue():
    def __init__(self):
        self.intent = []
        self.requirement = []
        self.task = []

# makes an issue a class. not sure about the best way of getting
# something by id yet.
def get_one_issue(our_requirement):
    this_issue = Issue()
    for requirement, tasks_and_intents in mappings.iteritems():
        if requirement == our_requirement:
            requirement_id = requirement.split('_', 1)[-1]
            this_issue.requirement.append(get_one("requirement", requirement_id))
            for i in tasks_and_intents:
                for key, values in i.iteritems():
                    entity = key
                    for value in values:
                        id = str(value)
                        if entity == "task":
                            this_issue.task.append(get_one(entity,id))
                        else:
                            this_issue.intent.append(get_one(entity, id))
    return this_issue

# populate all issues with classes
def make_classes_of_issues(mappings):
    issues = []

    for issue, values in mappings.iteritems():
        desc = vars(get_one_issue(issue))
        issues.append(desc)
    return issues

