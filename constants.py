# General Bot Messages

DM_WELCOME_MESSAGE: str = "Hi there, welcome to Cervinakuy Resources. I'm Simon the help bot!\n"\
                          "If you have a question regarding KitPvP, please feel free to ask me before posting in the "\
                          "support channel - I'm happy to help 😃"

UNSURE_MESSAGE: str = "Sorry, I'm not really sure how to help you with that. Try again using different phrasing " \
                      "in your question."

ONLY_HELPCHAT_ATTACHMENTS: str = "{} Your message has been removed. Please use https://paste.helpch.at for any " \
                                 "logs/errors/files"

# Bot Help Responses

SIGNS_MESSAGE: str = "If normal players are unable to use KitPvP signs, this may be because spawn-protection in the " \
                     "server.properties is not set to 0. This is not a permissions issue."

LEADERBOARD_MESSAGE: str = "KitPvP supports creating Leaderboards for top kills, deaths, and level. Learn more: " \
                           "<https://bit.ly/kp-leaderboards>"

COMMAND_FORMAT_MESSAGE: str = "Commands globally across KitPvP use the same format, and support PlaceholderAPI. " \
                         "Learn more: <https://bit.ly/kp-command-format>"

NO_KIT_MESSAGE: str = "To disable the No Kit Protection system (“You cannot hit that player because they have no " \
                      "kit”) please disable NoKitProtection in the config.yml. Learn more: " \
                      "<https://bit.ly/kp-config-nokitprotection>"

INSTALLATION_MESSAGE: str = "To learn how to setup KitPvP, please see the installation guide: " \
                            "<https://bit.ly/kp-installation>"

PERMISSION_MESSAGE: str = "If players encounter a “You do not have permission message“, please learn more about " \
                          "setting up a permissions plugin: <https://bit.ly/kp-permissions-setup-1>. Otherwise, view " \
                          "a full list of KitPvP permissions: <https://bit.ly/kp-permissions>"

RANK_MESSAGE: str = "The chat format supports PlaceholderAPI placeholders, rank prefixes, and can easily be modified " \
                    "or disabled. It is only visible in arena worlds. Learn more: <https://bit.ly/kp-chat-format>"

ORIGINAL_FILES_MESSAGE: str = "If you are looking for original copies of any .yml file, they can be found on the " \
                              "GitHub: <https://github.com/cervinakuy/KitPvP/tree/master/src/main/resources>"

CONFIG_FILE_MESSAGE: str = "For documentation on the config.yml, please see: <https://bit.ly/kp-config>"

LEVELS_FILE_MESSAGE: str = "For documentation on the levels.yml, please see: <https://bit.ly/kp-levels>"

SCOREBOARD_FILE_MESSAGE: str = "For documentation on the scoreboard.yml, please see: <https://bit.ly/kp-scoreboard>."

SIGN_FILE_MESSAGE: str = "For documentation on the signs.yml, please see: <https://bit.ly/kp-signs>"

KILLSTREAKS_FILE_MESSAGE: str = "For documentation on the killstreaks.yml, please see: <https://bit.ly/kp-killstreaks>"

MENU_FILE_MESSAGE: str = "For documentation on the menu.yml, please see: <https://bit.ly/kp-menu>"

PVP_NOT_PERMITTED_MESSAGE: str = "If players are unable to use abilities due to a “PVP is not permitted in this " \
                                 "region” message, ensure the `pvp` flag in that region is set to `allow` using" \
                                 " WorldGuard. Learn more: <https://bit.ly/kp-pvp-not-allowed>"

FANCY_DEATH_MESSAGE: str = "To disable the death title and timer, toggle `FancyDeath` under `Arena` in the " \
                           "config.yml. If players are stuck in spectator mode, ensure you are running the latest " \
                           "version of your server version (example: if running 1.14, make sure you are running " \
                           "1.14.4, the latest version of 1.14) as some older versions have some sound bugs " \
                           "interrupting regular respawn."

INVENTORY_MESSAGE: str = "If players are losing their inventory when joining or leaving the arena, you must install " \
                         "a plugin such as Multiverse-Inventories, PerWorldInventory, or a variant to manage separate " \
                         "inventories across multiple worlds. KitPvP does not offer this functionality."

LEAVE_ITEM_MESSAGE: str = "If the “Return to Hub” item is not functioning, or you require assistance setting it up, " \
                          "please see: <https://bit.ly/kp-leave-item>"

PLACEHOLDERS_MESSAGE: str = "If placeholders such as %kitpvp_stats_kills%, %kitpvp_stats_deaths%, etc. are not " \
                            "working, ensure you have PlaceholderAPI installed. If already installed and the " \
                            "placeholder is not working in a hologram, please see: <https://bit.ly/kp-leaderboards>. " \
                            "For a complete list of KitPvP placeholders: <https://bit.ly/kp-placeholders-1>"

ONEVONE_MESSAGE: str = "Although on the to-do list, KitPvP does not currently offer any 1v1 features. However, this " \
                       "feature can likely be added through external plugins in the meantime."

UNLOCK_KIT_MESSAGE: str = "Players can unlock kits at a certain level. To implement this functionality into your own " \
                          "custom kit, learn more about the `Level` kit setting: <https://bit.ly/kit-level-setting>"

SCOREBOARD_NOT_WORKING_MESSAGE: str = "If the scoreboard is not appearing, this is likely due to 3 potential " \
                                      "reasons:\n " \
                                      "1) conflicting plugin: another plugin is interfering with displaying the " \
                                      "scoreboard. To identify the conflicting plugin, uninstall all plugins besides " \
                                      "KitPvP, and reinstall 1-by-1 until the causing plugin is found\n" \
                                      "2) scoreboard title is too long: If the configured title in the scoreboard.yml " \
                                      "is too long, Minecraft cannot properly display the scoreboard. Try using a very " \
                                      "short title to check whether this is the cause\n" \
                                      "3) too many lines: a scoreboard can only contain 16 lines, max. Anything " \
                                      "above this number will not display the scoreboard"

FILES_RESETTING_MESSAGE: str = "If your KitPvP plugin files are resetting, this is typically not a result of the " \
                               "plugin. Rather, there are some syntax errors in your files that confuses the parser, " \
                               "and subsequently resets the corrupted file to a safe state. To identify and resolve " \
                               "the syntax error(s) causing the file reset, use tools such as <https://yaml.helpch.at>"