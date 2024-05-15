from pathlib import Path

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL.ImageFont import FreeTypeFont


def add_text_to_image(image: Path, text: str, newname: Path) -> None:
    """
    Saves a new image with the text given as input.
    :param image: image to append text to;
    :param text: text to add to the image;
    :param newname: new image name;
    :return: none.
    """
    # Open an Image
    img: Image = Image.open(image)
    # Call draw Method to add 2D graphics in an image
    I1: ImageDraw = ImageDraw.Draw(img)
    # Custom font style and font size
    font: FreeTypeFont = ImageFont.truetype('rsc/fonts/CHILLER.TTF', 90)
    tx: float = (img.width / 2) - (font.size / 2 * (len(text) / 3)) + len(text) * 1.3
    ty: float = img.height - (img.height / 6)
    # Add Text to an image
    I1.text((tx, ty), text, font=font, fill=(28, 48, 57))
    # Display edited image
    # img.show()
    # Save the edited image
    img.save(newname)
