from basemodule import BaseModule
import requests

class Ams_cfw(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "Atmosphere-NX",
                "reponame": "Atmosphere",
                "assetPatterns": [".*atmosphere.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        release = self.get_latest_release(0)
        asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
        self.out["Atmosphere"] = asset[0].browser_download_url
        self.out["version"] = release.tag_name

