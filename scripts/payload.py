from basemodule import BaseModule

class Payload(BaseModule):
    def __init__(self):
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        #overlays
        a.append([{"username": "CTCaer","reponame": "hekate","assetPatterns": [".*hekate.*\\.zip"]}])
        a.append([{"username": "Decscots","reponame": "Lockpick_RCM","assetPatterns": [".*Lockpick_RCM.*\\.bin"]}])
        a.append([{"username": "suchmememanyskill","reponame": "TegraExplorer","assetPatterns": [".*TegraExplorer.*\\.bin"]}])
        a.append([{"username": "Atmosphere-NX","reponame": "Atmosphere","assetPatterns": [".*fusee.*\\.bin"]}])
        
        a.sort(key=lambda x: x['reponame'].lower())
        
        for i in a:
            self.config = i
            release = self.get_latest_release(0)
            asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
            description = self.get_description(0)
            self.out[self.config[0]["reponame"]] = {"name": i[0]["reponame"] , "link": asset[0].browser_download_url, "description": description, "version": release.tag_name}

