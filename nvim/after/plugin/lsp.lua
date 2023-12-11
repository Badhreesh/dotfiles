local lsp_zero = require('lsp-zero')

-- when LSP is attached to the buffer, run the function
-- read up on jumplist (C-o and C-i) and taglist (C-t)
lsp_zero.on_attach(function(client, bufnr)
  print("LSP has attached to this buffer")
  local opts = {buffer=bufnr}
  vim.keymap.set("n", "<leader>k", vim.lsp.buf.hover, opts)
  lsp_zero.default_keymaps({buffer = bufnr})
end)

-- (Optional) Configure lua language server for neovim
-- require('lspconfig').lua_ls.setup(lsp.nvim_lua_ls())
-- require('lspconfig').rust_analyzer.setup({})

require('mason').setup({})
require('mason-lspconfig').setup({
  ensure_installed = {'lua_ls', 'pyright', 'gopls', 'rust_analyzer'},
  handlers = {
    lsp_zero.default_setup,
    -- rust_analyzer = function()
    --     require('lspconfig').rust_analyzer.setup({
    --     settings = {
    --     ['rust-analyzer'] = {
    --         diagnostics = {
    --             enable = true
    --         }
    --     }
    -- }
    -- })
    -- end,
  }
})
-- local nvim_lsp = require'lspconfig'
--
-- local on_attach = function(client)
--     require'completion'.on_attach(client)
-- end
--
-- nvim_lsp.rust_analyzer.setup({
--     on_attach=on_attach,
--     settings = {
--         ["rust-analyzer"] = {
--             imports = {
--                 granularity = {
--                     group = "module",
--                 },
--                 prefix = "self",
--             },
--             cargo = {
--                 buildScripts = {
--                     enable = true,
--                 },
--             },
--             procMacro = {
--                 enable = true
--             },
--         }
--     }
-- })

lsp_zero.set_sign_icons({
  error = '✘',
  warn = '',
  hint = '⚑',
  info = '»'
})

-- lsp.setup()

local cmp = require("cmp")
cmp.setup({
	mapping = {
		['<Tab>'] = cmp.mapping.confirm({select = true})
	}
})

