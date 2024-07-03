from basemodule import BaseModule
import requests

class cfw(BaseModule):
    def __init__(self):
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        a.append([{"username":"Atmosphere-NX", "reponame":"Atmosphere","assetPatterns": [".*atmosphere.*\\.zip"]}])
        
        for i in a:
            self.config = i
            release=self.get_latest_release(0)
            asset=self.get_asset_link(release, self.config[0]["assetPatterns"][0])
            self.out[self.config[0]["reponame"]]={"name" : i[0]["reponame"], "link": asset[0].browser_download_url, "version": release.tag_name}