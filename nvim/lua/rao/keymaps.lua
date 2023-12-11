-- Modes
-- normal_mode = "n"
-- insert_mode = "i"
-- visual_mode = "v"
-- visual_block_mode = "x"
-- terminal_mode = "t"
-- command_mode = "c"

local set = vim.keymap.set
-- local set = vim.api.nvim_set_keymap

set('n', '<leader>w', ':w<CR>', {desc = 'Save changes'}) -- Use space + w to save changes
set({'n', 'x'}, 'cp', '"+y', {desc = 'Copy to clipboard'})
set({'n', 'x'}, 'cv', '"+p', {desc = 'Paste from clipboard'})

set('i', '<C-l>', '<Esc>w', {desc = 'evim version of exiting insert mode. Also go to next word.'})
set({'n', 'x'}, 'x', '"_x', {desc = 'Do not change internal registers when deleting text'})
set('n', '<C-d>', '<C-d>zz', {desc = 'Move down and keep cursor centered'})
set('n', '<C-u>', '<C-u>zz', {desc = 'Move up and keep cursor centered'})
set('n', '<C-o>', '<C-o>zz', {desc = 'Move to previous jump and keep cursor centered'})
set("n", "J", "mzJ`z", {desc = 'Take the line below you and append to current line with a space, while keeping cursor in place'})

set('n', 'cw', 'ciw', {desc = 'Change whole word no matter where cursor is on that word'})
set('n', 'dw', 'diw', {desc = 'Delete whole word no matter where cursor is on that word'})
set('n', 'vw', 'viw', {desc = 'Highlight whole word no matter where cursor is on that word'})
set('n', 'yw', 'yiw', {desc = 'Yank whole word no matter where cursor is on that word'})

set('n', 'n', 'nzzzv', {desc = 'Center search results'})
set('n', 'N', 'Nzzzv', {desc = 'Center search results'})
set('x', '<leader>p', '\"_dP', {desc = 'Do a delete to the _ register and paste content in visual block mode. This ensures copied text will not be overwritten with deleted text.'})


-- '> is a mark assigned by vim to identify the selection end
-- '>+1 is one line after last selected line
-- For the visual-mode mappings, gv reselects the last visual block and = re-indents that block.
set("v", "J", ":m '>+1<CR>gv=gv", {desc = 'Move block of selected lines down one line and indent if needed'})
set("v", "K", ":m '<-2<CR>gv=gv",{desc = 'Move block of selected lines up one line and indent if needed'} )

-- copy to system clipboard
set({"n", "v"}, "<leader>y", "\"+y", {desc = 'Yank text into system clipboard'})
set({"t"}, "<Esc>", "<C-\\><C-n>", {desc = 'Escape from insert mode in terminal buffer'})

set('n', ',', 'y$', {desc = 'Yank text till end of line'})
set('n', '.', '$p', {desc = 'Paste yanked text to end of line'})

-- highlight yanked text for 100ms using the "Visual" highlight group
vim.cmd[[
augroup highlight_yank
autocmd!
au TextYankPost * silent! lua vim.highlight.on_yank({higroup="Visual", timeout=100})
augroup END
]]

-- Remap to easily run a go script
-- au FileType go map <leader>r :!go run %<CR>

-- Better window navigation
set("n", "<C-h>", "<C-w>h", {desc="Navigate to window on left"})
set("n", "<C-j>", "<C-w>j", {desc="Navigate to window on down"})
set("n", "<C-k>", "<C-w>k", {desc="Navigate to window on up"})
set("n", "<C-l>", "<C-w>l", {desc="Navigate to window on right"})

set("n", "<leader>e", ":NvimTreeToggle<CR>", {desc = 'Open nvim-tree as the file explorer'})

-- Better tab navigation
set('n', '<leader>h', 'gT', {desc = 'Go to tab on the left'})
set('n', '<leader>l', 'gt', {desc = 'Go to tab on the right'})

-- Resize with arrows
set("n", "<C-Up>", ":resize +2<CR>")
set("n", "<C-Down>", ":resize -2<CR>")
set("n", "<C-Left>", ":vertical resize -2<CR>")
set("n", "<C-Right>", ":vertical resize +2<CR>")

-- Navigate buffers (These keymaps are already bound to moving cursor to top/bottom of view by default)
set("n", "<S-l>", ":bnext<CR>")
set("n", "<S-h>", ":bprevious<CR>")


-- VISUAL
set("v", "p", '"_dP', {desc = 'Do a delete to the _ register and paste content in visual mode. This ensures copied text will not be overwritten with deleted text.'})
