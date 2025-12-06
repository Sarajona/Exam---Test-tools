Feature: Handle navigation and interaction

  #[US7] As a user,
  # I want to navigate between the different tabs on the website,
  # so that I can access all features easily
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