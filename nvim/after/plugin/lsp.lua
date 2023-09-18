local lsp = require('lsp-zero').preset({})

-- when LSP is attached to the buffer, run the function
-- read up on jumplist (C-o and C-i) and taglist (C-t)
lsp.on_attach(function(client, bufnr)
  print("LSP has attached to this buffer")
  local opts = {buffer=bufnr}
  vim.keymap.set("n", "<leader>k", vim.lsp.buf.hover, opts)
  lsp.default_keymaps({buffer = bufnr})
end)

-- (Optional) Configure lua language server for neovim
require('lspconfig').lua_ls.setup(lsp.nvim_lua_ls())

lsp.set_sign_icons({
  error = '✘',
  warn = '',
  hint = '⚑',
  info = '»'
})

lsp.setup()

local cmp = require("cmp")
cmp.setup({
	mapping = {
		['<Tab>'] = cmp.mapping.confirm({select = true})
	}
})

