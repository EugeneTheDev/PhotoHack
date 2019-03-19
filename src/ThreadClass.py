import threading
import requests as re
import queue


class RequestThread(threading.Thread):
    def __init__(self, image_url: str, template: str, emotion_name: str, container: queue.Queue):
        super(RequestThread, self).__init__()
        self.template = template
        self.container = container
        self.emotion_name = emotion_name
        self.img_url = image_url
        print(template)

    def run(self):
        result_url = re.post(url="http://api-soft.photolab.me/template_process.php", data={
            "image_url[1]": self.img_url,
            "template_name": self.template
        }).text
        print(result_url)
        self.container.put({f"{self.emotion_name}": result_url})

