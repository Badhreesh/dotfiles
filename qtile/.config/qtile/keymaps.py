import os

from dotenv import load_dotenv
from libqtile.config import Key
from libqtile.lazy import lazy

load_dotenv()

mod = os.getenv("MOD", "mod1")
terminal = os.getenv("TERMINAL", "kitty")
browser = os.getenv("BROWSER", "google-chrome")


def get_keys() -> list:
    keys = [
        # Focus window
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key(
            [mod], "space", lazy.layout.next(), desc="Move window focus to other window"
        ),
        # Focus screen
        Key([mod], "period", lazy.prev_screen(), desc="Move focus to previous screen"),
        Key([mod], "comma", lazy.next_screen(), desc="Move focus to next screen"),
        # Move window
        Key(
            [mod, "shift"],
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [mod, "shift"],
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow window
        Key(
            [mod, "control"],
            "h",
            lazy.layout.grow_left(),
            desc="Grow window to the left",
        ),
        Key(
            [mod, "control"],
            "l",
            lazy.layout.grow_right(),
            desc="Grow window to the right",
        ),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        # System
        Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        # Fullscreen
        Key(
            [mod],
            "f",
            lazy.window.toggle_fullscreen(),
            desc="Toggle fullscreen on the focused window",
        ),
        # Toggles
        # Key([mod], "Tab", lazy.spawn("rofi -show window"), desc="Toggle between windows"),
        Key(["mod1"], "Tab", lazy.group.next_window(), desc="Focus next window"),
        Key([mod], "q", lazy.next_layout(), desc="Toggle between layouts"),
        Key(
            [mod],
            "t",
            lazy.window.toggle_floating(),
            desc="Toggle floating on the focused window",
        ),
        # Apps
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod, "control"], "f", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
        Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
        # Brightness
        Key(
            [mod],
            "F5",
            lazy.spawn("brightnessctl set 10%-"),
            desc="Decrease the brightness",
        ),
        Key(
            [mod],
            "F6",
            lazy.spawn("brightnessctl set 10%+"),
            desc="Increase the brightness",
        ),
        # todo: Make dedicated set of keymaps for rofi
        # Extend to a second monitor
        # Key([mod], "m", lazy.spawn("xrandr --output DisplayPort-3 --mode 1920x1200 --right-of eDP"), desc="Extend display to a second monitor")
        # Run this command to enable using a second monitor: xrandr --output eDP --primary --auto --output DisplayPort-2 --right-of eDP --auto
    ]
    return keys
