from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import numpy as np
import cv2
from face import face_retrun


SAVE_DIR = "./images/"

if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 画像をロード
        stream = request.files['image'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)

        # 画像データ用配列にデータがあれば
        if len(img_array) != 0:
            img = cv2.imdecode(img_array, 1)
            # グレースケール変換
            gray = face_retrun(img)
            # 画像の保存
            save_path =  "./static/test.png"
            cv2.imwrite(save_path, gray)


    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=0.0.0.0, port=5000)