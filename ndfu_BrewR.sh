#!/bin/bash

find "./BrewR/" "./BrewR_2/" "./BrewR_3/" -type f -exec md5sum '{}' \+ | sort > ./BrewR_file_hashes.txt

`awk '{a[$1]++}END{for (i in a)if (a[i]>1)print i;}' ./BrewR_file_hashes.txt > ./BrewR_dupe_keys.txt`

grep -f ./BrewR_dupe_keys.txt ./BrewR_file_hashes.txt > ./BrewR_dupes.txt

grep './BrewR_' BrewR_dupes.txt > ./BrewR_files_to_delete.txt

echo -e '#!/bin/bash\n\n' > BrewR_dupe_removal_script.sh

awk -F "  " '{print "trash --verbose \""$2"\" "}' ./BrewR_files_to_delete.txt >> BrewR_dupe_removal_script.sh
