#!/bin/bash
# Script to generate README.md file
set -e -u -o pipefail

func_def_table=$(cat ../pcof/pcof.py |
    sed -n '/^def/{:a;/    [r]\?""" *$/!{N;ba;};N;s/\n//g;s/  */ /g;p;}' |
    sed 's/^def \([^(]*\).*"""\(.*\)/| \1 | \2 |/')
func_dec_table=$(cat ../pcof/decorators.py |
    sed -n '/^def/{:a;/    [r]\?""" *$/!{N;ba;};N;s/\n//g;s/  */ /g;p;}' |
    sed 's/^def \([^(]*\).*"""\(.*\)/| \1 | \2 |/')

# add ```python to pydoc output
sed_pydoc="
    1i\`\`\`
    /^FUNCTIONS/a\`\`\`\\n\\n\`\`\`python
    s/^  *\$//g
    \$a\`\`\`
    /^\(FILE\|DATA\) *\$/,\$d"

##################################################
# Create README.md
##################################################
cat <<EOF > ../README.md
$(cat header.md)

## Usage Example

$(cat example.md)

## List of available functions

### Functions

| Name | Description |
|:-----|:------------|
$func_def_table

### Decorators

| Name | Description |
|:-----|:------------|
$func_dec_table

## Documentation (automatically generated using pydoc)

$(pydoc ../pcof/pcof.py       | sed "$sed_pydoc")

$(pydoc ../pcof/decorators.py | sed "$sed_pydoc")
\
EOF
