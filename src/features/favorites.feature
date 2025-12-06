Feature: Handle favorites

  Background: user is on "Katalog" page

  Scenario: Heart button becomes visible on hover
    Given user is on the "Katalog" page
    When user hovers over a book
    Then heart button for that book becomes visible

  # [US4] As a user,
  # I want to be able to select books as favorites,
  # so that I can remember which ones I've read and liked
  Scenario: Add favorite
    Given Min katt är min chef is not favorite
    When user adds Min katt är min chef as favorite
    Then Min katt är min chef is favorite

 # [US5] As a user,
 # I want a list of my favorite books,
 # so that I can have an overview of them
Scenario Outline: Display favorites in list
    Given the following books are marked as favorites: <favorites>
    When user navigates to "Mina böcker" page
    Then favorites list should display: <result>

Examples:
    | favorites                                       | result                                          |
    | Min katt är min chef, Jag trodde det var tisdag | Min katt är min chef, Jag trodde det var tisdag |
    | Kaffekokaren som visste för mycket              | Kaffekokaren som visste för mycket              |
    | <empty>                                         | Empty list, info text                           |

  #[US6] As a user,
  # I want to deselect favorite books,
  # so I can remove books from my list of favorites
  Scenario: Remove favorite
    Given Min katt är min chef is favorite
    When user removes Min katt är min chef from favorites
    Then Min katt är min chef is not favorite
    And Min katt är min chef does not exist in list of favorites on the "Mina böcker" page