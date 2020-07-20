# quickedit
a program I use to edit files that I edit frequently e.g. config file, to avoid cd'ing.

Files to edit are stored as name:file pair.
e.g. bash : ~/.bashrc

python -a <name> <relative_path_of_the_file>   : to add a new pair <br>
python -l                              : list the entries
python -e <name>                       : edit <name>, (default editor: vim)
python -rm <name>                      : remove and entry
