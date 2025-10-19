"""
base_screen.py

Implements the Textual Screen for the base management view.
This UI allows the player to see their base status and interact
with upgrades.
"""

from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button
from textual.containers import VerticalScroll
from textual.app import ComposeResult
# Import TYPE_CHECKING for type hinting GameApp
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tui.app import GameApp

class BaseScreen(Screen):
    """
    The screen for managing the player's base.

    Attributes:
        app (GameApp): The main application instance.
    """
    app: "GameApp"

    def compose(self) -> ComposeResult:
        """
        Create the child widgets for the base screen.
        Upgrade list is populated in on_mount.
        """
        yield Header(name="My Base")

        with VerticalScroll(id="base_layout"):
            yield Static("Base Management Screen")
            yield Static("Current Upgrades:", id="upgrades_header")
            # --- Upgrade list will be mounted here dynamically ---

            yield Button("Upgrade Barracks (Stub)", id="btn_upgrade_barracks")
            yield Button("Return to Main Menu", id="btn_main_menu")

        yield Footer()

    def on_mount(self) -> None:
        """
        Called when the screen is mounted. Loads the current base status
        and dynamically creates widgets to display it.
        """
        print("BaseScreen mounted.")
        # Access the base_status from the game state via the controller
        base_status = self.app.controller.game_state.base_status
        base_layout = self.query_one("#base_layout", VerticalScroll)

        print(f"Loading base status: {base_status}") # Debug print

        if not base_status:
             base_layout.mount(Static("No buildings yet.", classes="upgrade_item"))
        else:
            # Dynamically mount Static widgets for each building
            # Mount them after the header
            for building, level in base_status.items():
                upgrade_widget = Static(
                    f"[{building.capitalize()} - Lvl {level}]",
                    classes="upgrade_item"
                )
                base_layout.mount(upgrade_widget, after="#upgrades_header")

        # Future: Potentially update button text/state based on game_state

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events.
        """
        if event.button.id == "btn_upgrade_barracks":
            print("Stub: 'Upgrade Barracks' button pressed.")
            # Future: Call controller to handle logic
            # building_id = "barracks" # Or determine dynamically
            # success = self.app.controller.upgrade_building(building_id)
            # if success:
            #     # Refresh the screen or update the specific widget
            #     self.refresh_base_display() # Needs implementation
            # else:
            #     # Show feedback (e.g., notification)
            #     pass

        elif event.button.id == "btn_main_menu":
            # print("Stub: 'Return to Main Menu' button pressed.")
            # Pop screen to return to the previous one (MainMenuScreen)
            self.app.pop_screen()

    # Helper method example (for future use when upgrades happen)
    # def refresh_base_display(self) -> None:
    #     """
    #     Clears and re-populates the base upgrade list.
    #     """
    #     base_layout = self.query_one("#base_layout", VerticalScroll)
    #     # Remove old upgrade items
    #     for widget in base_layout.query(".upgrade_item"):
    #         widget.remove()
    #
    #     # Re-mount current status (similar to on_mount logic)
    #     base_status = self.app.controller.game_state.base_status
    #     if not base_status:
    #          base_layout.mount(Static("No buildings yet.", classes="upgrade_item"))
    #     else:
    #         for building, level in base_status.items():
    #              upgrade_widget = Static(f"[{building.capitalize()} - Lvl {level}]", classes="upgrade_item")
    #              base_layout.mount(upgrade_widget, after="#upgrades_header")
    #     print("Base display refreshed.")