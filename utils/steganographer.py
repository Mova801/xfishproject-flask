from pathlib import Path
import numpy as np
import skimage.io


def save_image(image: np.ndarray, destination: Path = '') -> None:
    skimage.io.imsave(destination, image)


def open_image(source: Path) -> np.ndarray:
    return skimage.io.imread(source)


def get_bin_char(char: str) -> list[int]:
    """
    Returns the bits of a character.
    :param char: character to get the bits;
    :return: bits of the character as a list.
    """
    bin_char: list[int] = [int(x) for x in bin(ord(char))[2:]]
    return [0] * (7 - len(bin_char)) + bin_char


def get_bin_str(string: str) -> list[int]:
    """
    Returns the bits of a string.
    :param string: string to get the bits;
    :return: bits of the string as a list.
    """
    binary_str: list[int] = list()
    for letter in string:
        binary_str += get_bin_char(letter)
    binary_str += [0] * 7
    return binary_str


def encode(I: np.ndarray, message_to_hide: str) -> bool | np.ndarray:
    """
    Encodes the message into an image with the Least Significant Bit Image Steganography.
    :param I: image to hide the message in;
    :param message_to_hide: message to hide;
    :return: image with hidden message;
    """
    # get binary string
    binary_msg: list[int] = get_bin_str(message_to_hide)
    binary_msg += [0] * 7
    binary_msg: np.ndarray = np.array(binary_msg, dtype=np.uint8)
    # get rounded image
    IRound: np.ndarray = I - I % 2
    IRound = IRound.flatten()
    # add hidden bits
    IRound[0:binary_msg.size] += binary_msg
    return np.reshape(IRound, I.shape)


def decode(IEnc: np.ndarray) -> str:
    """
    Decodes a message from an image with the Least Significant Bit Image Steganography.
    :param IEnc: image with hidden the message;
    :return: hidden message;
    """
    places = np.array([2 ** (6 - i) for i in range(7)])
    reading: bool = True
    message: str = ''
    IDec = IEnc.flatten()
    index: int = 0
    while reading:
        data: np.ndarray = IDec[index:index + 7] % 2
        char_ascii_code: np.array = np.sum(places * data)
        if char_ascii_code == 0:
            reading = False
        else:
            message += chr(int(char_ascii_code))
        index += 7
    return message
