import json


class Config:
    def __init__(self):
        with open(r"D:\Programmieren\Dc-bot\Flo.json", "r") as json_file:
            p = json.load(json_file)
            self.token = p["Token"]
            self.Serverchannel = p["Serverchannel"]
            self.Commandchannel = p["Commandchannel"]
            self.Eingansportal = p["Eingansportal"]
            self.Main = p["Main"]
            self.Bilder = p["Bilder"]
            self.Levelchannel = p["Levelchannel"]
            self.Level_up_channel = p["Level_up_channel"]
            self.Server_id = p["Server_id"]
            self.Serverteam = p["Serverteam"]
            self.Adminteam = p["Adminteam"]
            self.Verifiziert = p["Verifiziert"]
            self.Server_ip = p["Server_ip"]
            self.Password = p["Password"]
            self.Rollenvergabe = p["Rollenvergabe"]


    def get_token(self):
        return self.token

    def get_Serverchannel(self):
        return self.Serverchannel

    def get_Commandchannel(self):
        return self.Commandchannel

    def get_Eingansportal(self):
        return self.Eingansportal

    def get_Main(self):
        return self.Main

    def get_Bilder(self):
        return self.Bilder

    def get_Levelchannel(self):
        return self.Levelchannel

    def get_Level_up_channel(self):
        return self.Level_up_channel

    def get_Server_id(self):
        return self.Server_id

    def get_Serverteam(self):
        return self.Serverteam

    def get_Adminteam(self):
        return self.Adminteam

    def get_Verifiziert(self):
        return self.Verifiziert

    def get_Server_ip(self):
        return self.Server_ip

    def get_Password(self):
        return self.Password

    def get_Rollenvergabe(self):
        return self.Rollenvergabe
