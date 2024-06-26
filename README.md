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


[Link to the commit](https://github.com/zaherlavi/aider/commit/9ee753e4e772ae2d1bbe461347927ba0d8835a9d?diff=split&w=0)

<Provide a screenshot of the coverage results output by the instrumentation>

![Alt text](/Imgaes/vansham_validate_variables.png)

### Second Function

InputOutput.tool_error in io.py file

[Link to the commit](https://github.com/zaherlavi/aider/commit/9ee753e4e772ae2d1bbe461347927ba0d8835a9d?diff=split&w=0)

![Alt text](/Imgaes/vansham_configure_model_settings.png)


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

## Vansham Ahluwalia (vunet-id: vah201)

### Test 1

[Link to the commit](https://github.com/zaherlavi/aider/commit/9ee753e4e772ae2d1bbe461347927ba0d8835a9d?diff=split&w=0)

<Provide a screenshot of the old coverage results (the same as you already showed above)>


![Alt text](/Imgaes/vansham_old_percentage_validate_variables.png)

<Provide a screenshot of the new coverage results>


![Alt text](/Imgaes/vansham_new_percentage_validate_variables.png)

<State the coverage improvement with a number and elaborate on why the coverage is improved>

Improved branch coverage of the validate_variables function from 0% to 100%. In the existing tests for the models.py file, the function was not tested and covered at all. Using my own coverage tool, I identified the cases and wrote three tests for the validate_variables function. These tests are included in the test_models file, which has been committed to GitHub and can be accessed using the link above.

### Test 2

<Provide the same kind of information provided for Test 1>

[Link to the commit](https://github.com/zaherlavi/aider/commit/9ee753e4e772ae2d1bbe461347927ba0d8835a9d?diff=split&w=0)

![Alt text](/Imgaes/vansham_old_percentage_configure_model_settings.png)
![Alt text](/Imgaes/vansham_new_percentage_configure_model_settings.png)

Improved branch coverage of the configure_model_settings function from 65% to 94%. In the existing tests for the models.py file, the function was not tested and covered at all. Using my own coverage tool, I identified the cases and wrote five tests for the configure_model_settings function. These tests are included in the test_models file, which has been committed to GitHub and can be accessed using the link above.

## Shadman Sahil Chowdhury (vunet-id: scy580)

### First Function

models.token_count in models.py file


[Link to the commit](https://github.com/zaherlavi/aider/commit/cb27a2350bcb5f1c6b4e2932572fe041cffd19a8)

<Provide a screenshot of the coverage results output by the instrumentation>

![Alt text](/Imgaes/shadman-token_hit.png)

### Second Function

models.get_weak_model in models.py file

[Link to the commit](https://github.com/zaherlavi/aider/commit/cb27a2350bcb5f1c6b4e2932572fe041cffd19a8)

![Alt text](/Imgaes/shadman-weak_hit.png)


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

## Shadman Sahil Chowdhury (vunet-id: scy580)

### Test 1

[Link to the commit](https://github.com/zaherlavi/aider/commit/6dc42c2ed2f4d9c444c58c9e16e77986197b7ae3)

<Provide a screenshot of the old coverage results (the same as you already showed above)>


![Alt text](/Imgaes/shadman-token_count-before.jpg)

<Provide a screenshot of the new coverage results>


![Alt text](/Imgaes/shadman-token_count-after.jpg)

<State the coverage improvement with a number and elaborate on why the coverage is improved>

Improved branch coverage of the token_count function from 83% to 100%. In the existing tests for the models.py file, the function was not tested and covered at all. Using my own coverage tool, I identified the cases and wrote one test for the token_count function. This test is included in the test_models file, which has been committed to GitHub and can be accessed using the link above.

### Test 2

<Provide the same kind of information provided for Test 1>

[Link to the commit](https://github.com/zaherlavi/aider/commit/5cb3207326e066a0e3840e1f47b45da5c52056ef)

![Alt text](/Imgaes/shadman-get_weak_model-before.png)
![Alt text](/Imgaes/shadman-get_weak_model-after.png)

Improved branch coverage of the get_weak_model function from 90% to 100%. In the existing tests for the models.py file, the function was not tested and covered at all. Using my own coverage tool, I identified the cases and wrote one test for the get_weak_model function. The test is included in the test_models file, which has been committed to GitHub and can be accessed using the link above.



### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

![Alt text](/Imgaes/old-coverage.jpeg)

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>


## Statement of individual contributions

<Write what each group member did>

Zaher Lavi: I improved the branch coverage of two functions. In the report, I worked on the sections covering the project chosen, coverage measurement, individual parts, and the overall.

Shadman Sahil: I improved the branch coverage of two functions, updated the report and worked on my individual part.
