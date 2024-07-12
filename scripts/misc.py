from basemodule import BaseModule

class Misc(BaseModule):
    def __init__(self):
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        #overlays
        a.append([{"username": "XorTroll","reponame": "uLaunch","assetPatterns": [".*uLaunch.*\\.zip"], "archiveDirectory": "SdOut/", "archiveExtraction": "sdmc:/"}])
        
        for i in a:
            self.config = i
            release = self.get_latest_release(0)
            if "assetPatterns" in self.config[0] and self.config[0]["assetPatterns"]:
                asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
                description = self.get_description(0) or ""
                self.out[self.config[0]["reponame"]] = {
                    "name": i[0]["reponame"],
                    "link": asset[0].browser_download_url,
                    "description": description,
                    "version": release.tag_name,
                    "archiveDirectory": i[0]["archiveDirectory"],
                    "archiveExtraction": i[0]["archiveExtraction"]
                }
            else:
                print(f"Warning: No assetPatterns defined for repo {self.config[0]['reponame']}")

        self.out["90dns"] = {"name": "90dns", "link": "https://raw.githubusercontent.com/PoloNX/pack-links/master/download/default.txt", "version":"", "description": "You can add a custom DNS to your WiFi connection that will block all communication with Nintendo's servers","archiveDirectory":"", "archiveExtraction":"sdmc:/atmosphere/hosts/"}
        self.out["Hekate Config"] = {"name": "Hekate Config", "link": "https://raw.githubusercontent.com/PoloNX/pack-links/master/download/hekate_ipl.ini", "version":"", "description": "", "archiveDirectory":"A simple config for hekate", "archiveExtraction":"sdmc:/bootloader/"}
        self.out["exosphere"] = {"name": "exosphere (anti ban)", "link": "https://raw.githubusercontent.com/PoloNX/pack-links/master/download/exosphere.ini", "version":"", "description": "Simple config to blank prodinfo", "archiveDirectory":"", "archiveExtraction":"sdmc:/"}