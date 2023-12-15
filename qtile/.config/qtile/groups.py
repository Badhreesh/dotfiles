from libqtile.config import Group, Match

def get_groups() -> list:
    groups = [
            Group("web",
                  layout="max",
                  matches=[Match(wm_class=["google-chrome"])]
                  ),
            Group("dev",
                  layout="columns",
                  matches=[Match(wm_class=["kitty", "gnome-terminal", "pycharm"])]
                  ),
            Group("teams",
                  layout="max",
                  matches=[Match(wm_class=["Microsoft Teams - Preview"])]
                  ),
            Group("misc", layout="max")
            ]
    return groups
