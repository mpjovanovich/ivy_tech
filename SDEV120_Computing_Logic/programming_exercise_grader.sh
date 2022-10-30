#!/usr/bin/env bash

##############################################################################
## Get the program inputs.
##############################################################################
read -p "Grade program path: " grade_program_path
read -p "Student files path: " student_file_path
read -p "Number of program runs: " num_program_runs
read -p "Number of program inputs: " num_program_inputs 

out_path=${student_file_path}/out
tmp_path=${student_file_path}/tmp
solution_log_path=${out_path}/solution_log
rm -r $out_path
mkdir $out_path
rm -r $tmp_path
mkdir $tmp_path

for(( i = 1; i <= $num_program_runs; i++ ));
do
    touch ${tmp_path}/tmp${i}
    for(( j = 1; j <= $num_program_inputs; j++ ));
    do
        read -p "Input value, run $i, input $j: " input_value
        echo $input_value >> ${tmp_path}/tmp${i}
    done
done

##############################################################################
## Create the answer key.
##############################################################################

## Change terminal new line from CRLF to LF, then change back after the script
stty -opost
for(( i = 1; i <= $num_program_runs; i++ ));
do
    ## cat tmp file to bash | read one line at a time with a pause in between | print to stdout and pipe 
    ## to the solution file > redirect stdout to /dev/null
    script -c "cat ${tmp_path}/tmp${i} | { while read l ; do sleep .1; echo \$l; done } | tee >(python3 $grade_program_path)" \
        -O ${solution_log_path}${i} > /dev/null
    ## The -q option doesn't seem to work in script, so we need to remove the first and last lines
    tail -n +2 ${solution_log_path}${i} | head -n -1 > ${tmp_path}/tmp 
    mv ${tmp_path}/tmp ${solution_log_path}${i}
done
stty opost

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
    student_log_path=${out_path}/${student_name}_log
    student_diff_file=${out_path}/${student_name}_diff.txt

    ## Change terminal new line from CRLF to LF, then change back after the script
    stty -opost
    for(( i = 1; i <= $num_program_runs; i++ ));
    do
        ## cat tmp file to bash | read one line at a time with a pause in between | print 
        ## to stdout and pipe to the student file > redirect stdout to /dev/null
        script -c "cat ${tmp_path}/tmp${i} | { while read l ; do sleep .1; echo \$l; done } | tee >(python3 \"$student_file\")" \
            -O ${student_log_path}${i} > /dev/null
        ## The -q option doesn't seem to work in script, so we need to remove the first and last lines
        tail -n +2 ${student_log_path}${i} | head -n -1 > ${tmp_path}/tmp 
        mv ${tmp_path}/tmp ${student_log_path}${i}
    done
    stty opost
    
    touch $student_diff_file
    for(( i = 1; i <= $num_program_runs; i++ ));
    do
        ## Write the inputs to this program run.
        echo -n "PROGRAM RUN ${i}: {" >> ${student_diff_file}
        cat ${tmp_path}/tmp${i} | { while read l ; do echo -n "$l, "; done } >> ${student_diff_file}
        truncate -s-2 ${student_diff_file}
        echo "}" >> ${student_diff_file}

        diff --width=100 --expand-tabs --strip-trailing-cr --side-by-side \
            $solution_log_path$i $student_log_path$i >> $student_diff_file
    done

    ## The extra line bothers me. Get rid of it.
    truncate -s-1 $student_diff_file

done
