#!/usr/bin/env bash

## TODO: 
## Add python shebang at top of file if neeeded: #!/usr/bin/env python3
## Add chmod +x myfile.py
## Going to need to use expect program

## input_array=()
## read -p "Student files path: " student_files
## read -p "Grade program path: " grade_program
## read -p "Number of program inputs: " num_program_inputs 
## read -p "Number of program runs: " num_program_runs
## 
## for(( i = 1; i <= $num_program_runs; i++ ));
## do
##     for(( j = 1; j <= $num_program_inputs; j++ ));
##     do
##         read -p "Input value, run $i, input $j: " input_value
##         input_array+=($input_value)
##     done
## done

## tmp
grade_program='tmp_sln.py'

cat <<END > tmp
2
2 
2
END


cat tmp | echo

##cat tmp | tee /dev/tty | ./$grade_program
##./$grade_program < tmp | tee /dev/tty


