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


from printthings import *
from issueapi import *

# Very rudimentary CLI

print "Give type of thing (task, requirement or intent)"
print ""
entity = raw_input()
print "Give its id"
print ""
id = raw_input()
if len(id) == 1: # if id is < 10 and missing the leading 0, add it
    id = '0'+ id

print "This " + entity + " is:"
print ""
print get_one(entity, id) # print thing itself
print ""
print "-------------------------------------"
print ""
print "This " + entity + " is associated with:"
print ""

if entity == 'requirement':
    requirement = entity + '_' + id
    print_one_issue(requirement) # print anything it's related to
else:
    print_task_or_intent(entity, id)

# there should be some way of getting an entity by name so user
# can fill out mapping.yaml. Though they can always grep...

