"""
Chapter 11: Testing Your Code (with pytest)
This file acts as a complete study guide for testing functions and classes,
including the assertion cheat sheet, fixture implementation, and terminal output markers.

Note: In a real project, your application code and your test code would 
be stored in separate files. You would use import statements in your 
test files to access the functions and classes you want to test.
"""

import pytest

# =========================================================
# 1. THE APPLICATION CODE (Functions and Classes)
# Pretend these live in 'name_function.py' and 'survey.py'
# =========================================================

# --- A Failing Function Example ---
# If we wrote the function like this: 
# def get_formatted_name(first, middle, last): 
# It would BREAK our original test for 'Janis Joplin' because it requires 3 arguments.
# When a test fails, DO NOT change the test! Fix the function to handle the new behavior.

# --- The Fixed Function ---
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """Show the survey question."""
        print(self.question)
        
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


# =========================================================
# 2. COMMON ASSERTIONS REFERENCE (Table 11-1)
# =========================================================
# When testing, you can evaluate almost any conditional statement.
# Here are the 6 primary assertions to remember:
#
# assert a == b          (Asserts the two values are equal)
# assert a != b          (Asserts the two values are NOT equal)
# assert a               (Asserts the value evaluates to True)
# assert not a           (Asserts the value evaluates to False)
# assert item in list    (Asserts the item exists within the list)
# assert item not in list(Asserts the item does NOT exist in the list)


# =========================================================
# 3. UNIT TESTS FOR FUNCTIONS
# Pretend this is in 'test_name_function.py'
# You would need: from name_function import get_formatted_name
# =========================================================

# RULES: Test filenames and test function names MUST start with 'test_' 
# so pytest discovers them automatically.

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'


# =========================================================
# 4. FIXTURES & TESTING CLASSES
# Pretend this is in 'test_survey.py'
# You would need: from survey import AnonymousSurvey
# =========================================================

# FIXTURES: Use the @pytest.fixture decorator to build a resource ONCE 
# and reuse it across multiple tests. This prevents you from repeating setup code.
@pytest.fixture
def language_survey():
    """Builds a survey instance available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

# To inject the fixture, pass its exact function name as a parameter to your test.
def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
        
    for response in responses:
        assert response in language_survey.responses


# =========================================================
# 5. TERMINAL COMMANDS & OUTPUT CHEAT SHEET
# =========================================================
# Run all tests in a folder: $ pytest
# Run a specific test file:  $ pytest test_survey.py
#
# Output Markers:
# . (Dot) = The test passed.
# F       = The test failed.
# >       = Highlights the specific line of code that broke.
# E       = Explains the exact Error (e.g., TypeError).
#
# Dealing with Failures:
# 1. Look at the single 'F' to see a test failed.
# 2. Look at the '>' to find the line of code in your test that triggered the failure.
# 3. Look at the 'E' to see the exact error.
# 4. FIX THE FUNCTION/CLASS, NOT THE TEST!