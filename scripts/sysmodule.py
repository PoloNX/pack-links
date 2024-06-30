from basemodule import BaseModule

class Sysmodule(BaseModule):
    def __init__(self):
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        #sysmodules
        a.append([{"username": "ndeadly","reponame": "MissionControl","assetPatterns": [".*MissionControl.*\\.zip"]}])
        a.append([{"username": "exelix11","reponame": "SysDVR","assetPatterns": ["SysDVR.zip"]}])
        a.append([{"username": "WerWolv","reponame": "nx-ovlloader","assetPatterns": [".*nx-ovlloader.*\\.zip"]}])
        for i in a:
            self.config = i
            release = self.get_latest_release(0)
            asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
            self.out[self.config[0]["reponame"]] = {"name": i[0]["reponame"] , "link": asset[0].browser_download_url, "version": release.tag_name}
