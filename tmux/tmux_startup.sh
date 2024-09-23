#!/usr/bin/bash
SESH="tmux_session"
# Start a new detached tmux session named work
tmux new-session -d -s $SESH -n "GP"

# Create "GP" window
# tmux rename-window GP

tmux send-keys -t $SESH:GP "cd projects/gp/scanfeld-pylib" Enter
tmux send-keys -t $SESH:GP "code ." Enter
tmux send-keys -t $SESH:GP "clear" C-m

# Create "playground" window
tmux new-window -t $SESH -dnplayground 

# Attach to the tmux session
tmux a -t $SESH

