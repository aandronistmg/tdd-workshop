# TDD Workshop with Pytest

**Goal of the workshop**: everyone has an understanding of the importance of testing and knows how to get started with TDD in pytest

## Setting up environment and installing libraries (MacOS)

Create a virtual environment
```
python3 -m venv .venv
```

Activate the virtual environment
```
source .venv/bin/activate
```

Install the dependencies
```
pip install -r requirements.txt
```

## How to run the tests

```
pytest
```

`-s` to display (only when the test fails)

`-k` to run a specific test (looks for test containing that name)

`-v` verbose

## Example TDD

[FizzBuzz](https://codingdojo.org/kata/FizzBuzz/)

## Practical problem for TDD

[Roman Numerals kata](https://codingdojo.org/kata/RomanNumerals/)

>> The Kata says you should write a function to convert from normal numbers to Roman Numerals using a TDD approach.

## Red, Green, Refactor

1. Write a test for a new function. The test should fail.

2. Write code until the test passes.

3. Refactor until the code is suitable for continued development

4. Goto 1.

You should proceed with baby steps, as small as possible! The above steps are the only things you are allowed to do.


## [Pick a pair](https://pickerwheel.com/tools/random-team-generator/_)

## Pair programming refresher
>> Pair programming is a software development technique in which two programmers work together at one workstation. One, the driver, writes code while the other, the observer or navigator, reviews each line of code as it is typed in. The two programmers switch roles frequently. While reviewing, the observer also considers the "strategic" direction of the work, coming up with ideas for improvements and likely future problems to address. This is intended to free the driver to focus all of their attention on the "tactical" aspects of completing the current task, using the observer as a safety net and guide.

- two programmers
    - driver : writes code
    - observer/navigator : reviews each line of code as it's types
- switch every 10 min