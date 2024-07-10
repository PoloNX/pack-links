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
                "sysmodule": ["sys-patch"],
                "overlay": []
            },
            {
                "name": "Normal",
                "cfw": ["Atmosphere"],
                "homebrew": ["dbi", "Hekate-Toolbox", "JKSV", "NX-Activity-Log", "hb-appstore", "aio-switch_updater"],
                "payload": ["Atmosphere", "hekate", "Lockpick_RCM"],
                "sysmodule": ["sys-patch", "MissionControl", "nx-ovlloader"],
                "overlay": ["Tesla-Menu", "fastCFWswitch", "QuickNTP"]
            },
            {
                "name": "Modding",
                "cfw": ["Atmosphere"],
                "homebrew": ["dbi", "SimpleModDownloader", "SimpleModManager", "JKSV"],
                "payload": ["Atmosphere", "hekate"],
                "sysmodule": ["sys-patch", "nx-ovlloader"],
                "overlay": ["Tesla-Menu", "Status-Monitor-Overlay"]
            },
            {
                "name": "Advanced",
                "cfw": ["all"],
                "homebrew": ["all"],
                "payload": ["all"],
                "sysmodule": ["all"],
                "overlay": ["all"]
            },
        ]