from basemodule import BaseModule

class Payload(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "CTCaer",
                "reponame": "hekate",
                "assetPatterns": [".*hekate.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        #overlays
        a.append([{"username": "Decscots","reponame": "Lockpick_RCM","assetPatterns": [".*Lockpick_RCM.*\\.bin"]}])
        a.append([{"username": "suchmememanyskill","reponame": "TegraExplorer","assetPatterns": [".*TegraExplorer.*\\.bin"]}])
        a.append([{"username": "Atmosphere-NX","reponame": "Atmosphere","assetPatterns": [".*fusee.*\\.bin"]}])
        for i in a:
            self.config = i
            release = self.get_latest_release(0)
            asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
            self.out[self.config[0]["reponame"]] = {"name": i[0]["reponame"] , "link": asset[0].browser_download_url, "version": release.tag_name}
