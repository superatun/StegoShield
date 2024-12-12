# Image Encryption and Steganography

This project implements a secure way to encrypt sensitive information and hide it within an image using **AES encryption** and **Least Significant Bit (LSB) steganography**. The encrypted data is securely embedded in the image, ensuring both security and stealth.

## Features

- **AES Encryption**: Encrypts the password using the AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode.
- **Steganography**: Hides the encrypted data inside an image using the Least Significant Bit (LSB) method.
- **Secure Output**: The resulting image looks identical to the original but contains hidden encrypted information.
- **Base64 Encoding**: Converts binary data to Base64 to ensure compatibility with the steganography process.

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.8 or higher
- `cryptography`
- `steganography`
- `base64`

You can install the required dependencies using:

```bash
pip install cryptography steganography
```

## Usage

### 1. Encrypt and Hide Data in an Image

#### Process:
1. Encrypts the password using AES encryption.
2. Encodes the encrypted data in Base64.
3. Embeds the encoded data into the least significant bits of the image.
4. Saves the modified image to a new file.

### 2. Retrieve and Decrypt Data from an Image

The `decrypt_image` method retrieves the hidden data from an image and decrypts it.

#### Parameters:
- `password` (str): The password used for encryption (must match the original).

#### Example:

```python
from your_module import YourClass

decryptor = YourClass(temp_file="path/to/image_hidden.png")
decrypted_password = decryptor.decrypt_image()
print(f"Decrypted password: {decrypted_password}")
```

#### Process:
1. Extracts the hidden Base64-encoded data from the image.
2. Decodes the data back to binary.
3. Decrypts the binary data using AES and the original password.
4. Returns the original password.

## File Structure

```plaintext
project/
|-- main.py                # Main script to execute encryption and decryption
|-- helpers/
    |-- encrypt_helper.py  # Handles encryption logic
    |-- decrypt_helper.py  # Handles decryption logic
|-- resources/
    |-- example.png        # Example input image
|-- README.md              # Documentation for the project
```

## Error Handling

The methods handle the following exceptions:
- **FileNotFoundError**: Raised if the input image file does not exist.
- **RuntimeError**: Raised for general issues during encryption or decryption.

## Security Considerations

- **Encryption Key**: The encryption key is derived using a random salt and SHA-256 hashing for strong security.
- **Integrity Check**: The Base64-encoded data includes a hash to verify the integrity of the hidden message.
- **Stealth**: The modified image looks identical to the original, making the hidden data undetectable without specific tools.

## Contribution

Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

This project is for educational purposes only. Ensure you comply with legal and ethical guidelines when using steganography or encryption in real-world applications.
