Feature: test2

Scenario Outline: Obtener la suma total
    Given a <values> to sum
    When the calc sum the values
    Then the <total> is ok

    Examples: values
    |   values |   total   |
    |   3,2    |    5      |