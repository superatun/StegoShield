import os
import shutil
import tempfile

from Model.Enum.ActionEnum import ActionEnum
from cryptography.fernet import Fernet
from stegano import lsb
from pathlib import Path

class ImageConverterModel:
    def __init__(self):
        self.file_path = None
        self.temp_file = None
        self.sufix=None
        
    def encrypt_image(self, password):
        
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted_pwd = cipher.encrypt(password.encode())
        downloads_folder = Path.home() / "Downloads"
        output_path = downloads_folder / f"{Path(self.temp_file).stem}_encoded.{self.suffix}"
        try:
            lsb.hide(self.temp_file,message=encrypted_pwd.decode()).save(output_path)
            return key
        except:
            return None
            
    def decrypt_image(self, image_path, key):
        try:
            cipher = Fernet(key)
            secret = lsb.reveal(image_path)
            if secret is None:
                return None
            
            decrypted_pwd = cipher.decrypt(secret.encode()).decode()
            return decrypted_pwd 
        except:
            return None
            
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