# https://venthur.de/2021-12-19-managing-dotfiles-with-stow.html
all:
	stow --verbose --target=$$HOME --restow tmux/

delete:
	stow --verbose --target=$$HOME --delete tmux/ 
