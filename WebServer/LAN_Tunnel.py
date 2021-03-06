import json
import os
#import ngrok
import subprocess as sp

#sp.check_output(["./ngrok", "http 8800"], shell=True)

class TunnelingCatcher:
    def __init__(self):
        self._publicURL = ""

    def getGeneratedPaublicURL(self):
        return self._publicURL

    def ngrok_call(self):
        retcode=sp.call("./ngrok http 8800", shell=True)
        if retcode == 0:
            print ("success")
        else:
            print ("failure")

    def ngrok_print(self):
        os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")
        with open('tunnels.json') as data_file:
            datajson = json.load(data_file)

        msg = "ngrok URL's: \n"
        for i in datajson['tunnels']:
            msg = msg + i['public_url'] +'\n'
        self._publicURL = msg
        print (msg)

    def CatchTunnelingPRDN(self):
        #ngrok_call()
        with sp.Popen(["./ngrok", "-log=stdout" "http", "8080"], stdout=sp.PIPE) as ngrokProc:
        #ngrokProc.communicate()
            print(ngrokProc.stdout.read())
        #log.write(ngrokProc.stdout.read())
        #ngrok.client.BASE_URL = "http://localhost:8800"
        #print("Tunnels:")
        #print(ngrok.link.get_tunnels())

    def run(self):
        # self.CatchTunnelingPRDN()
        # ngrok_call()
        self.ngrok_print()
        return self.getGeneratedPaublicURL()

    def catchTunnelingTelemetry(self):
        tunneling = TunnelingCatcher()
        return tunneling.run()
'''
if __name__ == "__main__":
    tunneling = TunnelingCatcher()
    tunneling.run()
'''