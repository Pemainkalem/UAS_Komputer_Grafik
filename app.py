from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__, template_folder='uploads', static_folder='uploads')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/crop', methods=['POST'])
def crop():
    # Memperoleh data dari formulir HTML
    input_image = request.files['input_image']
    x = int(request.form['x'])
    y = int(request.form['y'])
    width = int(request.form['width'])
    height = int(request.form['height'])

    # Menyimpan gambar input ke file sementara
    input_image_path = 'uploads/input_image.jpg'
    input_image.save(input_image_path)

    # Memanggil fungsi crop_image
    output_image_path = 'uploads/output_image.jpg'
    crop_image(input_image_path, output_image_path, x, y, width, height)

    # Menghapus file sementara
    input_image.close()

    # Menampilkan hasil crop pada halaman HTML
    return render_template('result.html', output_image_path=output_image_path)


def crop_image(image_path, output_path, x, y, width, height):
    # Load gambar
    image = Image.open(image_path)

    # Crop gambar
    cropped_image = image.crop((x, y, x + width, y + height))

    # Simpan gambar hasil crop
    cropped_image.save(output_path)


if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template

# app = Flask(__name__, template_folder='uploads')


# @app.route('/')
# def home():
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run()
