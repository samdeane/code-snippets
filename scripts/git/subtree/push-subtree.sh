# Push the latest changes to a module using git subtree
# (C) 2010 Sam Deane, Elegant Chaos.
#
# Feel free to copy, modify and generally hack these scripts to death. 
# Please let me know about any improvements you make to them!
# http://www.elegantchaos.com

if [ -e "./.git" ]
then
	source "subtrees/$1.subtree"
	git subtree split -P "${LOCAL}" -b "${TREE}-push"
	git push "${TREE}" "${TREE}-push:master"
else
	echo Run this script from the root of the repository
fi


