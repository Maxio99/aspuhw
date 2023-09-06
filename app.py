from flask import send_file, Flask, request
import werkzeug
from werkzeug import utils

app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB


@app.route('/', methods=["POST", "GET"])
def get_image():
    try:
        image_file = request.files['image']
        # filename = werkzeug.utils.secure_filename(image_file.filename)
        # file_path = "./uploaded/" + filename
        # print("\nReceived image File name : " + image_file.filename)
        # TODO : Process the image and color it
    except Exception:
        return "Failed"
    print("\n Image Sent : testing.png")
    return send_file(path_or_file='/uploaded/testing.png', mimetype='image/png')


if __name__ == "__main__":
    app.run()
