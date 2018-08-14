import json
import urllib2

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
        super(SONOFF, self).__init__()
        self.states = None

    def _setstate(self, state):
        addr = "http://%s/cm?user=%s&password=%s&cmnd=POWER%i%%20%i" % (
        self["device"], self["user"], self["password"], self["output"], state)
        contents = json.loads(urllib2.urlopen(addr, timeout=1).read())

        target_state = "ON" if state == 1 else "OFF"
        return contents["POWER%i" % self["output"]] == target_state

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
        addr = "http://%s/cm?user=%s&password=%s&cmnd=POWER%i" % (
        self["device"], self["user"], self["password"], self["output"])
        contents = json.loads(urllib2.urlopen(addr, timeout=1).read())
        return contents["POWER%i" % self["output"]] == "ON"
