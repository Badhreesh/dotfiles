from libqtile.config import Group, Match

def get_groups() -> list:
    # You can get the WM_CLASS for an application by typing xpop WM_CLASS and
    # then clicking the application window in question.
    groups = [
            Group("web",
                  layout="max",
                  matches=[Match(wm_class=["google-chrome"])]
                  ),
            Group("dev",
                  layout="columns",
                  matches=[Match(wm_class=["kitty", "Gnome-terminal", "pycharm"])]
                  ),
            Group("teams",
                  layout="max",
                  matches=[Match(wm_class=["Microsoft Teams - Preview"])]
                  ),
            Group("misc", layout="max",
                  matches=[Match(wm_class=["org.remmina.Remmina"])]
                  )
            ]
    return groups
