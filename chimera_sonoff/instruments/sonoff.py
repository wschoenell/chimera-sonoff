import json
import urllib.request

from chimera.core.chimeraobject import ChimeraObject
from chimera.interfaces.switch import Switch


class SONOFF(ChimeraObject, Switch):
    __config__ = {"device": "192.168.0.254",
                  "output": 1,  # Which output to switch on/off
                  "switch_timeout": None,  # Maximum number of seconds to wait for state change
                  "user": "",
                  "password": ""
                  }

    def __init__(self):
        super().__init__()
        self.states = None

    def _setstate(self, state):
        addr = f"http://{self['device']}/cm?user={self['user']}&password={self['password']}&cmnd=POWER{self['output']}%20{state}"
        with urllib.request.urlopen(addr, timeout=1) as response:
            contents = json.loads(response.read().decode())
        target_state = True if state == 1 else False
        return self._ParseIsSwitchedOn(contents) == target_state

    def switchOn(self):
        if not self.isSwitchedOn():
            if self._setstate(1):
                self.switchedOn()
                return True
            else:
                return False
        else:
            return True

    def switchOff(self):
        if self.isSwitchedOn():
            if self._setstate(0):
                self.switchedOff()
                return True
            else:
                return False
        else:
            return True

    def isSwitchedOn(self):
        addr = f"http://{self['device']}/cm?user={self['user']}&password={self['password']}&cmnd=POWER{self['output']}"
        print(addr)
        with urllib.request.urlopen(addr, timeout=1) as response:
            contents = json.loads(response.read().decode())
        return self._ParseIsSwitchedOn(contents)
        
    def _ParseIsSwitchedOn(self, contents):
        if "POWER" in contents:
            return contents["POWER"] == "ON"
        else:
            return contents[f"POWER{self['output']}"] == "ON"
