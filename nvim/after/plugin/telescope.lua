local actions = require("telescope.actions")
local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ob',builtin.buffers, {desc = 'Display Open Buffers'})
vim.keymap.set('n', '<leader>ff',":lua require('telescope.builtin').find_files({ hidden = true })<CR>", {desc = 'Find all files including hidden ones'}) -- Mapping is different as I needed to pass hidden=true to func
vim.keymap.set('n', '<leader>gf', builtin.git_files, {desc = 'Find files tracked by Git'})
vim.keymap.set('n', '<leader>ss', builtin.live_grep, {desc = 'Search for a String'})
vim.keymap.set('n', '<leader>sf', builtin.grep_string, {desc = 'Search Files for usages of a word'})

require('telescope').setup{
  defaults = {
    file_ignore_patterns = {"venv", "__pycache__"},
    -- Default configuration for telescope goes here:
    -- config_key = value,
    mappings = {
      i = {
        -- map actions.which_key to <C-h> (default: <C-/>)
        -- actions.which_key shows the mappings for your picker,
        -- e.g. git_{create, delete, ...}_branch for the git_branches picker
        ["<C-h>"] = "which_key",
        -- ["<C-d>"] = actions.delete_buffer,
        ["<esc>"] = actions.close -- Quit in insert mode
      },
      n = {
        -- ["<C-d>"] = require('telescope.actions').delete_buffer
      }
    }
  },
  pickers = {
    -- Default configuration for builtin pickers goes here:
    -- picker_name = {
    --   picker_config_key = value,
    --   ...
    -- }
    -- Now the picker_config_key will be applied every time you call this
    -- builtin picker
  },
  extensions = {
    -- Your extension configuration goes here:
    -- extension_name = {
    --   extension_config_key = value,
    -- }
    -- please take a look at the readme of the extension you want to configure
  }
}
