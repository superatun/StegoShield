# Image Password Encryption Tool

This project is a tool built using Python that encrypts a password into an image using steganography. The tool generates a unique decryption token along with a new image containing the encrypted password. The only way to retrieve the password is by using the generated token and the image. The project follows the Model-View-Controller (MVC) architectural pattern and uses `tkinter` for the graphical user interface.

## Features
- Encrypt a password and embed it into an image using steganography.
- Generate a decryption token to securely retrieve the password.
- Output a new image containing the encrypted password.
- Follows the MVC design pattern for better code organization.

## Project Structure
The project directory is organized as follows:

```
src/
├── Controller/         # Contains the business logic for the application
├── Model/              # Includes data models and encryption methods
├── View/               # Manages the user interface using tkinter
├── requirements.txt    # Python dependencies for the project
.gitignore              # Specifies intentionally untracked files to ignore
main.py                 # Main entry point of the application
README.md               # Project documentation
start.ps1               # Script to start the application (only Windows)
LICENSE                 # License
```

## Installation

### Prerequisites
- Python 3.12.0 or higher
- A Windows operating system (recommended for running the `start.ps1` script)

### Steps
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/superatun/StegoShield.git
   ```
2. Navigate to the project directory:
   ```bash
   cd StegoShield
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   ./venv/Scripts/activate
   ```
   or

   Run start.ps1 on PowerShell

4. Install the required dependencies:
   ```bash
   pip install -r src/requirements.txt
   ```

## Usage
1. To start the application, run the following command in the terminal:
   ```bash
   powershell -File start.ps1
   ```
2. Use the graphical interface to upload an image and input the password you want to encrypt.
3. The application will generate:
   - A new image with the encrypted password.
   - A decryption token to retrieve the password from the image.

## Encryption Process
The encryption process is handled by the `encrypt_image` method, which works as follows:
1. A random salt and initialization vector (IV) are generated.
2. A password-based key is derived using SHA-256 hashing.
3. AES encryption (CBC mode) is applied to the password with PKCS7 padding.
4. The salt, IV, and encrypted password are combined and embedded into the image using steganography.
5. A token is generated using the SHA-256 hash of the combined data and encoded in base64.
6. The new image with the encrypted data is saved.

## Important Notes
- The decryption process requires both the encrypted image and the token.
- The `start.ps1` script is specifically designed for Windows environments.

## Dependencies
The project uses the following libraries:
- `tkinter` - For the graphical user interface.
- `os` and `pathlib` - For file and path management.
- `hashlib` - For hashing and cryptographic functions.
- `cryptography` - For AES encryption.
- `stepic` - For embedding data into images.
- `base64` - For encoding data.

## Troubleshooting
- Ensure the `temp_file` exists before attempting encryption.
- Make sure to install all dependencies from `requirements.txt`.
- If any errors occur, verify the paths and ensure you have the correct permissions.

## License
This project is proprietary software. All rights are reserved.