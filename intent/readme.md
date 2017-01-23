'epics', or in this workflow, 'intents'

the 'artifacts' field is there as users *frequently* want to attach
files to bug reports. we can't track them in git (could be big and/or
binaries, neither of which git likes), but if we want them tracked in
the repo, a symlink and standard metadata isn't enough (could be spoofed).
so, we include a hash of the file, so it's at least possible to check
if it has changed at the linked destination. Though I'm not sure if it'd
be affected by 'last-accessed-at' or something. hm. I don't know much
about file hashes.
