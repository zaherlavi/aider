# Report for Assignment 1

## Project chosen

Name: Aider

URL: https://github.com/paul-gauthier/aider

Number of lines of code and the tool used to count it: The tool was lizard and it was 10920 nloc

Programming language: Python

## Coverage measurement

### Existing tool

<Inform the name of the existing tool that was executed and how it was executed>
We used coverage.py as an existing tool fore coverage measurement


```bash
// Coverage tool running process
coverage run -m pytest
coverage report
coverage html
```

<Show the coverage results provided by the existing tool with a screenshot>

![Alt text](/Imgaes/old-coverage.jpeg)


### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Group member name>

## Zaher Lavi (vunet-id: zla202)

### First Function

InputOutput.user_input in io.py file


[Link to the commit](https://github.com/zaherlavi/aider/commit/9ee753e4e772ae2d1bbe461347927ba0d8835a9d?diff=split&w=0)

<Provide a screenshot of the coverage results output by the instrumentation>

![Alt text](/Imgaes/zaher-user_input.png)

### Second Function

InputOutput.tool_error in io.py file

[Link to the commit](https://github.com/zaherlavi/aider/commit/9ee753e4e772ae2d1bbe461347927ba0d8835a9d?diff=split&w=0)

![Alt text](/Imgaes/zaher-tool_error.png)


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

## Zaher Lavi (vunet-id: zla202)

### Test 1

[Link to the commit](https://github.com/zaherlavi/aider/commit/9ee753e4e772ae2d1bbe461347927ba0d8835a9d?diff=split&w=0)

<Provide a screenshot of the old coverage results (the same as you already showed above)>


![Alt text](/Imgaes/zaher-old-user_input-coverage-percentage.png)

<Provide a screenshot of the new coverage results>


![Alt text](/Imgaes/zaher-new-user_input-coverage-percentage.png)

<State the coverage improvement with a number and elaborate on why the coverage is improved>

Improved branch coverage of the user_input function from 70% to 100%. In the existing tests for the io.py file, the function was not tested and covered at all, and there were two cases that could be tested. Using my own coverage tool, I identified these cases and wrote two tests for the user_input function. These tests are included in the test_io file, which has been committed to GitHub and can be accessed using the link above.

### Test 2

<Provide the same kind of information provided for Test 1>

[Link to the commit](https://github.com/zaherlavi/aider/commit/9ee753e4e772ae2d1bbe461347927ba0d8835a9d?diff=split&w=0)

![Alt text](/Imgaes/zaher-old-tool_error-coverage-percentage.png)
![Alt text](/Imgaes/zaher-new-tool_error-coverage-percentage.png)

Improved branch coverage of the tool_error function from 75% to 100%. In the existing tests for the io.py file, the function was not tested and covered at all, and there were three cases that could be tested. Using my own coverage tool, I identified these cases and wrote three tests for the tool_error function. These tests are included in the test_io file, which has been committed to GitHub and can be accessed using the link above.





## Vansham Ahluwalia (vunet-id: vah201)

### First Function

models.validate_variables in models.py file


[Link to the commit](https://github.com/Vansham8/aider/commit/2a335e17e59533ec5a4d3eb842e32c57c6949ae7)

<Provide a screenshot of the coverage results output by the instrumentation>

![Alt text](/Imgaes/vansham_validate_variables.png)

### Second Function

InputOutput.tool_error in io.py file

[Link to the commit](https://github.com/Vansham8/aider/commit/2a335e17e59533ec5a4d3eb842e32c57c6949ae7)

![Alt text](/Imgaes/vansham_configure_model_settings.png)


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

## Vansham Ahluwalia (vunet-id: vah201)

### Test 1

[Link to the commit](https://github.com/Vansham8/aider/commit/2a335e17e59533ec5a4d3eb842e32c57c6949ae7)

<Provide a screenshot of the old coverage results (the same as you already showed above)>


![Alt text](/Imgaes/vansham_old_percentage_validate_variables.png)

<Provide a screenshot of the new coverage results>


![Alt text](/Imgaes/vansham_new_percentage_validate_variables.png)

<State the coverage improvement with a number and elaborate on why the coverage is improved>

Improved branch coverage of the validate_variables function from 0% to 100%. In the existing tests for the models.py file, the function was not tested and covered at all. Using my own coverage tool, I identified the cases and wrote three tests for the validate_variables function. These tests are included in the test_models file, which has been committed to GitHub and can be accessed using the link above.

### Test 2

<Provide the same kind of information provided for Test 1>

[Link to the commit](https://github.com/Vansham8/aider/commit/2a335e17e59533ec5a4d3eb842e32c57c6949ae7)

![Alt text](/Imgaes/vansham_old_percentage_configure_model_settings.png)
![Alt text](/Imgaes/vansham_new_percentage_configure_model_settings.png)

Improved branch coverage of the configure_model_settings function from 65% to 94%. In the existing tests for the models.py file, the function was not tested and covered at all. Using my own coverage tool, I identified the cases and wrote five tests for the configure_model_settings function. These tests are included in the test_models file, which has been committed to GitHub and can be accessed using the link above.

## Shadman Sahil Chowdhury (vunet-id: scy580)

### First Function

Commands.cmd_commit() in commands.py file


[Link to the commit](https://github.com/zaherlavi/aider/commit/61af747ebe309ab536a875e3f951e3ed60c93402)

<Provide a screenshot of the coverage results output by the instrumentation>

![Alt text](/Imgaes/shadman-commit_hits.png)

### Second Function

 Repomap.get_repo_map() in repomap.py file

[Link to the commit](https://github.com/zaherlavi/aider/commit/0d42b33d846081b2e099d1fbe553e78459ae1946)

![Alt text](/Imgaes/shadman-map_hits.png)


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

## Shadman Sahil Chowdhury (vunet-id: scy580)

### Test 1

[Link to the commit](https://github.com/zaherlavi/aider/commit/08f5357b7e53ee6f0356847b91a8f1fd1dcbb688)

<Provide a screenshot of the old coverage results (the same as you already showed above)>


![Alt text](/Imgaes/shadman-cmd-before.png)

<Provide a screenshot of the new coverage results>


![Alt text](/Imgaes/shadman-cmd-after.png)

<State the coverage improvement with a number and elaborate on why the coverage is improved>

Improved branch coverage of the cmd_commit function from 50% to 100%. In the existing tests for the commands.py file, the function was not tested and covered at all. Using my own coverage tool, I identified the cases and wrote tests for the function. These tests are included in the test_commands file, which has been committed to GitHub and can be accessed using the link above.

### Test 2

<Provide the same kind of information provided for Test 1>

[Link to the commit](https://github.com/zaherlavi/aider/commit/c33bd77946a7504e791a91768e7393cfac672713)

![Alt text](/Imgaes/shadman-get_repo-before.png)
![Alt text](/Imgaes/shadman-get_repo-after.png)

Improved branch coverage of the get_repo_map function from 69% to 82%. In the existing tests for the repomap.py file, the function was not tested and covered at all. Using my own coverage tool, I identified the cases and wrote 5 tests for the get_repo_map function. The tests are included in the test_repomap file, which has been committed to GitHub and can be accessed using the link above.

## Ana Mafiyusef (vunet-id: ama487)

### First Function
run_cmd in linter.py file

[Link to the commit](https://github.com/zaherlavi/aider/commit/4a5ed2828e8fb2d297868e9bbef449459c21b8d4)

![Alt text](https://github.com/zaherlavi/aider/blob/main/Imgaes/ana-run_cmd.png?raw=true)

## Second Function
py_lint in linter.py file 

[Link to the commit](https://github.com/zaherlavi/aider/commit/4a5ed2828e8fb2d297868e9bbef449459c21b8d4)

![Alt text](https://github.com/zaherlavi/aider/blob/main/Imgaes/ana_py_lint.png?raw=true)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

## Ana Mafiyusef (vunet-id: ama487)

### Test 1
[Link to the commit](https://github.com/zaherlavi/aider/commit/11b3b6eccf4529b64a31fd20f580d2ecaddf256a)

![Alt text](https://github.com/zaherlavi/aider/blob/main/Imgaes/ana_run_cmd_before.png?raw=true)

![Alt text](https://github.com/zaherlavi/aider/blob/main/Imgaes/ana_run_cmd_afterr.png?raw=true)

I improved the branch coverage of the run_cmd function from 0% to 81%. Initially, there were no test files for linter.py, so I created a new file, test_linter.py.The test is included in the test_models file, which has been committed to GitHub and can be accessed using the link above.
### Test 2

![Alt text](https://github.com/zaherlavi/aider/blob/main/Imgaes/ana_py_lint_before.png?raw=true)

![Alt text](https://github.com/zaherlavi/aider/blob/main/Imgaes/ana_py_lint_after.png?raw=true)

I improved the branch coverage of the run_cmd function from 0% to 84%. Initially, there were no test files for linter.py, so I created a new file, test_linter.py.The test is included in the test_models file, which has been committed to GitHub and can be accessed using the link above.

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>


![Alt text](/Imgaes/old-coverage.jpeg)

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>


![Alt text](/Imgaes/new_coverage.png)

## Statement of individual contributions

<Write what each group member did>

Zaher Lavi: I improved the branch coverage of two functions. In the report, I worked on the sections covering the project chosen, coverage measurement, individual parts, and the overall.

Vansham Ahluwalia: I checked and improved the branch coverage of two functions in models, updated the report and worked on my individual part and overall.

Shadman Sahil: I improved the branch coverage of two functions, updated the report and worked on my individual part.

Ana Mafiyusef: I improved the branch coverage of two functions, worked on my individual part and updated the report.
