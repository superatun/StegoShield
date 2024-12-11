import os
import shutil
import tempfile

from Model.Enum.ActionEnum import ActionEnum

class ImageConverterModel:
    def __init__(self):
        self.file_path = None
        self.temp_file = None
        pass
    
    def encrypt_image(self, password):
        print(password)
        pass
    
    def process_file(self, field_path, action):
        if action == ActionEnum.SAVE:
            try:
                _, suffix = os.path.splitext(field_path)
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
                
                with open(field_path, 'rb') as src, open(temp_file.name, 'wb') as dst:
                    shutil.copyfileobj(src, dst)
                
                self.temp_file = temp_file.name
                print(self.temp_file)
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