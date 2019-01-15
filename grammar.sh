#source: https://github.com/eleven-labs/blog.eleven-labs.com/blob/master/bin/check-spelling.sh 
# requires apt packages: hunspell, myspell-it, myspell-en-us
#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;36m'
NC='\033[0m' # No Color

#word count for .dictionary.dic
cat .dictionary.dic | wc -l > dictionaryApp.dic
cat .dictionary.dic >> dictionaryApp.dic
cat dictionaryApp.dic > .dictionary.dic

#only diff files
#TEX_FILES_CHANGED=`(git diff --name-only $TRAVIS_COMMIT_RANGE || true) | grep .md`
#all file check
TEX_FILES_CHANGED=`git ls-files | grep "tex"`

if [ -z "$TEX_FILES_CHANGED" ]
then
    echo -e "$GREEN>> No TEX file to check $NC"

    exit 0;
fi

echo -e "$BLUE>> Following tex files were changed in this pull request (commit range: $TRAVIS_COMMIT_RANGE):$NC"
echo "$TEX_FILES_CHANGED"

USE_LANGUAGE='it_IT,en_US,.dictionary'
echo -e "$BLUE>> Will use this language as main one:$NC"
echo "$USE_LANGUAGE"

# cat all markdown files that changed
#TEXT_CONTENT_WITHOUT_METADATA=`cat $(echo "$MARKDOWN_FILES_CHANGED" | sed -E ':a;N;$!ba;s/\n/ /g')`
# remove metadata tags
#TEXT_CONTENT_WITHOUT_METADATA=`echo "$TEXT_CONTENT_WITHOUT_METADATA" | grep -v -E '^(layout:|permalink:|date:|date_gmt:|authors:|categories:|tags:|cover:)(.*)'`
# remove { } attributes
#TEXT_CONTENT_WITHOUT_METADATA=`echo "$TEXT_CONTENT_WITHOUT_METADATA" | sed -E 's/\{:([^\}]+)\}//g'`
# remove html
#TEXT_CONTENT_WITHOUT_METADATA=`echo "$TEXT_CONTENT_WITHOUT_METADATA" | sed -E 's/<([^<]+)>//g'`
# remove code blocks
#TEXT_CONTENT_WITHOUT_METADATA=`echo "$TEXT_CONTENT_WITHOUT_METADATA" | sed  -n '/^\`\`\`/,/^\`\`\`/ !p'`
# remove links
#TEXT_CONTENT_WITHOUT_METADATA=`echo "$TEXT_CONTENT_WITHOUT_METADATA" | sed -E 's/http(s)?:\/\/([^ ]+)//g'`
TEXT_CONTENT=`cat $(echo "$TEX_FILES_CHANGED")`

echo -e "$BLUE>> Checking in '$USE_LANGUAGE'"
MISSPELLED=`echo "$TEXT_CONTENT" | hunspell -d "$USE_LANGUAGE" --encoding=UTF-8 -t -l | sort -u`

NB_MISSPELLED=`echo "$MISSPELLED" | wc -l`
echo "$NB_MISSPELLED $MISSPELLED"
if [ "$NB_MISSPELLED" -gt 0 ]
then
    echo -e "$RED>> Words that might be misspelled, please check:$NC"
    MISSPELLED=`echo "$MISSPELLED" | sed -E ':a;N;$!ba;s/\n/, /g'`
    COMMENT="$NB_MISSPELLED words might be misspelled, please check them: $MISSPELLED"
    echo -e "$COMMENT"
    RETURN_STATUS=1
else
    COMMENT="No spelling errors, congratulations!"
    echo -e "$GREEN>> $COMMENT $NC"
    RETURN_STATUS=0
fi

echo -e "$BLUE>> errors"

exit $RETURN_STATUS
