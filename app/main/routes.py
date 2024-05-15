import os
from pathlib import Path
import numpy as np
from flask import render_template, request, current_app, flash
from werkzeug.utils import secure_filename

from app.main import bp
from utils.string_functions import is_ascii
from utils.image_editor_functions import add_text_to_image
from utils.steganographer import decode as steganographer_decode
from utils.steganographer import open_image as steganographer_open
from utils.steganographer import encode as steganographer_encode
from utils.steganographer import save_image as steganographer_save

files = [
    [0, '..%%ram=0dv"=er?"$50'],
    [1, '..%%deadfishproject-1.0%%.stg'],
    [2, '..%%secret.bin']
]


@bp.get('/index/')
@bp.get('/')
def index() -> str:
    return render_template('index.html', files=files)


@bp.get('/xfish/')
def xfish() -> str:
    flash('Nessun username trovato.')
    return render_template('xfish.html', username='<NO_NAME>', image='images/xfp_participation_pass.png')


@bp.post('/xfish/')
def xfish_post() -> str:
    username: str = request.form.get('username', '<NO_NAME>')[: 15]
    if username == '<NO_NAME>':
        flash('Nessun username trovato.')
        return render_template('xfish.html', username=username)
    else:
        flash('Congratulazioni per aver trovato questa pagina!')
        default_img: str = 'images/xfp_participation_pass.png'
        new_img: str = f"uploads/{username.lower().replace(' ', '_')}_participation_pass.png"
        add_text_to_image(Path(current_app.static_folder + '/' + default_img), username,
                          Path(current_app.static_folder + '/' + new_img))
        img = steganographer_open(Path(current_app.static_folder + '/' + new_img))
        enc = steganographer_encode(img, 'Se hai trovato questo easter egg sei proprio un boss.')
        steganographer_save(enc, Path(current_app.static_folder + '/' + new_img))
    return render_template('xfish.html', username=username, image=new_img)


@bp.get('/steganographer/')
def steganographer() -> str:
    flash("Caricare immagine con messaggio nascosto.")
    return render_template('steganographer.html', image='')


@bp.post('/steganographer/')
def steganographer_post() -> str:
    uploaded_img = request.files['uploaded-file']
    if not uploaded_img or uploaded_img.filename.find('.png') == -1:
        flash("Caricare immagine PNG.")
        return render_template('steganographer.html', image='')
    flash("Esito analisi immagine.")

    img_filename: str = secure_filename(uploaded_img.filename)
    img_path: Path = Path(os.path.join(current_app.config['UPLOAD_FOLDER'], img_filename))
    uploaded_img.save(img_path)
    image: np.ndarray = steganographer_open(img_path)
    message: str = steganographer_decode(image)
    if not is_ascii(message) or message == '':
        message = '<NO_MSG>'

    return render_template('steganographer.html', image=img_filename, hidden_message=message)
