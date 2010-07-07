# Fetch latest version of a module using git subtree
# (C) 2010 Sam Deane, Elegant Chaos.
#
# Feel free to copy, modify and generally hack these scripts to death. 
# Please let me know about any improvements you make to them!
# http://www.elegantchaos.com

if [ -e "./.git" ]
then
	source "subtrees/$1.subtree"
	git fetch "${TREE}"
	git subtree merge -P "${LOCAL}" --squash "${TREE}/master"
else
	echo Run this script from the root of the repository
fi

