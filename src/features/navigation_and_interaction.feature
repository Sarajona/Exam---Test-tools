# language: sv

# [US7] Som en användare,
#vill jag att "Katalog" ska vara startsidan när jag navigerar till hemsidan
#så att jag lättare förstår hemsidans syfte och struktur

# [US8] Som en användare,
# vill jag kunna navigera mellan olika flikar på hemsidan
# så att kan utnyttja samtlig funktionalitet

# [US9] Som en användare,
# vill jag kunna hovra över de olika element på hemsidan
# så att blir tydligt att man kan interagera med dem

Scenario: Katalog som startsida
    Then ska "Katalog"-fliken visas som startsida

  Scenario Outline: Navigera mellan flikar
    Given jag befinner mig på <start_flik>-fliken
    When jag navigerar till <gå_till>-fliken
    Then ska <gå_till>-fliken visas

    Examples:
      | start_flik    | gå_till       |
      | Katalog       | Lägg till bok |
      | Katalog       | Mina böcker   |
      | Lägg till bok | Katalog       |
      | Lägg till bok | Mina böcker   |
      | Mina böcker   | Katalog       |
      | Mina böcker   | Lägg till bok |

  Scenario Outline: Hovra över flikar
    When jag hovrar över <flik>-fliken
    Then ska fliken markeras som interaktiv

    Examples:
      | flik          |
      | Katalog       |
      | Lägg till bok |
      | Mina böcker   |

  Scenario: Hovra över en bok i katalogen
    When jag hovrar över en bok i katalogen
    Then ska boken markeras som interaktiv

  Scenario: Hovra över hjärtikon
    When jag hovrar över hjärtikonen på en bok
    Then ska hjärtikonen markeras som interaktiv

  Scenario: Hovra över "Lägg till bok"-knappen
    Given att jag har fyllt i titel och författare
    When jag hovrar över knappen "Lägg till bok"
    Then ska knappen markeras som interaktiv