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
  Scenario Outline: Add book to the catalog
    Given user is on the "Lägg till bok" page
    When user adds <title> by <author>
    Then the fields should be cleared
    And <title> by <author> should be added to catalog

        Examples:
      | title                                                                                                                                                                                                                                                                                          | author                                                                                                                                                                |
      | Fyra anledningar till att ge mig VG                                                                                                                                                                                                                                                            | Sara Jonason                                                                                                                                                          |
      | 1234567890                                                                                                                                                                                                                                                                                     | 1234567890                                                                                                                                                            |
      | #@)(%&€_-,;.*^¨"/0+´`\ $∞§[]≈±©!                                                                                                                                                                                                                                                               | #@)(%&€_-,;.*^¨"/0+´`\ $∞§[]≈±©!                                                                                                                                      |
      | åäöôóòûúùœéüëáàèïîÅÄÖÁÀÉÈËÜÛÂÊÎÏÔÒÓ                                                                                                                                                                                                                                                            | åäöôóòûúùœéüëáàèïîÅÄÖÁÀÉÈËÜÛÂÊÎÏÔÒÓ                                                                                                                                   |
      | En bok med hemskt lång titel som liksom aldrig verkar ta slut men det måste vara så för att den här titeln ska kunna förklara vad boken handlar om, annars hade ingen valt att läsa den kanske är titeln det bästa med boken, den här författaren kommer nog inte att få skriva en bok igen... | Her Majesty Grand Princess Banana Hammock of The Badlands and Cathulu Långt Namn Oj Det Kanske Går I familjen På Något Sätt Att Man Inte Lyckas Hålla Sig Till Poängen|
      | space                                                                                                                                                                                                                                                                                          | space                                                                                                                                                                 |

  # [US3] As a site manager,
  #I want users to be stopped from adding books without both author and title,
  #so that there won't be books without complete information in the catalog
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

    Scenario: Add same book twice
      Given user is on the "Lägg till bok" page
      When user adds The call of Cthulhu by H.P Lovecraft
      And user adds The call of Cthulhu by H.P Lovecraft
      Then The catalog should contain 2 copies of The call of Cthulhu by H.P Lovecraft