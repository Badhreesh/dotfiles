from libqtile import widget
from libqtile.lazy import lazy

colours = [
    ["#1f2329", "#1f2329"],  # Background
    ["#dcdcdc", "#dcdcdc"],  # Foreground
    ["#535965", "#535965"],  # Grey Colour
    ["#e55561", "#e55561"],
    ["#54f542", "#54f542"],
    ["#e2b86b", "#e2b86b"],
    ["#4fa6ed", "#4fa6ed"],
    ["#bf68d9", "#bf68d9"],
    ["#48b0bd", "#48b0bd"],
    ["#eff542", "#eff542"] # yellow
]

def get_widgets_for_laptop():
    seperator = widget.Sep(foreground=colours[2], linewidth=1, padding=10)
    widgets = [
            widget.Image(filename="~/.config/qtile/python-logo.png",
                     mouse_callbacks={
                         "Button1": lazy.next_layout(),
                         }
                     ),
            seperator,
            widget.GroupBox(disable_drag=True, highlight_method="line"),
            seperator,
            widget.CurrentLayoutIcon(),
            widget.CurrentLayout(),
            # seperator,
            #  widget.Prompt(),
            seperator,
            widget.WindowName(),
            seperator,
            widget.Chord(
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.Systray(),
            seperator,
            widget.PulseVolume(foreground=colours[6], fmt="<u>墳 {}</u>", volume_app="pactl", step=5),
                           # volume_up_command="pactl set-sink-volume @DEFAULT_SINK@ +10%",
                           # volume_down_command="pactl set-sink-volume @DEFAULT_SINK@ -10%"),
            seperator,
            widget.Backlight(backlight_name='amdgpu_bl0', change_comand='brightnessctl set {0:.0f}+', fmt='<u>󰃞 : {}</u>'),
            seperator,
            widget.Battery(
                foreground=colours[4], # Green
                format="<u>{char} {percent:2.0%}</u>",
                charge_char=" ",
                discharge_char=" ",
                empty_char=" ",
                full_char=" ",
                unknown_char=" ",
                low_foreground=colours[3], # Red Background color on low battery
                low_percentage=0.15, # Show low_forground color at 15% battery
                show_short_text=False,
                notify_below=15),
            seperator,
            widget.Clock(format=" %a %b %d %H:%M", foreground=colours[7]),
            seperator,
            widget.QuickExit()
            ]
    return widgets


def get_widgets_for_monitor():
    seperator = widget.Sep(foreground=colours[2], linewidth=1, padding=10)
    widgets = [
            widget.Image(filename="~/.config/qtile/python-logo.png",
                     mouse_callbacks={
                         "Button1": lazy.next_layout(),
                         }
                     ),
            seperator,
            widget.GroupBox(disable_drag=True, highlight_method="line"),
            seperator,
            widget.CurrentLayoutIcon(),
            widget.CurrentLayout(),
            # seperator,
            #  widget.Prompt(),
            seperator,
            widget.WindowName(),
            seperator,
            widget.Chord(
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            seperator,
            widget.PulseVolume(foreground=colours[6], fmt="<u>墳 {}</u>", volume_app="pactl", step=5),
                           # volume_up_command="pactl set-sink-volume @DEFAULT_SINK@ +10%",
                           # volume_down_command="pactl set-sink-volume @DEFAULT_SINK@ -10%"),
            seperator,
            widget.Backlight(backlight_name='amdgpu_bl0', change_comand='brightnessctl set {0:.0f}+', fmt='<u>󰃞 : {}</u>'),
            seperator,
            widget.Battery(
                foreground=colours[4], # Green
                format="<u>{char} {percent:2.0%}</u>",
                charge_char=" ",
                discharge_char=" ",
                empty_char=" ",
                full_char=" ",
                unknown_char=" ",
                low_foreground=colours[3], # Red Background color on low battery
                low_percentage=0.15, # Show low_forground color at 15% battery
                show_short_text=False,
                notify_below=15),
            seperator,
            widget.Clock(format=" %a %b %d %H:%M", foreground=colours[7]),
            seperator,
            widget.QuickExit()
            ]
    return widgets


