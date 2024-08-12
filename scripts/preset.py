import cfw
import overlay
import payload
import sysmodule
import homebrew


class Preset():
    def handle_module(self):
        self.out = [
            {
                "name": "Minimal",
                "cfw": ["Atmosphere"],
                "homebrew": ["dbi", "hb-appstore"],
                "payload": ["hekate", "Atmosphere"],
                "sysmodule": ["ns-sys-patch"],
                "overlay": [],
                "misc": ["90dns", "Hekate Config", "exosphere (anti ban)"]
            },
            {
                "name": "Normal",
                "cfw": ["Atmosphere"],
                "homebrew": ["dbi", "Hekate-Toolbox", "JKSV", "NX-Activity-Log", "hb-appstore", "aio-switch_updater"],
                "payload": ["Atmosphere", "hekate", "Lockpick_RCM"],
                "sysmodule": ["ns-sys-patch", "MissionControl", "nx-ovlloader"],
                "overlay": ["Tesla-Menu", "fastCFWswitch", "QuickNTP"],
                "misc": ["90dns", "Hekate Config", "exosphere (anti ban)"]
            },
            {
                "name": "Modding",
                "cfw": ["Atmosphere"],
                "homebrew": ["dbi", "SimpleModDownloader", "SimpleModManager", "JKSV"],
                "payload": ["Atmosphere", "hekate"],
                "sysmodule": ["ns-sys-patch", "nx-ovlloader"],
                "overlay": ["Tesla-Menu", "Status-Monitor-Overlay"],
                "misc": ["90dns", "Hekate Config", "exosphere (anti ban)"]
            }
        ]