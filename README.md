# Tones
Backend infrastructure code to handle the linux box in the tones photobooth. Pure CLI Workflow for Fast and Lightweight Image Processing

---

# 🔍 Overview
This project focuses on providing a blazing fast and lightweight image processing workflow using the command-line interface (CLI). Ideal for automating photo capturing, editing, and printing, the workflow uses gPhoto2, fswebcam, ImageMagick, and custom scripts to streamline image processing without any GUI overhead.

---

## 📋 Features
- Maximum Speed: Designed for minimal dependencies and fast execution.
- Batch Image Editing: Simulate Adobe Camera Raw (ACR) adjustments and apply color grading using LUTs.
- Customizable Templates: Easily generate photo strips and overlays with Bash/Python scripts.
- Automation Ready: Simple scripts to automate your entire workflow from photo capture to printing.
---
## 🐧 Requirements
Before starting, make sure to install the following dependencies:

- gPhoto2 or fswebcam for image capture
- ImageMagick for image editing and batch processing
- Bash/Python for scripting and automation
- Python 3.8+
- Linux-based OS (Ubuntu, Debian, Fedora, etc.)
---

## ⚡️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/project-name.git
cd project-name
```

(Recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Basic usage:

```bash
python3 main.py --help
```

Example command:

```bash
python3 main.py --input /path/to/input --output /path/to/output
```

---

## 🧪 Running Tests

To run the test suite:

```bash
pytest tests/
```

---

## 🛠 Configuration

Configuration is done via a `.env` file or command-line arguments:

```
EXAMPLE_ENV_VAR=value
```

Or pass directly:

```bash
python3 main.py --env_var value
```

---

## 💡 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## 🧾 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Library 1](https://example.com)
- [Library 2](https://example.com)

---

## 📬 Contact

For support or questions, open an issue or contact christophergayiuman@gmail.com.
