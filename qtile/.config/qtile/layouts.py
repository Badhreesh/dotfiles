from libqtile import layout


def get_layouts() -> list:
    layouts = [
            layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
            layout.Max()
            ]
    return layouts

    # layout.MonadTall(border_focus="#4287f5", border_width=1),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
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

