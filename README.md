# 🚗 Pixelstoplates

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.0+-green?style=for-the-badge&logo=django)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16+-orange?style=for-the-badge&logo=tensorflow)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A powerful Django-based web application for intelligent image processing and license plate recognition using AI/ML technologies.**

[🚀 Quick Start](#quick-start) • [📋 Requirements](#requirements) • [🔧 Installation](#installation) • [🐛 Troubleshooting](#troubleshooting) • [📚 Documentation](#documentation)

</div>

---

## ✨ Features

- 🔍 **Advanced Image Processing** - State-of-the-art computer vision algorithms
- 🧠 **AI-Powered Recognition** - Deep learning models for accurate plate detection
- 🌐 **Web-Based Interface** - Modern, responsive Django web application
- 📊 **Real-time Analytics** - Live processing and result visualization
- 🔒 **Secure & Scalable** - Enterprise-grade security and performance
- 📱 **Mobile Responsive** - Works seamlessly across all devices

## 🎯 Use Cases

- **Traffic Management** - Automated license plate recognition for traffic monitoring
- **Security Systems** - Access control and surveillance applications
- **Parking Solutions** - Smart parking management and billing
- **Law Enforcement** - Vehicle identification and tracking
- **Research & Development** - Computer vision and ML research platform

---

## 📋 Requirements

### 🐍 Python Version Compatibility

| Python Version | TensorFlow | Keras | Status |
|----------------|------------|-------|---------|
| **3.13** | ❌ | ❌ | Not Supported |
| **3.12** | ✅ | ✅ | **Recommended** |
| **3.11** | ✅ | ✅ | **Supported** |
| **3.10** | ✅ | ✅ | Legacy |

> ⚠️ **Important:** Python 3.13 is not yet supported by TensorFlow/Keras. Use Python 3.12 for the best experience.

### 💻 System Requirements

- **OS**: Windows 10+, macOS 10.14+, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 2GB free space
- **GPU**: Optional but recommended for faster processing

---

## 🚀 Quick Start

### 1️⃣ Install Python 3.12

```bash
# Download from official Python website
# https://www.python.org/downloads/release/python-3120/
```

### 2️⃣ Clone & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/pixelstoplates.git
cd pixelstoplates

# Create virtual environment
python3.12 -m venv venv

# Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate
# Windows (CMD):
venv\Scripts\activate.bat
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Verify Installation

```bash
# Check Python version
python --version

# Verify TensorFlow
python -c "import tensorflow as tf; print(f'🎉 TensorFlow {tf.__version__} installed successfully!')"

# Verify Django
python -c "import django; print(f'🎉 Django {django.__version__} installed successfully!')"
```

### 4️⃣ Run the Application

```bash
# Start development server
python manage.py runserver

# Open your browser and navigate to
# http://127.0.0.1:8000
```

---

## 📦 Installation (Detailed)

### Step-by-Step Guide

<details>
<summary><b>🔧 Detailed Installation Steps</b></summary>

#### 1. Download Python 3.12
- Visit [Python 3.12.0 Release Page](https://www.python.org/downloads/release/python-3120/)
- Download the appropriate installer for your OS
- **Important**: Check "Add Python 3.12 to PATH" during installation

#### 2. Verify Python Installation
```bash
python3.12 --version
# Should output: Python 3.12.x
```

#### 3. Create Project Directory
```bash
mkdir pixelstoplates
cd pixelstoplates
```

#### 4. Set Up Virtual Environment
```bash
python3.12 -m venv venv
```

#### 5. Activate Virtual Environment
```bash
# Windows PowerShell
.\venv\Scripts\Activate

# Windows Command Prompt
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

#### 6. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

</details>

---

## 🏗️ Project Structure

```
pixelstoplates/
├── 📁 .venv/                 # Virtual environment
├── 📁 static/               # Static files (CSS, JS, images)
├── 📁 templates/            # HTML templates
├── 📁 media/                # User uploaded files
├── 📁 apps/                 # Django applications
│   ├── 📁 core/            # Core functionality
│   ├── 📁 recognition/     # Plate recognition logic
│   └── 📁 api/             # API endpoints
├── 📄 requirements.txt      # Python dependencies
├── 📄 manage.py            # Django management script
├── 📄 README.md            # This file
└── 📄 .gitignore           # Git ignore rules
```

---

## 🔧 Dependencies

### 🎯 Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **Django** | 5.0+ | Web framework |
| **TensorFlow** | 2.16+ | Machine learning framework |
| **Keras** | 3.3+ | Neural networks API |
| **NumPy** | 1.26+ | Numerical computing |
| **SciPy** | 1.13+ | Scientific computing |
| **Pillow** | 10.3+ | Image processing |
| **OpenCV** | 4.8+ | Computer vision |

### 🛠️ Development Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **Rich** | 13.7+ | Terminal formatting |
| **Markdown** | 3.6+ | Documentation |
| **Werkzeug** | 3.0+ | WSGI utilities |
| **Requests** | 2.31+ | HTTP library |

---

## 🐛 Troubleshooting

### Common Issues & Solutions

<details>
<summary><b>❌ "No matching distribution found for tensorflow"</b></summary>

**Problem**: You're using Python 3.13 or an unsupported version.

**Solution**:
```bash
# Check your Python version
python --version

# If it shows 3.13, install Python 3.12
# Then create a new virtual environment
python3.12 -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

</details>

<details>
<summary><b>❌ Virtual environment not activating</b></summary>

**Problem**: Virtual environment activation fails.

**Solution**:
```bash
# Check if venv exists
ls venv/Scripts/  # Windows
ls venv/bin/      # Linux/Mac

# If not, recreate it
rm -rf venv
python3.12 -m venv venv
.\venv\Scripts\Activate
```

</details>

<details>
<summary><b>❌ Permission errors on Windows</b></summary>

**Problem**: Access denied errors during installation.

**Solution**:
1. Run PowerShell as Administrator
2. Or use Command Prompt instead
3. Check Windows Defender settings
4. Temporarily disable antivirus if needed

</details>

<details>
<summary><b>❌ Package installation fails</b></summary>

**Problem**: Dependencies fail to install.

**Solution**:
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install with verbose output
pip install -r requirements.txt -v

# Try individual packages
pip install numpy
pip install tensorflow
pip install django
```

</details>

---

## 🔄 Alternative: PyTorch Setup

If you prefer to use Python 3.13, you can replace TensorFlow with PyTorch:

```bash
# Remove TensorFlow packages
pip uninstall tensorflow tensorflow-intel keras

# Install PyTorch
pip install torch torchvision torchaudio

# Update your code to use PyTorch instead
```

---

## 🚀 Development

### Running the Application

```bash
# Start development server
python manage.py runserver

# Run with custom port
python manage.py runserver 8080

# Run with external access
python manage.py runserver 0.0.0.0:8000
```

### Database Operations

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.recognition

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Code Quality

```bash
# Format code
black .

# Check code style
flake8 .

# Run type checking
mypy .
```

---

## 📚 Documentation

- 📖 [API Documentation](docs/api.md)
- 🔧 [Configuration Guide](docs/configuration.md)
- 🎯 [Model Training](docs/training.md)
- 🚀 [Deployment Guide](docs/deployment.md)
- 🐛 [Troubleshooting](docs/troubleshooting.md)

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### How to Contribute

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/pixelstoplates.git
cd pixelstoplates

# Add upstream remote
git remote add upstream https://github.com/original-owner/pixelstoplates.git

# Create development branch
git checkout -b development

# Install development dependencies
pip install -r requirements-dev.txt
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **TensorFlow Team** - For the amazing ML framework
- **Django Community** - For the robust web framework
- **OpenCV Contributors** - For computer vision tools
- **All Contributors** - For making this project better

---

## 📞 Support

Need help? Here's how to get support:

- 📖 **Documentation**: Check our [docs](docs/) first
- 🐛 **Issues**: [Report a bug](https://github.com/yourusername/pixelstoplates/issues)
- 💬 **Discussions**: [Join the conversation](https://github.com/yourusername/pixelstoplates/discussions)
- 📧 **Email**: support@pixelstoplates.com

---

## 📊 Project Status

![GitHub stars](https://img.shields.io/github/stars/yourusername/pixelstoplates?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/pixelstoplates?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/pixelstoplates)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/pixelstoplates)
![GitHub license](https://img.shields.io/github/license/yourusername/pixelstoplates)

---

<div align="center">

**Made with ❤️ by the Pixelstoplates Team**

[⬆ Back to top](#-pixelstoplates)

</div> #   p i x e l s t o p l a t e s  
 