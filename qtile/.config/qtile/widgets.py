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

def image() -> widget.Image:
    return widget.Image(
            filename="~/.config/qtile/ubuntu-logo.png", 
            mouse_callbacks={"Button1": lazy.next_layout()}
             )


def separator() -> widget.Sep:
    return widget.Sep(foreground=colours[2], linewidth=1, padding=10)


def group_box() -> widget.GroupBox:
   return widget.GroupBox(disable_drag=True, highlight_method="line")


def current_layout_icon() -> widget.CurrentLayoutIcon:
    return widget.CurrentLayoutIcon()


def current_layout() -> widget.CurrentLayout:
    return widget.CurrentLayout()


def window_name() -> widget.WindowName:
    return widget.WindowName()


def systray() -> widget.Systray:
    return widget.Systray()


def pulse_volume() -> widget.PulseVolume:
    return widget.PulseVolume(foreground=colours[6], fmt="󰕾 {}", volume_app="pactl", step=5)


def brightness() -> widget.Backlight:
    return widget.Backlight(backlight_name='amdgpu_bl0', change_comand='brightnessctl set {0:.0f}+', fmt='󰃞 {}')


def battery() -> widget.Battery:
    return widget.Battery(
            foreground=colours[4], # Green
            format="{char}{percent:2.0%}",
            charge_char="󰂄 ",
            discharge_char=" ",
            empty_char=" ",
            full_char="󰁹 ",
            unknown_char=" ",
            low_foreground=colours[3], # Red Background color on low battery
            low_percentage=0.15, # Show low_forground color at 15% battery
            show_short_text=False,
            notify_below=15)


def clock() -> widget.Clock:
    return widget.Clock(format=" %a %b %d %H:%M", foreground=colours[7])


def exit() -> widget.QuickExit:
    return widget.QuickExit()


def get_widgets_for_laptop():
    widgets = [
            image(),
            separator(),
            group_box(),
            separator(),
            current_layout_icon(),
            current_layout(),
            separator(),
            window_name(),
            separator(),
            systray(),
            separator(),
            pulse_volume(),
            separator(),
            brightness(),
            separator(),
            battery(),
            separator(),
            clock(),
            separator(),
            exit()
            ]
    return widgets


def get_widgets_for_monitor():
    widgets = [
            image(),
            separator(),
            group_box(),
            separator(),
            current_layout_icon(),
            current_layout(),
            separator(),
            window_name(),
            separator(),
            pulse_volume(),
            separator(),
            brightness(),
            separator(),
            battery(),
            separator(),
            clock(),
            separator(),
            exit()
            ]
    return widgets


