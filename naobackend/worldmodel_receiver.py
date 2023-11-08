from naobackend.flightlog import Flightlog
import json

class WorldmodelReceiver:
    def __init__(self, ip):
        self.ip = ip
        self.worldmodel = None

        self.log = Flightlog(self.ip)

        self.log.subscribe_firmware_info(self.receive_worldmodel)


    #receive and pars json data
    def receive_worldmodel(self, data):
        self.worldmodel = data

    def get_worldmodel(self):
        return self.worldmodel