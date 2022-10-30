#!/usr/bin/env bash

##############################################################################
## Get the program inputs.
##############################################################################
read -p "Grade program path: " grade_program_path
read -p "Student files path: " student_file_path
read -p "Number of program runs: " num_program_runs
read -p "Number of program inputs: " num_program_inputs 

out_path=${student_file_path}/out
solution_log_path=${out_path}/solution_log.txt
rm -r $out_path
mkdir $out_path

for(( i = 1; i <= $num_program_runs; i++ ));
do
    input_array=()
    for(( j = 1; j <= $num_program_inputs; j++ ));
    do
        read -p "Input value, run ${i}, input $j: " input_value
        input_array+=($input_value)
    done
    printf "%s\n" "${input_array[@]}" > tmp${i}
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
    script -c "cat tmp${i} | { while read l ; do sleep .1; echo \$l; done } | tee >(python3 $grade_program_path)" \
        -O ${solution_log_path}${i} > /dev/null
    ## The -q option doesn't seem to work in script, so we need to remove the first and last lines
    tail -n +2 ${solution_log_path}${i} | head -n -1 > tmp 
    mv tmp ${solution_log_path}${i}
done
stty opost

echo -n '' > ${solution_log_path}
for(( i = 1; i <= $num_program_runs; i++ ));
do
    echo "BEGIN PROGRAM RUN ${i}" >> ${solution_log_path}
    cat ${solution_log_path}${i} >> ${solution_log_path}
    rm ${solution_log_path}${i}
done

## I'm not sure where the extra LFs are coming from but they bother me.
## Let's get rid of them.
truncate -s-2 ${solution_log_path}


##############################################################################
## Create the student file runs.
##############################################################################

for student_file in $student_file_path/*
do
    ## Use parameter expansion to only return the file name - not the full path.
    ## Store it in a variable.
    student_name=$(echo "${student_file##*/}" | cut -d '_' -f 1)
    student_out_file=${out_path}/${student_name}_log.txt
    student_diff_file=${out_path}/${student_name}_diff.txt

    ## Change terminal new line from CRLF to LF, then change back after the script
    stty -opost
    for(( i = 1; i <= $num_program_runs; i++ ));
    do
        ## cat tmp file to bash | read one line at a time with a pause in between | print 
        ## to stdout and pipe to the student file > redirect stdout to /dev/null
        script -c "cat tmp${i} | { while read l ; do sleep .1; echo \$l; done } | tee >(python3 $student_file)" \
            -O ${student_out_file}${i} > /dev/null
        ## The -q option doesn't seem to work in script, so we need to remove the first and last lines
        tail -n +2 ${student_out_file}${i} | head -n -1 > tmp 
        mv tmp ${student_out_file}${i}
    done
    stty opost
    
    echo -n '' > ${student_out_file}
    for(( i = 1; i <= $num_program_runs; i++ ));
    do
        echo "BEGIN PROGRAM RUN ${i}" >> ${student_out_file}
        cat ${student_out_file}${i} >> ${student_out_file}
        rm ${student_out_file}${i}
    done

    ## I'm not sure where the extra LFs are coming from but they bother me.
    ## Let's get rid of them.
    truncate -s-2 ${student_out_file}

    ## Create the diff file
    diff --side-by-side --suppress-common-lines ${solution_log_path} $student_out_file > $student_diff_file
    ##diff ${solution_log_path} $student_out_file > $student_diff_file

done

## Cleanup
for(( i = 1; i <= $num_program_runs; i++ ));
do
    rm tmp${i}
done
