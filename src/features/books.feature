Feature: Handle books in the catalog
  As a user I want to be able to see and add books

  Scenario: Display a catalog with books
    Given user is on the "Katalog" page
    Then user should see a list of books
    And every book should have a title, an author and a heart icon

  Scenario: Add book to the catalog
    Given user is on the "Lägg till bok" page
    When user adds Project Hail Mary and Andy Weir
    Then the fields should be cleared
    And Project Hail Mary by Andy Weir should be added to catalog

  Scenario Outline: Enable the "Lägg till bok" button
    Given user is on the "Lägg till bok" page
    When user enters <title> and <author>
    Then the result should be <result>

    Examples:
      | title                                 | author       | result            |
      | Fyra anledningar till att ge mig VG   | Sara Jonason | button is enabled |
      | <empty>                               | <empty>      | button is disabled|
      | Project Hail Mary                     | <empty>      | button is disabled|
      | <empty>                               | Neil Gaiman  | button is disabled|