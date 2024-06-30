import json

import ams_cfw
import firmwares
import app
import overlay
import payload
import sysmodule
import homebrew
import tab

if __name__ == '__main__':

    json_file = "pack-links.json"
    try:
        with open(json_file, "r") as old_file:
            out = json.load(old_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        out = {}

    modules = [
        ams_cfw.Ams_cfw(),
        firmwares.Firmwares(),
        app.App(),
        homebrew.Homebrew(),
        overlay.Overlay(),
        payload.Payload(),
        sysmodule.Sysmodule(),
        tab.Tab()
    ]
    for module in modules:
        module.handle_module()
        if module.out == {}:
            print(f"Module {module.__module__} returned an empty dict.")
        out[module.__module__] = module.out

    with open(json_file, 'w') as out_file:
        json.dump(out, out_file, indent=4)
