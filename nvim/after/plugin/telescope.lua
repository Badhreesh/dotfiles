local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ff',":lua require('telescope.builtin').find_files({ hidden = true })<CR>", {desc = 'Find all files including hidden ones'}) -- Mapping is different as I needed to pass hidden=true to func
vim.keymap.set('n', '<leader>ob',builtin.buffers, {desc = 'Display open buffers'})
vim.keymap.set('n', '<C-p>', builtin.git_files, {desc = 'Find files tracked by git'})
vim.keymap.set('n', '<leader>sf', builtin.live_grep, {desc = 'Search files for a word'})
vim.keymap.set('n', '<leader>fw', builtin.grep_string, {desc = 'Find usages of a word in files'})

require('telescope').setup{
  defaults = {
    file_ignore_patterns = {"venv", "__pycache__"},
    initial_mode = "normal",
    -- Default configuration for telescope goes here:
    -- config_key = value,
    mappings = {
      i = {
        -- map actions.which_key to <C-h> (default: <C-/>)
        -- actions.which_key shows the mappings for your picker,
        -- e.g. git_{create, delete, ...}_branch for the git_branches picker
        ["<C-h>"] = "which_key",
        ["<C-d>"] = require('telescope.actions').delete_buffer
      },
      n = {
        ["<C-d>"] = require('telescope.actions').delete_buffer
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
