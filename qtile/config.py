import os
import subprocess

from libqtile import bar, hook, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from widgets import get_widgets_for_laptop, get_widgets_for_monitor

mod = "mod1"
terminal = "gnome-terminal" # guess_terminal()
browser = "google-chrome"

### Keybindings ###
keys = [
    # Focus window
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move window
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow window
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # System
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),

    # Toggles
    Key([mod], "Tab", lazy.spawn("rofi -show window"), desc="Toggle between windows"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"] , "f", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    
    # Brightness
    Key([mod], "F5",
        lazy.spawn("brightnessctl set 10%-"),
        desc="Decrease the brightness"),
    Key([mod], "F6",
        lazy.spawn("brightnessctl set 10%+"),
        desc="Increase the brightness"),
    # todo: Make dedicated set of keymaps for rofi

    # Extend to a second monitor
    # Key([mod], "m", lazy.spawn("xrandr --output DisplayPort-3 --mode 1920x1200 --right-of eDP"), desc="Extend display to a second monitor")
    # Run this command to enable using a second monitor: xrandr --output eDP --primary --auto --output DisplayPort-2 --right-of eDP --auto
]
 
### Groups ###
groups = [
        Group("web",
              layout="max",
              matches=[
                  Match(wm_class=["google-chrome"])]
              ),
        Group("dev",
              layout="columns",
              matches=[
                  Match(wm_class=["kitty", "gnome-terminal", "pycharm"])]
              ),
        Group("teams",
              layout="max",
              matches=[Match(wm_class=["teams"])]
              ),
        Group("misc", layout="max")
        ]
for group_id, group in enumerate(groups, 1):
    # mod1 + letter of group = switch to group
    switch_to_group = Key([mod], str(group_id), lazy.group[group.name].toscreen(), desc=f"Switch to group {group.name}")

    # mod1 + shift + letter of group = switch to & move focused window to group
    switch_and_move_window_to_group = Key([mod, "shift"], str(group_id), lazy.window.togroup(group.name, switch_group=True), desc=f"Switch to & move focused window to group {group.name}")
    keys.extend([switch_to_group, switch_and_move_window_to_group])

### Layouts ###
layouts = [
    # layout.MonadTall(border_focus="#4287f5", border_width=1),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()


connected_monitors = subprocess.run(
    "xrandr | busybox grep -w 'connected' | busybox cut -d' ' -f1",
    capture_output=True,
    shell=True,
    text=True
    ).stdout

external_monitors = connected_monitors.strip().split('\n')[1:] # The first monitor always refers to the laptop screen (eDP)

# todo: Move systray from second monitor to second monitor if available
laptop_monitor_widgets = get_widgets_for_laptop()
secondary_screen_widgets = get_widgets_for_monitor()

screens = [
    Screen(
        top=bar.Bar(widgets=laptop_monitor_widgets, size=24,
        wallpaper="/home/rao/Pictures/Wallpapers/Cyberpunk_Edgerunners_Lucy.jpg",)
        # wallpaper_mode="fill")
    )
]


for external_monitor in external_monitors:
    screens.append(
        Screen(
            top=bar.Bar(widgets=secondary_screen_widgets, size=24),
            wallpaper="/home/rao/Pictures/Wallpapers/Cyberpunk_Edgerunners_Lucy.jpg",
            wallpaper_mode="fill")
        )
    # Extend monitor from laptop monitor
    subprocess.run(f"xrandr --output eDP --primary --auto --output {external_monitor} --left-of eDP --auto" , shell=True)
    # Set laptop speaker as default audio sink (Name got from pactl list sinks)
    subprocess.run("pactl set-default-sink alsa_output.pci-0000_04_00.6.analog-stereo", shell=True)
    # Set laptop microphone as default audio source (Name got from pactl list sources)
    subprocess.run("pactl set-default-source alsa_input.pci-0000_04_00.6.analog-stereo", shell=True)
                
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        # Match(wm_class="blueman-manager"),  # GPG key password entry
        Match(wm_class="Blueman-manager"),  # Bluetooth manager
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
