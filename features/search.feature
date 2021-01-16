@Android
Feature: Check the Search result in subreddit

  Scenario Outline: check the most post title of the subreddit
    Given the app is launched
    When "<SEARCHED TERM>" is entered
    Then should be able to see the "<SEARCHED TERM>" results
    When tap on the "<SEARCHED TERM>" in the searched result list
    Then check "<CHECK TERM>" in the recent posted title
    Examples:
    | SEARCHED TERM | CHECK TERM |
    | gaming        | nintendo   |
