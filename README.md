# Dotfiles
This is a collection of all the dotfiles that configures the tools that I use for my development environment.

# How to install them
Clone the repo to home folder (~):
```
git clone git@github.com:Badhreesh/dotfiles.git
```
Use stow to create a symlink for the program of your choosing. For example, to use the qtile config:
```
stow qtile
```
This will place the qtile config in `~/.config/qtile`, but it just a symlink that points to `~/dotfiles/qtile/.config/qtile`.

You can also use the provided makefile to create/update or delete symlinks. It currently supports only tmux.
Create/Update:
```
make
```
Delete:
```
make delete
```
