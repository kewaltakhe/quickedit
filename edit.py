#!/usr/bin/env python

import argparse
import json
import pathlib
import sys
import os
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('-e','--edit', dest='config' , help='a config to edit')
parser.add_argument('-a', '--add', dest='new_entry', nargs=2,  help='add config and file with relative path')
parser.add_argument('-l', '--list', help='list all entries', action='store_true')
parser.add_argument('-rm', '--remove', dest='rmentry', help='remove an entry',)

args = parser.parse_args()

#if no argument if given
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# ed_save: updates ed.json by dumping ed_dict into it
def ed_save():
    with open('ed.json','w') as jp:
        json.dump(ed_dict,jp)


# ed.json
# ed_dict: global variable loaded with the content of ed.json

try:
    with open('ed.json','r+') as jp:
        ed_dict = json.load(jp)
except json.decoder.JSONDecodeError:
    ed_dict = {}

# list the entries
if args.list:
    pprint(ed_dict)


# adding a new pair;; update ed_dict, ed_save()

if args.new_entry:
    filepath = pathlib.Path(args.new_entry[1]).expanduser()
    if not (filepath.exists() and filepath.is_file()):
        print('config file does not exists')
        sys.exit(1)
    ed_dict[args.new_entry[0]] = str(filepath)
    ed_save()



# edit a config
if args.config:
    try:
        configfile = ed_dict[args.config]
        child_pid = os.fork()
        is_child = child_pid == 0
        editor="vim"
        if is_child:
            os.execvp(editor,[editor,configfile])
        else:
            os.waitpid(child_pid, 0)
            
        
    except KeyError:
        print('no entry found for %s.'%(args.config))

# remove an entry
if args.rmentry:
    try:
        del ed_dict[args.rmentry]
        ed_save()
    except KeyError:
        print('no entry found for %s.'%(args.config))

        
