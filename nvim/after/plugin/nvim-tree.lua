require("nvim-tree").setup({
    diagnostics = {
        enable = false,
        icons = {
            hint = "",
            info = "",
            warning = "",
            error = "",
        },
    },
    renderer = {
        add_trailing = false, -- Appends a trailing slash to folder names
        group_empty = false, -- Compact folders that only contain a single folder into one node. 
        full_name = false, -- Display node whose name length is wider than the width of nvim-tree window in floating window.
        root_folder_label = ":~:s?$?/..?", -- In what format to show root folder.
        indent_width = 2, -- Number of spaces for an each tree nesting level. Minimum 1.
        special_files = { "Cargo.toml", "Makefile", "README.md", "readme.md" }, -- A list of filenames that gets highlighted with `NvimTreeSpecialFile`.
        symlink_destination = true, -- Whether to show the destination of the symlink.
        highlight_git = false, -- Enable highlight for git attributes using `NvimTreeGit*` highlight groups.
        highlight_diagnostics = false, -- Enable highlight for diagnostics using `LspDiagnosticsError*Text` highlight groups.
        highlight_opened_files = "none", -- Highlight icons and/or names for |bufloaded()| files using the `NvimTreeOpenedFile` highlight group.
        highlight_modified = "none", -- Highlight icons and/or names for modified files using the `NvimTreeModifiedFile` highlight group.
        highlight_clipboard = "name", -- Enable highlight for clipboard items using the `NvimTreeCutHL` and `NvimTreeCopiedHL` groups.
        indent_markers = { -- Configuration options for tree indent markers.
            enable = true, -- Display indent markers when folders are open
            inline_arrows = true, -- Display folder arrows in the same column as indent marker when using |renderer.icons.show.folder_arrow|
            icons = { -- Icons shown before the file/directory. Length 1.
                corner = "└",
                edge = "│",
                item = "│",
                bottom = "─",
                none = " ",
                },
            },
        icons = {
            web_devicons = {
                file = {
                    enable = true,
                    color = true,
                },
                folder = {
                    enable = false,
                    color = true,
                },
            },
            git_placement = "before", -- Place where the git icons will be rendered
            diagnostics_placement = "signcolumn",
            modified_placement = "after", -- Place where the modified icon will be rendered.
            padding = " ", -- Inserted between icon and filename.
            symlink_arrow = " ➛ ", -- Used as a separator between symlinks' source and target.
            show = { -- Configuration options for showing icon types.
                file = true,
                folder = true,
                folder_arrow = true,
                git = true,
                diagnostics = true,
                modified = true,
            },
            glyphs = {
                default = "",
                symlink = "",
                bookmark = "󰆤",
                modified = "●",
                folder = {
                    arrow_closed = "",
                    arrow_open = "",
                    default = "",
                    open = "",
                    empty = "",
                    empty_open = "",
                    symlink = "",
                    symlink_open = "",
                },
                git = {
                    unstaged = "",
                    staged = "S",
                    unmerged = "",
                    renamed = "➜",
                    untracked = "U",
                    deleted = "",
                    ignored = "◌",
                },
            },
        },
    },
})


