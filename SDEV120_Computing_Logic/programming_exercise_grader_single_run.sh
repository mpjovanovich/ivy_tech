#!/usr/bin/env bash

##############################################################################
## Get the program inputs.
##############################################################################
read -p "Test run prefix: " test_name
read -p "Student files path: " student_file_path
read -p "Number of program inputs: " num_program_inputs 

out_path=${student_file_path}/out
tmp_path=${student_file_path}/tmp

## May fail, but who cares.
#rm -r $out_path
mkdir $out_path
rm -r $tmp_path
mkdir $tmp_path

touch ${tmp_path}/$test_name
for(( j = 1; j <= $num_program_inputs; j++ ));
do
	read -p "Input value, input $j: " input_value
	echo $input_value >> ${tmp_path}/$test_name
done


##############################################################################
## Create the student file runs.
##############################################################################

for student_file in $student_file_path/*
do
    if [ ! -f "$student_file" ]; then
        continue
    fi

    ## Use parameter expansion to only return the file name - not the full path.
    ## Store it in a variable.
    student_name=$(echo "${student_file##*/}" | cut -d '_' -f 1)
    student_log_path=${out_path}/${student_name}_${test_name}.txt

    ## Change terminal new line from CRLF to LF, then change back after the script
    stty -opost

	## cat tmp file to bash | read one line at a time with a pause in between | print 
	## to stdout and pipe to the student file > redirect stdout to /dev/null
	script -c "cat ${tmp_path}/$test_name | { while read l ; do sleep .1; echo \$l; done } | \
		tee >(python3 \"$student_file\")" -O ${student_log_path} > /dev/null
	## The -q option doesn't seem to work in script, so we need to remove the first and last lines
	tail -n +2 ${student_log_path} | head -n -1 > ${tmp_path}/{$test_name}_out
	mv ${tmp_path}/{$test_name}_out ${student_log_path}

    stty opost

done
