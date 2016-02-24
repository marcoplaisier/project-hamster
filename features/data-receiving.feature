# Created by marco at 13-Feb-16
Feature: Sensors send data
  When a sensor senses a change in reflectivity, it hands the data of to another process that makes sense of it. When
  one sensor fires first, followed by the other, we know that the wheel is turning in a certain direction. When the
  first sensor fires and then fires again, we know that the wheel is stationary.

  Scenario: turning
    Given two sensors
    And sensor 1 is low
    When sensor 1 goes high
    Then the sensor manager returns 1 transition