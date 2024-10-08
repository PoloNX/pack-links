from basemodule import BaseModule

class Sysmodule(BaseModule):
    def __init__(self):
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        #sysmodules
        a.append([{"username": "ndeadly","reponame": "MissionControl","assetPatterns": [".*MissionControl.*\\.zip"], "archiveDirectory": "", "archiveExtraction": "sdmc:/"}])
        a.append([{"username": "exelix11","reponame": "SysDVR","assetPatterns": ["SysDVR.zip"], "archiveDirectory": "", "archiveExtraction": "sdmc:/"}])
        a.append([{"username": "WerWolv","reponame": "nx-ovlloader","assetPatterns": [".*nx-ovlloader.*\\.zip"], "archiveDirectory": "", "archiveExtraction": "sdmc:/"}])
        a.append([{"username": "HookedBehemoth","reponame": "sys-tune","assetPatterns": [".*sys-tune.*\\.zip"], "archiveDirectory": "", "archiveExtraction": "sdmc:/"}])
        a.append([{"username": "XorTroll","reponame": "emuiibo","assetPatterns": [".*emuiibo.*\\.zip"], "archiveDirectory": "SdOut/", "archiveExtraction": "sdmc:/"}])
        #a.append([{"username": "o0Zz","reponame": "sys-con","assetPatterns": [".*sys-con.*\\1.7.x.zip"], "archiveDirectory": "", "archiveExtraction": "sdmc:/"}])
        a.append([{"username": "retronx-team","reponame": "sys-clk","assetPatterns": [".*sys-clk.*\\.zip"], "archiveDirectory": "", "archiveExtraction": "sdmc:/"}])
        a.append([{"username": "bakatrouble","reponame": "sys-screenuploader","assetPatterns": [".*sys-screenuploader.*\\.zip"], "archiveDirectory": "", "archiveExtraction": "sdmc:/"}])
        a.append([{"username": "pgalonza","reponame": "ns-sys-patch","assetPatterns": [".*sys-patch.*\\.zip"], "archiveDirectory": "", "archiveExtraction": "sdmc:/"}])
        
        a.sort(key=lambda x: x[0]['reponame'].lower())

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

