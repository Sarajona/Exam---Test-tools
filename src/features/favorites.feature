Feature: Handle favorites

  #[US4] As a user,
  #I want to there to be a heart button,
  #so I can select it as favorite
  Scenario: Add favorite
    Given user is on the "Katalog" page
    And Min katt är min chef is not favorite
    When user adds Min katt är min chef as favorite
    Then Min katt är min chef is favorite

  Scenario Outline: User clicks on heart button more than 2 times
    Given user is on the "Katalog" page
    And book has <state_of_book>
    When user clicks on heart button <times> times
    Then book should be <new_state>

    Examples:
      | state_of_book | times | new_state   |
      | favorite      | 3     | not favorite|
      | not favorite  | 3     | favorite    |
      | favorite      | 4     | favorite    |
      | not favorite  | 4     | not favorite|
      | favorite      | 10    | favorite    |
      | not favorite  | 10    | not favorite|
      | favorite      | 31    | not favorite|
      | not favorite  | 31    | favorite    |

   # [US5] As a user,
   # I want a list of my favorite books,
   # so that I can have an overview of them
  Scenario Outline: Display favorites in list
    Given user is on the "Katalog" page
    When user marks the following books as favorites: <favorites>
    And navigates to "Mina böcker" page
    Then favorites list should have: <result>

    Examples:
      | favorites                                       | result                                          |
      | Min katt är min chef, Jag trodde det var tisdag | Min katt är min chef, Jag trodde det var tisdag |
      | Kaffekokaren som visste för mycket              | Kaffekokaren som visste för mycket              |
      | <empty>                                         | Empty list, info text                           |

    #[US6] As a user,
    # I want to deselect favorite books,
    # so I can remove books from my list of favorites
  Scenario: Remove favorite
    Given user is on the "Katalog" page
    And Min katt är min chef is favorite
    When user removes Min katt är min chef from favorites
    Then Min katt är min chef is not favorite
    And Min katt är min chef does not exist in list of favorites on the "Mina böcker" page