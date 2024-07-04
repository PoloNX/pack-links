from basemodule import BaseModule

class Overlay(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "XorTroll",
                "reponame": "Goldleaf",
                "assetPatterns": [".*Goldleaf.*\\.nro"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        #overlays
        a.append([{"username": "WerWolv","reponame": "Tesla-Menu","assetPatterns": [".*ovlmenu.*\\.zip"]}])
        a.append([{"username": "Hartie95","reponame": "fastCFWswitch","assetPatterns": [".*fastCFWswitch.*\\.zip"]}])
        a.append([{"username": "nedex","reponame": "QuickNTP","assetPatterns": [".*QuickNTP.*\\.ovl"]}])
        a.append([{"username": "masagrator","reponame": "Status-Monitor-Overlay","assetPatterns": [".*Status-Monitor.*\\.zip"]}])
        a.append([{"username": "SegFault42","reponame": "sys-ftpd-ovl","assetPatterns": [".*sys-ftpd.*\\.zip"]}])
        a.append([{"username": "HookedBehemoth","reponame": "ShareNX-Overlay","assetPatterns": [".*ovlShareNX.*\\.ovl"]}])
        for i in a:
            self.config = i
            release = self.get_latest_release(0)
            asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
            self.out[self.config[0]["reponame"]] = {"name": i[0]["reponame"] , "link": asset[0].browser_download_url, "version": release.tag_name}
