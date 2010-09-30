#!/usr/bin/env python

# (C) 2010 Sam Deane, Elegant Chaos. All rights reserved.
# Licensed under the terms of the BSD License, as specified below.
#
# Feel free to copy, modify and generally hack these scripts to death. 
# Please let me know about any improvements you make to them!
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 
# * Neither the name of Elegant Chaos nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import getopt
import __main__

def DoCommand_help(args, options):
	if (len(args) > 0):
		command = args[0]
		try:
			result = eval('__main__.GetCommandHelp_'  + command + '(options)')
		except:
			result = "No help for command: " + command
	else:
		result = "Which command do you want help on?"

	return result


def Run(args):
	shortOpts = __main__.GetShortOptions()
	longOpts = __main__.GetLongOptions()
	
	(options, args) = getopt.gnu_getopt(args[1:], shortOpts, longOpts)
	if (len(args) > 0):
		command = args[0]
		
		output = __main__.PreflightCommand(command, args, options)
		if output:
			result = output 
		
		else:
			try:
				result = eval('__main__.DoCommand_'  + command + '(args[1:], options)')
			except AttributeError:
				try:
					result = eval('DoCommand_'  + command + '(args[1:], options)')
				except AttributeError:
					result = "Unknown command: " + command

	else:
		result = "Usage: " + sys.argv[0] + " <command>"
					
	return result
