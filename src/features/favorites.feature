Feature: Handle favorites

  Background: user is on "Katalog" page

  Scenario: Add favorite
    Given Min katt är min chef is not favorite
    When user adds Min katt är min chef as favorite
    Then Min katt är min chef is favorite

Scenario Outline: Display favorites in list
    Given the following books are marked as favorites: <favorites>
    When user navigates to "Mina böcker" page
    Then favorites list should display: <result>

Examples:
    | favorites                                       | result                                          |
    | Min katt är min chef, Jag trodde det var tisdag | Min katt är min chef, Jag trodde det var tisdag |
    | Kaffekokaren som visste för mycket              | Kaffekokaren som visste för mycket              |
    | <empty>                                         | Empty list, info text                           |

  Scenario: Remove favorite
    Given Min katt är min chef is favorite
    When user removes Min katt är min chef from favorites
    Then Min katt är min chef is not favorite
    And Min katt är min chef does not exist in list of favorites on the "Mina böcker" page