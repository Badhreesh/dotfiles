-- Modify "g"lobal variables
vim.g.mapleader = ' ' -- a global var that sets the leader key (default is \)
vim.g.maplocalleader = ' '

-- vim.opt behaves like :set in vimscript
vim.opt.relativenumber = true -- Relative line number
vim.opt.ignorecase = true -- ignore uppercase chars when executing a search
vim.opt.smartcase = true -- override 'ignorecase' if search pattern has uppercase chars 
vim.opt.hlsearch = false -- dont highlight search matches
--vim.opt.showcmd = true -- show (partial) command somewhere
vim.opt.breakindent = true -- wrapped lines should have the same indent as the original line
--vim.opt.clipboard = 'unnamedplus' -- allow copying text from nvim to clipboard

-- use spaces for tabs
vim.opt.tabstop = 2 -- use 2 spaces for a tab char, instead of default 8
vim.opt.shiftwidth = 2 -- amt of chars nvim uses to indent a line. default is 8
--vim.opt.shiftround = true -- Round indent to multiple of 'shiftwidth'
vim.opt.expandtab = true -- transform a tab char to spaces

-- Create custom keybindings
vim.keymap.set('n', '<leader>w', '<cmd>write<cr>', {desc = 'Save changes'}) -- Use space + w to save changes
vim.keymap.set({'n', 'x'}, 'cp', '"+y', {desc = 'Copy to clipboard'})
vim.keymap.set({'n', 'x'}, 'cv', '"+p', {desc = 'Paste from clipboard'})
vim.keymap.set('n', 're', ':so %<cr>', {desc = 'reload config'})

vim.keymap.set({'n', 'x'}, 'x', '"_x', {desc = 'Do not change internal registers when deleting text'})
vim.keymap.set('n', '<C-j>', '<C-d>zz', {desc = 'Move down and keep cursor centered'})
vim.keymap.set('n', '<C-k>', '<C-u>zz', {desc = 'Move up and keep cursor centered'})

vim.keymap.set('n', 'yw', 'yiw', {desc = 'Yank whole word no matter where cursor is on that word'})
vim.keymap.set('n', 'cw', 'ciw', {desc = 'Change whole word no matter where cursor is on that word'})
vim.keymap.set('n', 'dw', 'diw', {desc = 'Delete whole word no matter where cursor is on that word'})

vim.keymap.set('n', 'n', 'nzz', {desc = 'Center search results'})
vim.keymap.set('n', 'N', 'Nzz', {desc = 'Center search results'})

local install_path = vim.fn.stdpath('data') .. '/site/pack/packer/start/packer.nvim'
local install_plugins = false

if vim.fn.empty(vim.fn.glob(install_path)) > 0 then
  print('Installing packer...')
  local packer_url = 'https://github.com/wbthomason/packer.nvim'
  vim.fn.system({'git', 'clone', '--depth', '1', packer_url, install_path})
  print('Done.')

  vim.cmd('packadd packer.nvim')
  install_plugins = true
end

-- Text to copy.

-- Paste copied text here.

--[[
1
2
3
4
5
two 
Two
tWo
--]]
