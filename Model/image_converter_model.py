import ast
import base64
import hashlib
import os
import shutil
import tempfile

from Model.Enum.ActionEnum import ActionEnum
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
from stegano import lsb
from pathlib import Path
import zlib
import re

from Model.Enum.FileTypeEnum import FileTypeEnum
from Model.Helper.FileHelper import FileHelper

class ImageConverterModel:
    def __init__(self):
        self.file_path = None
        self.temp_file = None
        self.sufix=None
        
    def encrypt_image(self, password):
        try:
            salt = os.urandom(16)
            key = hashlib.sha256(salt).digest()
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_password = padder.update(password.encode()) + padder.finalize()
            encrypted_pwd = encryptor.update(padded_password) + encryptor.finalize()
            combined_data = salt + iv + encrypted_pwd
            token = base64.b64encode(hashlib.sha256(combined_data).digest()).decode('utf-8')
            message_base64 = base64.b64encode(combined_data).decode('utf-8')
            output_path = FileHelper.save_file(FileTypeEnum.IMG, f"{Path(self.temp_file).stem}_encoded{self.suffix}")
            if not output_path:
                raise RuntimeError("Operation cancelled by the user.")
            
            if not Path(self.temp_file).is_file():
                raise FileNotFoundError(f"Image '{self.temp_file}' does not exist.")
            lsb.hide(self.temp_file, message_base64).save(output_path)

            return token

        except:
            raise RuntimeError("Error encrypting image")

    def decrypt_image(self, image_path, token):
        try:
            message = lsb.reveal(image_path)
            if message is None:
                raise ValueError("Image did not contained any message")
            combined_data = base64.b64decode(message)
            computed_token = base64.b64encode(hashlib.sha256(combined_data).digest()).decode('utf-8')
            if computed_token != token:
                raise ValueError("Invalid token")
            salt = combined_data[:16]
            iv = combined_data[16:32]
            encrypted_pwd = combined_data[32:]
            key = hashlib.sha256(salt).digest()
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_password = decryptor.update(encrypted_pwd) + decryptor.finalize()
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            original_password = unpadder.update(padded_password) + unpadder.finalize()
            return original_password.decode()

        except:
            raise RuntimeError("Error encrypting image")
            
    def process_file(self, field_path, action):
        if action == ActionEnum.SAVE:
            try:
                _, self.suffix = os.path.splitext(field_path)
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=self.suffix)
                
                with open(field_path, 'rb') as src, open(temp_file.name, 'wb') as dst:
                    shutil.copyfileobj(src, dst)
                
                self.temp_file = temp_file.name
                return temp_file.name            
            except Exception as ex:
                print(str(ex))
                return None
            
        if action == ActionEnum.DELETE:
            try:
                if os.path.exists(field_path):
                    os.remove(field_path)
                    self.temp_file = None
            except Exception as ex:
                print(str(ex))
                raise RuntimeError("Error deleting file")