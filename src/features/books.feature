Feature: Handle books in the catalog
  As a user I want to be able to see and add books

  #[US1] As a user,
  #  # I want a catalog of books,
  #  # so I can see which books there are to interact with
  Scenario: Display a catalog with books
    Given user is on the "Katalog" page
    Then user should see a list of books
    And every book should have a title, an author and a heart icon

  # [US2] As a user,
  #  # I want to be able to add books,
  #  # so that I can expand the catalog
  Scenario: Add book to the catalog
    Given user is on the "Lägg till bok" page
    When user adds Project Hail Mary and Andy Weir
    Then the fields should be cleared
    And Project Hail Mary by Andy Weir should be added to catalog

  # [US3] As a site manager,
  # I want to disable the "Lägga till bok" button until both title and author are filled in,
  # so that books can't be added without complete information
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