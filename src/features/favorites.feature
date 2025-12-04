# language: sv

# US4] Som en användare,
# vill jag kunna favoritmarkera böcker i katalogen
# så att jag kommer ihåg vilka jag läst och tyckt om

# [US5] Som en användare,
# vill jag kunna se en lista över mina favoritböcker
# så att jag får en samlad överblick av dem

# [US6] Som en användare,
# vill jag kunna avmarkera favoritböcker
# så att jag kan ta bort böcker ur min favoritlista

Feature: Hantering av favoritböcker

  Background: att jag befinner på mig "Katalog"-fliken

  Scenario: Favoritmarkera en bok
    Given att en bok inte är favoritmarkerad
    When jag klickar på hjärtikonen
    Then ska boken markeras som favorit

  Scenario: Visa lista över favoritböcker
    Given att jag har minst en favoritmarkerad bok
    When jag navigerar till sidan "Mina böcker"
    Then ska jag se en lista med mina favoritmarkerade böcker

  Scenario: Avmarkera en favoritbok
    Given att en bok redan är favoritmarkerad
    When jag klickar på hjärtikonen igen
    Then ska boken inte längre vara favorit
    And den ska inte längre visas på sidan "Favoriter"