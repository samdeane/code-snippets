#!/bin/sh

# Build the doxygen documentation for the project and load the docset into Xcode.
#
# Tweaked by Sam Deane from an original script here:
# http://developer.apple.com/tools/creatingdocsetswithdoxygen.html

# We expect the variable DOXYGEN_ID to be set to a product id for the docset:
# for example: com.elegantchaos.myapp. You should set this variable in your
# project, or in the Run Script build step.
#
# Launch this script from a Run Script build step like this:
# /path/to/script/build-doxygen.sh > "$TEMP_DIR/doxygen.output.log" 2> "$TEMP_DIR/doxygen.log" &

# We expect to find the doxygen executable at /usr/local/bin/doxygen.
# If you've got it installed as a binary app, you might want to symbolic link it
# like this:
# ln -s /Applications/Doxygen.app/Contents/Resources/doxygen /usr/local/bin/doxygen
DOXYGEN_PATH=/usr/local/bin/doxygen

# We expect to find a Doxygen config file in $SOURCE_ROOT/Code/doxygen.config
DOXYGEN_CONFIG="$SOURCE_ROOT/Code/doxygen.config"

# We're going to build the documentation into a fixed location relative to the project
# then copy it into the user's library later
mkdir -p "$SOURCE_ROOT/build/documentation"
DOCSET_OUTPUT="$SOURCE_ROOT/build/documentation/DoxygenDocs.docset"

# Make a copy of the config file.
# Then append the proper input/output directories and docset info to the config file.
# This works even though values are assigned higher up in the file. Easier than fiddling with the config file with sed.
TEMP_CONFIG="$TEMP_DIR/doxygen.config"
cp "$DOXYGEN_CONFIG" "$TEMP_CONFIG"
echo "INPUT = \"$SOURCE_ROOT\"" >> "$TEMP_CONFIG"
echo "OUTPUT_DIRECTORY = \"$DOCSET_OUTPUT\"" >> "$TEMP_CONFIG"

#  Run doxygen on the updated config file.
$DOXYGEN_PATH "$TEMP_CONFIG"

# Doxygen has created a Makefile that does most of the heavy lifting.
# make will invoke docsetutil. All we need to do is invoke it.

# If you want to take a look at the Makefile to see what it does, uncomment the line below
#cp "$DOCSET_OUTPUT/html/Makefile" "/Users/$USER/Desktop/MakefileBackup"

# Run the makefile. The --silent parameter stops it from spamming us with too much output.
make --silent -C "$DOCSET_OUTPUT/html" install

#  Construct a temporary applescript file to tell Xcode to load the docset.
rm -f "$TEMP_DIR/loadDocSet.scpt"
touch "/Users/$USER/Library/Developer/Shared/Documentation/DocSets/$DOXYGEN_ID.docset/Contents/Info.plist"
echo "tell application \"Xcode\"" >> "$TEMP_DIR/loadDocSet.scpt"
echo "load documentation set with path \"/Users/$USER/Library/Developer/Shared/Documentation/DocSets/$DOXYGEN_ID.docset\"" 
     >> "$TEMP_DIR/loadDocSet.scpt"
echo "end tell" >> "$TEMP_DIR/loadDocSet.scpt"

#  Run the load-docset applescript command.
osascript "$TEMP_DIR/loadDocSet.scpt"

exit 0