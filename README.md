Automation Tool 

The following Python script using Behave and Docker is used to automate the test 

cases:

INSTRUCTIONS FOR RUNNING THE AUTOMATION SCRIPT

1. Set up Docker:

a. Ensure Docker is installed and running on your machine.

b. Pull the Docker image using the provided command:

docker pull public.ecr.aws/l4q9w4c5/loanpro-calculator-cli:latest

2. Install Behave by running:

pip install behave

3. Save the provided Python script in a file named calculator_steps.py within a 

steps directory.

4. Create a features directory and save your feature files (e.g., 

calculator.feature) within it.

5. Run the tests using Behave:

Behave
