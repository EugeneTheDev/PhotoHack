import threading
import requests as re
import queue


class RequestThread(threading.Thread):
    def __init__(self, file, template: str, emotion_name: str, container: queue.Queue):
        """file is a werkzeug.FileStorage instance"""
        super(RequestThread, self).__init__()
        self.template = template
        self.file = file
        self.container = container
        self.emotion_name = emotion_name

    def run(self):
        img_url = re.post(url="http://upload-soft.photolab.me/upload.php?no_resize=1", files={
            "file": (self.file.filename, self.file.stream, self.file.mimetype)}).text
        print(img_url)
        result_url = re.post(url="http://api-soft.photolab.me/template_process.php", data={
            "image_url[1]": img_url,
            "template_name": self.template
        }).text
        print(result_url)
        self.container.put({f"{self.emotion_name}": result_url})

