# Created by An Nguyen at 11/25/2017
Feature: Google Search function

  Scenario: Navigate to Google page
    Given user navigates to Google page
    When user inputs "GameK" keyword into search field and type ENTER on keyboard
    And he is continue to clicking Gamek website in search results
    Then he do not want to do anything else