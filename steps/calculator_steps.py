import subprocess
from behave import given, when, then

def run_docker_command(operation, *args):
    command = ["docker", "run", "--rm", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", operation] + list(map(str, args))
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout.strip()

@given('I have a calculator')
def step_given_i_have_a_calculator(context):
    subprocess.run(["docker", "pull", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli:latest"], check=True)

@when('I add {a:d} and {b:d}')
def step_when_i_add_integers(context, a, b):
    result = subprocess.run(
        ["docker", "run", "--rm", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", "add", str(a), str(b)],
        capture_output=True, text=True, check=True
    )
    context.result = float(result.stdout.strip().split(": ")[1])

@when('I subtract {b:d} from {a:d}')
def step_when_i_subtract_integers(context, a, b):
    result = subprocess.run(
        ["docker", "run", "--rm", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", "subtract", str(a), str(b)],
        capture_output=True, text=True, check=True
    )
    context.result = float(result.stdout.strip().split(": ")[1])

@when('I multiply {a:d} and {b:d}')
def step_when_i_multiply_integers(context, a, b):
    result = subprocess.run(
        ["docker", "run", "--rm", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", "multiply", str(a), str(b)],
        capture_output=True, text=True, check=True
    )
    context.result = float(result.stdout.strip().split(": ")[1])

@when('I divide {a:d} by {b:d}')
def step_when_i_divide_integers(context, a, b):
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
def step_then_the_result_should_be_integers(context, expected_result):
    assert context.result == expected_result

@when('I add decimals {a} and {b}')
def step_when_i_add_decimals(context, a, b):
    try:
        output = run_docker_command("add", a, b)
        context.result = float(output.split(": ")[1])
    except (subprocess.CalledProcessError, ValueError, IndexError):
        context.result = 'Error'

@when('I subtract decimals {b} from {a}')
def step_when_i_subtract_decimals(context, a, b):
    try:
        output = run_docker_command("subtract", a, b)
        context.result = float(output.split(": ")[1])
    except (subprocess.CalledProcessError, ValueError, IndexError):
        context.result = 'Error'

@when('I multiply decimals {a} and {b}')
def step_when_i_multiply_decimals(context, a, b):
    try:
        output = run_docker_command("multiply", a, b)
        context.result = float(output.split(": ")[1])
    except (subprocess.CalledProcessError, ValueError, IndexError):
        context.result = 'Error'

@when('I divide decimals {a} by {b}')
def step_when_i_divide_decimals(context, a, b):
    try:
        output = run_docker_command("divide", a, b)
        if "Cannot divide by zero" in output:
            context.result = 'Error'
        else:
            context.result = float(output.split(": ")[1])
    except (subprocess.CalledProcessError, ValueError, IndexError):
        context.result = 'Error'

@then('the result should be {expected_result}')
def step_then_the_result_should_be_decimals(context, expected_result):
    if expected_result == 'Error':
        assert context.result == 'Error'
    else:
        expected_result = float(expected_result)
        epsilon = 1e-8
        assert abs(context.result - expected_result) < epsilon, f"Expected {expected_result}, but got {context.result}"

@when('I add non-numeric {a} and {b}')
def step_when_i_add_non_numeric(context, a, b):
    try:
        output = run_docker_command("add", a, b)
        context.result = float(output.split(": ")[1])
    except (subprocess.CalledProcessError, ValueError, IndexError):
        context.result = 'Error'

@when('I subtract non-numeric {a} from {b}')
def step_when_i_subtract_non_numeric(context, a, b):
    try:
        output = run_docker_command("subtract", a, b)
        context.result = float(output.split(": ")[1])
    except (subprocess.CalledProcessError, ValueError, IndexError):
        context.result = 'Error'

@when('I multiply non-numeric {a} by {b}')
def step_when_i_multiply_non_numeric(context, a, b):
    try:
        output = run_docker_command("multiply", a, b)
        context.result = float(output.split(": ")[1])
    except (subprocess.CalledProcessError, ValueError, IndexError):
        context.result = 'Error'

@when('I divide non-numeric {a} by {b}')
def step_when_i_divide_non_numeric(context, a, b):
    try:
        output = run_docker_command("divide", a, b)
        context.result = float(output.split(": ")[1])
    except (subprocess.CalledProcessError, ValueError, IndexError):
        context.result = 'Error'

@then('an error should occur')
def step_then_an_error_should_occur(context):
    assert context.result == 'Error'
