Feature: Handle navigation and interaction

  Scenario Outline: Navigate between tabs
    Given user is on <start_page> page
    When user navigates to <go_to_page> page
    Then <go_to_page> page is shown

    Examples:
      | start_page    | go_to_page    |
      | Katalog       | Lägg till bok |
      | Katalog       | Mina böcker   |
      | Lägg till bok | Katalog       |
      | Lägg till bok | Mina böcker   |
      | Mina böcker   | Katalog       |
      | Mina böcker   | Lägg till bok |
      | Katalog       | Katalog       |
      | Mina böcker   | Mina böcker   |
      | Lägg till bok | Lägg till bok |

  Scenario: Heart button becomes visible on hover
    Given user is on the "Katalog" page
    When user hovers over a book
    Then heart button for that book becomes visible