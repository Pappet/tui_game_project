# Architecture Plan (architecture.md)

## 1\. High-Level Concept

Das Projekt wird als modulare Python-Anwendung strukturiert. Der Kern der Architektur trennt die **Game Logic** (Was passiert im Spiel?) von der **TUI Presentation** (Wie wird es angezeigt?).

Ein zentraler `GameController` (oder "Game Loop") verwaltet den aktuellen Spielzustand (z.B. `MENU`, `BATTLE`, `BASE_MANAGEMENT`) und leitet Benutzereingaben an das entsprechende Logikmodul weiter.

Für die TUI schlagen wir die Verwendung des **Textual**-Frameworks vor. Es bietet ein modernes, ereignisgesteuertes Modell, das gut zu dieser modularen Struktur passt und die Verwaltung komplexer Layouts (Basis, Team-Management, Kampf) vereinfacht.

## 2\. Directory and Module Structure

Hier ist die vorgeschlagene Verzeichnisstruktur:

```plaintext
tui_game/
├── main.py
├── core/
│   ├── __init__.py
│   ├── game_controller.py  # Manages the main game loop and state transitions
│   └── game_state.py       # Holds all persistent data (heroes, inventory, base)
│
├── tui/
│   ├── __init__.py
│   ├── app.py              # Textual App entry point
│   ├── input_handler.py    # (May be handled by Textual events)
│   └── screens/
│       ├── __init__.py
│       ├── base_screen.py    # UI for base building and progression
│       ├── battle_screen.py  # UI for combat
│       ├── hero_screen.py    # UI for hero management and equipping
│       └── main_menu.py    # UI for the main menu
│
├── game_logic/
│   ├── __init__.py
│   ├── base_manager.py     # Logic for base progression and unlocks
│   ├── battle_system.py    # Logic for handling combat mechanics
│   ├── hero_manager.py     # Logic for hero stats, leveling, and status
│   └── item_manager.py     # Logic for equipment, inventory, and item effects
│
├── data/
│   ├── items.json          # Definitions for equippable items
│   ├── heroes.json         # Definitions for hero classes/archetypes
│   └── enemies.json        # Definitions for battle encounters
│
└── utils/
    ├── __init__.py
    └── logger.py           # General utility functions (e.g., logging)
```

## 3\. Module Responsibilities

### `main.py`

  * **Verantwortung:** Der Haupteinstiegspunkt der Anwendung.
  * **Aktion:** Initialisiert und startet die Textual TUI-Anwendung (`tui/app.py`).

### `core/` (Der Kern)

  * `game_controller.py`: Der "Dirigent". Wechselt zwischen den Hauptzuständen (z.B. vom `base_screen` zum `battle_screen`). Er koordiniert die Aktionen zwischen der `tui` und der `game_logic`.
  * `game_state.py`: Das "Gehirn". Beinhaltet den gesamten *persistente* Zustand des Spiels (alle Helden, ihr Inventar, der Zustand der Basis). Dieses Modul ist dafür verantwortlich, den Spielstand zu laden und zu speichern (z.B. als JSON).

### `tui/` (Die Darstellung)

  * `app.py`: Die Haupt-Textual-Anwendungsklasse. Lädt die verschiedenen `screens`.
  * `screens/`: Jede `.py`-Datei hier repräsentiert einen Hauptbildschirm.
      * `base_screen.py`: Zeigt die Basis an, erlaubt Interaktionen für Upgrades (definiert in `game_logic/base_manager.py`).
      * `hero_screen.py`: Zeigt das 5-Personen-Team an, erlaubt das Ausrüsten von Gegenständen (Logik aus `hero_manager.py` und `item_manager.py`).
      * `battle_screen.py`: Zeigt den Kampf an (Logik aus `battle_system.py`).

### `game_logic/` (Die Regeln)

  * Dies sind "dumme" (stateless) Logik-Module. Sie erhalten den `game_state` von `core/`, führen Berechnungen durch und geben das Ergebnis zurück. Sie interagieren *niemals* direkt mit der TUI.
  * `hero_manager.py`: Verwaltet das Level-Up eines Helden, berechnet Statuswerte basierend auf der Ausrüstung.
  * `item_manager.py`: Definiert, was passiert, wenn ein Gegenstand ausgerüstet wird.
  * `battle_system.py`: Berechnet den Ausgang einer Angriffsrunde im Kampf.
  * `base_manager.py`: Verwaltet die Regeln und Kosten für Basis-Upgrades und deren Auswirkungen auf das Spiel (z.B. Freischalten neuer Ausrüstung).

## 4\. Data Flow Example (Equipping an Item)

1.  **User Input:** Der Benutzer drückt 'E' auf einem Helden im `tui/hero_screen.py`.
2.  **TUI Event:** Der `hero_screen` (Textual Widget) fängt die Eingabe ab.
3.  **Action Call:** Der Screen ruft den `core/game_controller.py` auf (z.B. `controller.equip_item(hero_id, item_id)`).
4.  **Game Logic:** Der `game_controller` ruft `game_logic/item_manager.py` auf (z.B. `item_manager.apply_item(game_state, hero_id, item_id)`).
5.  **State Update:** Der `item_manager` modifiziert das `game_state`-Objekt (z.B. fügt das Item dem Helden hinzu und entfernt es aus dem Inventar).
6.  **UI Refresh:** Der `game_controller` signalisiert der TUI (oder die TUI reagiert auf die Zustandsänderung, z.B. via Textual "watch"), dass die Daten sich geändert haben.
7.  **Render:** `tui/hero_screen.py` liest den aktualisierten `game_state` und zeichnet sich neu, um das ausgerüstete Item anzuzeigen.
