from basemodule import BaseModule

class Homebrew(BaseModule):
    def __init__(self):
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        a.append([{"username": "rashevskyv","reponame": "dbi","assetPatterns": [".*DBI.*\\.nro"]}])
        a.append([{"username": "WerWolv","reponame": "EdiZon","assetPatterns": [".*EdiZon.*\\.nro"]}])
        a.append([{"username": "mtheall","reponame": "ftpd","assetPatterns": [".*ftpd-classic.*\\.nro"]}])
        a.append([{"username": "XorTroll","reponame": "Goldleaf","assetPatterns": [".*Goldleaf.*\\.nro"]}])
        a.append([{"username": "WerWolv","reponame": "Hekate-Toolbox","assetPatterns": [".*HekateToolbox.*\\.nro"]}])
        a.append([{"username": "J-D-K","reponame": "JKSV","assetPatterns": [".*JKSV.*\\.nro"]}])
        a.append([{"username": "tallbl0nde","reponame": "NX-Activity-Log","assetPatterns": [".*NX-Activity-Log.*\\.nro"]}])
        #a.append([{"username": "PoloNX","reponame": "Ls-News","assetPatterns": [".*Ls-News.*\\.nro"]}])
        a.append([{"username": "PoloNX","reponame": "SimpleModDownloader","assetPatterns": [".*SimpleModDownloader.*\\.nro"]}])
        a.append([{"username": "nadrino","reponame": "SimpleModManager","assetPatterns": [".*SimpleModManager.*\\.nro"]}])
        #a.append([{"username": "znxDomain","reponame": "DNS-MITM_Manager","assetPatterns": [".*DNS-MITM_Manager.*\\.zip"]}])
        a.append([{"username": "fortheusers","reponame": "hb-appstore","assetPatterns": [".*appstore.*\\.nro"]}])
        a.append([{"username": "exelix11","reponame": "SwitchThemeInjector","assetPatterns": [".*NXThemesInstaller.*\\.nro"]}])
        a.append([{"username": "suchmememanyskill","reponame": "themezer-nx","assetPatterns": [".*themezer-nx.*\\.nro"]}])
        a.append([{"username": "HamletDuFromage","reponame": "aio-switch-updater","assetPatterns": [".*aio-switch-updater.*\\.zip"]}])

        a.sort(key=lambda x: x[0]['reponame'].lower())

        for i in a:
            self.config = i
            release = self.get_latest_release(0)
            
            # Vérifier si assetPatterns est défini et non vide
            if "assetPatterns" in self.config[0] and self.config[0]["assetPatterns"]:
                asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
                description=self.get_description(0)
                self.out[self.config[0]["reponame"]] = {
                    "name": i[0]["reponame"],
                    "link": asset[0].browser_download_url,
                    "description": description,
                    "version": release.tag_name
                }
            else:
                # Gérer le cas où assetPatterns est vide ou non défini
                print(f"Warning: No assetPatterns defined for repo {self.config[0]['reponame']}")


