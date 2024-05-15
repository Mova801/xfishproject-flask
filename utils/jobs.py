import pathlib

UPLOAD_FOLDER: pathlib.Path = pathlib.Path('app/static/uploads')


def clear_uploads_folder() -> None:
    """
    Clear 'uploads' folder.
    :return: None
    """
    [file.unlink() for file in UPLOAD_FOLDER.iterdir() if UPLOAD_FOLDER.exists() and UPLOAD_FOLDER.is_dir()]
