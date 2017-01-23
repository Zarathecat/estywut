This is a python yaml parser for the content of this repo, so that
it's easier to read info. There's currently a ropey CLI. Here is
some sample output when given the arguments 'intent' and '01':

.........................................................................................
.........................................................................................

This intent is:

{'artifacts': {'artifact_01': {'link': 'big-binary-file.example.org',
'hash': 'shashum256somethingorother', 'description': 'picture of a cat'}},
'created_at': None, 'title': 'Fix everything',
'description': 'Everything is broken and we have been given lots of cash to fix it',
'id': 1}

-------------------------------------

This intent is associated with:

Requirement:

{'created_at': None, 'title': 'Fix the first broken thing',
'description': 'The first thing is broken; we should fix it
\nHere are the logs:\nfoo foo foo\nbar bar bar\nbaz baz\n', 'id': 1}

task:

{'priority': 'HIGH', 'assignee_id': None, 'link': 'https://review.whatever.org',
'notes': "the foobar fails to compile with error 'xys452'. Going to try kicking it.",
'title': 'get foobar to compile', 'created_at': None, 'id': 1}


task:

{'priority': 'HIGH', 'assignee_id': None, 'link': 'https://review.whatever.org/02',
'notes': "the barbaz also fails to compile with error 'xys452'.
some guy on the internet says kicking doesn't work, but throwing it out of the
window has given him success in the past. we should try that ", 
'title': 'get barbaz to compile', 'created_at': None, 'id': 2}


intent:

{'artifacts': {'artifact_01': {'link': 'big-binary-file.example.org',
'hash': 'shashum256somethingorother', 'description': 'picture of a cat'}},
'created_at': None, 'title': 'Fix everything',
'description': 'Everything is broken and we have been given lots of cash to fix it',
 'id': 1}

............................................................................................
............................................................................................
