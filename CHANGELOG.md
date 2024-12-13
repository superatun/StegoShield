# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

---
## [0.2.1] - 2024-12-12
### Added
- Modifies GUI for better appareance

---

## [0.2.0] - 2024-12-12
### Added
- Implementation of semantic versioning using `bump2version` to manage project versions.

### Changed
- Adjusted project structure to include a `VERSION` and `CHANGELOG.md` file containing the current version and changes.
- Improved documentation to reflect the use of `bump2version` in the workflow.
---

## [0.1.0] - 2024-12-10
### Added
- Initial functional version of the project.
- Password encryption in images using steganography.
- Generation of unique tokens for decrypting passwords.
- Basic graphical interface using tkinter.
- Support for images in JPG and PNG formats.

---

## How to Use `bump2version`
1. **Install `bump2version`**:
   Make sure you have `bump2version` installed in your environment:
   ```bash
   pip install bump2version

2. **Semantic**
    - bump2version patch
    - bump2version minor
    - bump2version major