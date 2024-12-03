import os
import subprocess

from dotenv import load_dotenv
from groups import get_groups
from keymaps import get_keys
from layouts import get_layouts
from libqtile import bar, hook, layout
from libqtile.config import Click, Drag, Key, Match, Screen
from libqtile.lazy import lazy
from widgets import get_widgets_for_laptop, get_widgets_for_monitor

load_dotenv()
mod = os.getenv("MOD", "mod1")
terminal = os.getenv("TERMINAL", "gnome-terminal")
browser = os.getenv("BROWSER", "google-chrome")

keys = get_keys()
groups = get_groups()
layouts = get_layouts()

# Extend keys with group related keybindings
for group_id, group in enumerate(groups, 1):
    # mod1 + letter of group = switch to group
    switch_to_group = Key(
        [mod],
        str(group_id),
        lazy.group[group.name].toscreen(),
        desc=f"Switch to group {group.name}",
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    switch_and_move_window_to_group = Key(
        [mod, "shift"],
        str(group_id),
        lazy.window.togroup(group.name, switch_group=True),
        desc=f"Switch to & move focused window to group {group.name}",
    )
    keys.extend([switch_to_group, switch_and_move_window_to_group])

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

connected_monitors = subprocess.run(
    "xrandr | busybox grep -w 'connected' | busybox cut -d' ' -f1",
    capture_output=True,
    shell=True,
    text=True,
).stdout


# todo: Move systray from second monitor to second monitor if available
laptop_monitor_widgets = get_widgets_for_laptop()
secondary_screen_widgets = get_widgets_for_monitor()
home = os.path.expanduser("~")

screens = [
    Screen(
        top=bar.Bar(widgets=laptop_monitor_widgets, size=24, background="#141415"),
        wallpaper=home + "/.config/qtile/walls/Kita_Philosophy.png",
        wallpaper_mode="fill",
    )
]

external_monitors = connected_monitors.strip().split("\n")[
    1:
]  # The first monitor always refers to the laptop screen (eDP)
for external_monitor in external_monitors:
    screens.append(
        Screen(
            top=bar.Bar(
                widgets=secondary_screen_widgets, size=24, background="#141415"
            ),
            wallpaper=home + "/.config/qtile/walls/Kita_Philosophy.png",
            wallpaper_mode="fill",
        )
    )
# Extend monitor from laptop monitor (Got the xrandr comand by running arandr)
subprocess.run(
    "xrandr --output eDP --primary --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-A-0 --off --output DisplayPort-0 --off --output DisplayPort-1 --off --output DisplayPort-2 --mode 1920x1200 --pos 3840x0 --rotate normal --output DisplayPort-3 --off --output DisplayPort-4 --mode 1920x1200 --pos 1920x0 --rotate normal --output DisplayPort-5 --off",
    shell=True,
)
# Set laptop speaker as default audio sink (Name got from pactl list sinks)
subprocess.run(
    "pactl set-default-sink alsa_output.pci-0000_04_00.6.analog-stereo", shell=True
)
# Set laptop microphone as default audio source (Name got from pactl list sources)
subprocess.run(
    "pactl set-default-source alsa_input.pci-0000_04_00.6.analog-stereo", shell=True
)

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
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
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])
