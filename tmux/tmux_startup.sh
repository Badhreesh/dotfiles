#!/usr/bin/bash

# Start a new detached tmux session named work
tmux new-session -d -s work

# Create "GP" window
tmux rename-window GP

# Create "playground" window
tmux new-window -t work -dnplayground 

# Attach to the tmux session
tmux a -t work

