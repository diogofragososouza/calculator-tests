Feature: Calculator

  Scenario: TC001 Add two positive numbers
    Given I have a calculator
    When I add 8 and 5
    Then the result should be 13

  Scenario: TC002 Subtract two numbers
    Given I have a calculator
    When I subtract 3 from 10
    Then the result should be 7

  Scenario: TC003 Multiply two numbers
    Given I have a calculator
    When I multiply 4 and 2
    Then the result should be 8

  Scenario: TC004 Divide two numbers
    Given I have a calculator
    When I divide 9 by 3
    Then the result should be 3

  Scenario: TC005 Add a positive and a negative number
    Given I have a calculator
    When I add 7 and -2
    Then the result should be 5

  Scenario: TC006 Divide by zero
    Given I have a calculator
    When I divide 10 by 0
    Then an error should occur

  Scenario: TC007 Add two large numbers
    Given I have a calculator
    When I add 1000000 and 2000000
    Then the result should be 3000000

  Scenario: TC008 Subtract a larger number from a smaller number
    Given I have a calculator
    When I subtract 10 from 5
    Then the result should be -5

  Scenario: TC009 Multiply by zero
    Given I have a calculator
    When I multiply 15 and 0
    Then the result should be 0

  Scenario: TC010 Divide a number by itself
    Given I have a calculator
    When I divide 7 by 7
    Then the result should be 1

  Scenario: TC011 Divide a very large number
    Given I have a calculator
    When I divide 100000000000000000000000 by 2
    Then the result should be 50000000000000000000000

  Scenario: TC012 Multiply zero by a positive integer
    Given I have a calculator
    When I multiply 0 and 5
    Then the result should be 0

  Scenario: TC013 Add non-numeric values
    Given I have a calculator
    When I add non-numeric "a" and 5
    Then an error should occur

  Scenario: TC014 Add two large decimal numbers
    Given I have a calculator
    When I add decimals 12345678.1234567 and 98765432.1234567
    Then the result should be 111111110.2469134

  Scenario: TC015 Add a small number to a decimal number
    Given I have a calculator
    When I add decimals 0.0000001 and 1000.0000001
    Then the result should be 1000.0000002

  Scenario: TC016 Subtract a negative integer from a positive integer
    Given I have a calculator
    When I subtract -5 from 10
    Then the result should be 15

  Scenario: TC017 Divide a decimal number by an integer
    Given I have a calculator
    When I divide decimals 100.5 by 2
    Then the result should be 50.25

  Scenario: TC018 Multiply two large decimal numbers
    Given I have a calculator
    When I multiply decimals 12345.6789 and 98765.4321
    Then the result should be 1219326311.1263527

  Scenario: TC019 Subtract a decimal number from a large integer
    Given I have a calculator
    When I subtract decimals 0.1234567 from 1000000
    Then the result should be 999999.8765433

  Scenario: TC020 Subtract a very small number from a decimal number
    Given I have a calculator
    When I subtract decimals 0.0000001 from 1.0000001
    Then the result should be 1.0

  Scenario: TC021 Add two decimal numbers
    Given I have a calculator
    When I add decimals 1.2345678 and 9.8765432
    Then the result should be 11.111111

  Scenario: TC022 Subtract a decimal number from an integer
    Given I have a calculator
    When I subtract decimals 1.2345678 from 10
    Then the result should be 8.7654322

  Scenario: TC023 Multiply two decimal numbers
    Given I have a calculator
    When I multiply decimals 1.2345678 and 9.8765432
    Then the result should be 12.1932631

  Scenario: TC024 Divide a large decimal number by an integer
    Given I have a calculator
    When I divide decimals 98765432.1234567 by 3
    Then the result should be 32921810.7078189

  Scenario: TC025 Divide non-numeric values
    Given I have a calculator
    When I divide non-numeric "a" by 5
    Then an error should occur

  Scenario: TC026 Multiply non-numeric values
    Given I have a calculator
    When I multiply non-numeric "a" by 5
    Then an error should occur

  Scenario: TC027 Subtract non-numeric values
    Given I have a calculator
    When I subtract non-numeric "a" from 5
    Then an error should occur