#!/usr/bin/env python

import ecprocess
import ecshell
import sys
import ecsettings
import os
import re

def GetShortOptions():
	return ""

def GetLongOptions():
	return ['force']


def CommandNeedsSubtree(command):
	return command in ['log', 'add', 'pull', 'push', 'fetch', 'commit']

def DoCommand_log(args, options):
	output = ecprocess.Output('git', "log", local)
	return output


def FetchRemote():
	output = ecprocess.Output('git', 'fetch', tree)

	return output


def LoadSubtreeSettings(path):
	global local
	global tree
	global url
	global treemaster

	if not os.path.exists(path):
		output = "Subtree '" + subtree + "' doesn't exist."
		
	else:

		settings = ecsettings.Load(path)
		local = settings['LOCAL']
		tree = settings['TREE']
		url = settings['URL']
		treemaster = tree + '/master'
		output = ""

	return output


def PreflightCommand(command, args, options):
	output = ""
	if CommandNeedsSubtree(command):
		if (len(args) < 2):
			output = "No subtree specified."
	
		else:
			subtree = args[1]
			path = os.path.join(root, "subtrees", subtree + ".subtree")
			output = LoadSubtreeSettings(path)
				
	return output


def DoCommand_add(args, options):
	if ('force' in options) or (not os.path.exists(local)):
		output = ecprocess.Output('git', 'remote', 'add', tree, url)
		output += FetchRemote()
		output += ecprocess.Output('git', 'subtree', 'add', '--prefix=' + local, '--squash', treemaster)
	else:
		output = "Directory " + local + " already exists."

	return output


def DoCommand_fetch(args, options):
	output = FetchRemote()
	output += ecprocess.Output('git', 'subtree', 'merge', '--prefix=' + local, '--squash', treemaster)

	return output


def DoCommand_pull(args, options):
	output = FetchRemote()
	output += ecprocess.Output('git', 'subtree', 'pull', '--prefix=' + local, '--squash', tree)
	
	return output

def DoCommand_commit(args, options):
	output = ecprocess.Output('git', 'commit', local)
	
	return output


def DoCommand_push(args, options):
	output = ecprocess.Output('git', 'subtree', 'split', '--prefix=' + local, '-b', tree + '-subtree')
	output += ecprocess.Output('git', 'push', tree, tree + '-subtree:master')
	output += ecprocess.Output('git', 'subtree', 'pull', '--prefix=' + local, '--squash', tree)
	
	return output


root = os.getcwd()

gitroot = os.path.join(root, ".git")

if not os.path.exists(gitroot):
	print "Run this script from the root of the repository."
	
else:
	status = ecprocess.Output('git', 'status', '--porcelain', '--untracked=no')
	if status != "":
		print "Working tree has modifications. Sort them out first!\n"
		print status
	
	else:
		print ecshell.Run(sys.argv)
