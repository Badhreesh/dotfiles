-- Modify "g"lobal variables
vim.g.mapleader = " " -- a global var that sets the leader key (default is \)
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

local opt = vim.opt -- vim.opt behaves like :set in vimscript

opt.number = true -- Set line number
opt.relativenumber = true -- Relative line number
opt.ignorecase = true -- ignore uppercase chars when executing a search
opt.smartcase = true -- override 'ignorecase' if search pattern has uppercase chars 
--opt.showcmd = true -- show (partial) command somewhere
opt.breakindent = true -- wrapped lines should have the same indent as the original line
--opt.clipboard = 'unnamedplus' -- allow copying text from nvim to clipboard
opt.tabstop = 4 -- insert 4 spaces for a tab
opt.softtabstop = 4 -- number of spaces that <Tab> uses while editing
opt.shiftwidth = 4 -- number of spaces inserted for each indentation
opt.expandtab = true -- convert tabs to spaces
opt.hlsearch = false -- dont highlight search matches
opt.termguicolors = true -- enable 24-bit RGB color in the terminal UI
opt.colorcolumn = "80"
opt.splitbelow = true -- force all horizontal splits to go below current window
opt.splitright = true -- force all vertical splits to go below current window
opt.numberwidth = 2 -- set number column width to 2 (default is 4)
opt.cursorline = true -- highlight the current line

-- Use vim.cmd to run vimscript
-- Make - as part of a keyword. This makes it easier to navigate words and edit them. asdf-asdf will now be deleted as one word. To revert, set iskeyword-=-
vim.cmd [[set iskeyword+=-]]

