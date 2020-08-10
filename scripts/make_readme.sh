#!/bin/bash
# Script to generate README.md file
set -e -u -o pipefail

FMT_TABLE='
# check if there are dependencies and store it on hold space
/^Dependencies/ {
    s/.*://
    h
}
/^def/ {
    :a
    /    [r]\?""" *$/ !{
        N
        b a
    }
    N
    s/\n//g
    s/  */ /g
    s/^def \([^(]*\).*"""\(.*\)/| \1 | \2 |/
    G
    s/|\n$/| - |/ # there is no dependency
    s/\(.*\)|\n\(.*\)/\1|\2 |/ # there is dependency
    p
}
'

FUNC_FILES="../pcof/pcof.py
../pcof/printtable.py
../pcof/pytz.py
../pcof/downloadfile.py"
FUNC_DECOR_FILES="../pcof/decorators.py"

# create markdown tables
func_def_table=$(
for i in $FUNC_FILES;do
    f="$(echo ${i##*/} | sed 's/.py$//')"
    sed -n "$FMT_TABLE" "$i" | sed "s/^/| $f /";
done)

func_dec_table=$(
for i in $FUNC_DECOR_FILES; do
    f="$(echo ${i##*/} | sed 's/.py$//')"
    sed -n "$FMT_TABLE" "$i" | sed "s/^/| $f /";
done)

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

| Module | Name | Description | Dependencies |
|:-------|:-----|:------------|:-------------|
$func_def_table

### Decorators

| Module | Name | Description | Dependencies |
|:-------|:-----|:------------|:-------------|
$func_dec_table

## Documentation (automatically generated using pydoc)

$(for i in $FUNC_FILES; do pydoc "$i" | sed "$sed_pydoc"; done)

$(for i in $FUNC_DECOR_FILES; do pydoc "$i" | sed "$sed_pydoc"; done)
\
EOF
