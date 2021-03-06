import os
import sys

# Generates the file list.go with all processors

header = """/*
Package include imports all processor packages so that they register with the global
registry. This package can be imported in the main package to automatically register
all of the standard supported apm-server processors.
*/
package include

import (
\t// This list is automatically generated by `make imports`
"""


def generate(go_beat_path):

    base_dir = "processor"
    path = os.path.abspath("processor")
    list_file = header

    # Fetch all protocols
    for protocol in sorted(os.listdir(base_dir)):
        if protocol == "model":
            continue

        if os.path.isfile(path + "/" + protocol):
            continue

        list_file += '	_ "' + go_beat_path + '/processor/' + protocol + '"\n'

    list_file += ")"

    # output string so it can be concatenated
    print(list_file)


if __name__ == "__main__":
    # First argument is the beat path under GOPATH.
    # (e.g. github.com/elastic/beats/packetbeat)
    go_beat_path = sys.argv[1]

    generate(go_beat_path)
