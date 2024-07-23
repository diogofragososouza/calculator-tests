import subprocess
from behave import given, when, then

@given('I have a calculator')
def step_given_i_have_a_calculator(context):
    # Pull the Docker image
    subprocess.run(["docker", "pull", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli:latest"], check=True)

@when('I add {a:d} and {b:d}')
def step_when_i_add(context, a, b):
    result = subprocess.run(
        ["docker", "run", "--rm", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", "add", str(a), str(b)],
        capture_output=True, text=True, check=True
    )
    # Extract the numeric part from the output
    context.result = float(result.stdout.strip().split(": ")[1])

@when('I subtract {b:d} from {a:d}')
def step_when_i_subtract(context, a, b):
    result = subprocess.run(
        ["docker", "run", "--rm", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", "subtract", str(a), str(b)],
        capture_output=True, text=True, check=True
    )
    # Extract the numeric part from the output
    context.result = float(result.stdout.strip().split(": ")[1])

@when('I multiply {a:d} and {b:d}')
def step_when_i_multiply(context, a, b):
    result = subprocess.run(
        ["docker", "run", "--rm", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", "multiply", str(a), str(b)],
        capture_output=True, text=True, check=True
    )
    # Extract the numeric part from the output
    context.result = float(result.stdout.strip().split(": ")[1])

@when('I divide {a:d} by {b:d}')
def step_when_i_divide(context, a, b):
    result = subprocess.run(
        ["docker", "run", "--rm", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", "divide", str(a), str(b)],
        capture_output=True, text=True
    )
    output = result.stdout.strip()
    if "Cannot divide by zero" in output:
        context.result = 'Error'
    else:
        context.result = float(output.split(": ")[1])

@then('the result should be {expected_result:d}')
def step_then_the_result_should_be(context, expected_result):
    assert context.result == expected_result

@then('an error should occur')
def step_then_an_error_should_occur(context):
    assert context.result == 'Error'
