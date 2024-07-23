Feature: Calculator

  Scenario: Add two positive numbers
    Given I have a calculator
    When I add 8 and 5
    Then the result should be 13

  Scenario: Subtract two numbers
    Given I have a calculator
    When I subtract 3 from 10
    Then the result should be 7

  Scenario: Multiply two numbers
    Given I have a calculator
    When I multiply 4 and 2
    Then the result should be 8

  Scenario: Divide two numbers
    Given I have a calculator
    When I divide 9 by 3
    Then the result should be 3

  Scenario: Add a positive and a negative number
    Given I have a calculator
    When I add 7 and -2
    Then the result should be 5

  Scenario: Divide by zero
    Given I have a calculator
    When I divide 10 by 0
    Then an error should occur

  Scenario: Add two large numbers
    Given I have a calculator
    When I add 1000000 and 2000000
    Then the result should be 3000000

  Scenario: Subtract a larger number from a smaller number
    Given I have a calculator
    When I subtract 10 from 5
    Then the result should be -5

  Scenario: Multiply by zero
    Given I have a calculator
    When I multiply 15 and 0
    Then the result should be 0

  Scenario: Divide a number by itself
    Given I have a calculator
    When I divide 7 by 7
    Then the result should be 1

  Scenario: Divide a very large number
    Given I have a calculator
    When I divide 100000000000000000000000 by 2
    Then the result should be 50000000000000000000000
