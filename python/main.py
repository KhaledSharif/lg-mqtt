import paho.mqtt.publish as publish
import falcon

class MuteResource:
    def on_get(self, req, resp):
        try:
            publish.single("lgtv/set/mute", "true", hostname="mosquitto")
        except Exception as e:
            resp.media = {"status": str(e)}
            resp.status = falcon.HTTP_500

        resp.media = {"status": "success"}
        resp.status = falcon.HTTP_200

class UnmuteResource:
    def on_get(self, req, resp):
        try:
            publish.single("lgtv/set/mute", "false", hostname="mosquitto")
        except Exception as e:
            resp.media = {"status": str(e)}
            resp.status = falcon.HTTP_500

        resp.media = {"status": "success"}
        resp.status = falcon.HTTP_200

api = falcon.API()
api.add_route('/tv/mute', MuteResource())
api.add_route('/tv/unmute', UnmuteResource())