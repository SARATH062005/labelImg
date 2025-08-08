
<!-- PROJECT HEADER -->
<h1 align="center">🖼️ Improved LabelImg – With Template Feature</h1>
<p align="center">
  <b>Fast • Stable • Cross-Platform • Open Source</b><br>
  ✨ Enhanced version of <a href="https://github.com/tzutalin/labelImg">LabelImg</a> with bug fixes & new features ✨
</p>

<p align="center">
  <a href="https://github.com/SARATH062005/labelImg/stargazers"><img src="https://img.shields.io/github/stars/YourUsername/YourRepo?color=yellow&style=for-the-badge"></a>
  <a href="https://github.com/SARATH062005/labelImg/network/members"><img src="https://img.shields.io/github/forks/YourUsername/YourRepo?color=lightblue&style=for-the-badge"></a>
  <a href="https://github.com/SARATH062005/labelImg/issues"><img src="https://img.shields.io/github/issues/YourUsername/YourRepo?color=orange&style=for-the-badge"></a>
  <a href="https://github.com/SARATH062005/labelImg/blob/main/LICENSE"><img src="https://img.shields.io/github/license/YourUsername/YourRepo?style=for-the-badge"></a>
</p>

---

##  Overview
This is a **custom enhanced version of LabelImg** — an open-source graphical image annotation tool — with **major bug fixes** and **full compatibility on Windows, Linux, and macOS**.  
We’ve also introduced a **Template RectBox Feature** allowing you to **apply the same bounding box to all images in a directory** for faster annotation.

---

## 📌 Credits
This project is originally based on **[LabelImg](https://github.com/tzutalin/labelImg)** by:  
- **Tzutalin** (2015–Present)  
- **Bryan Russell, Antonio Torralba, William T. Freeman** (MIT CSAIL, 2013)  

Enhanced, maintained, and improved by **Sarath Chandiran** in 2025.

---

## ✨ New Features Added
- 🆕 **Template RectBox** – Save a bounding box template and apply it to all images in the directory.  
- 🎯 **Hotkeys for Templates**  
  - **Ctrl+T** → Apply Template  
  - **Ctrl+Shift+T** → Unselect Template  
- 🛠 **Fixed all known LabelImg bugs** (stable on Windows, Linux, macOS)  
- 📦 **Better Windows Compatibility** – No more crashes or PyQt5 resource issues.  

### 📷 Example
<p align="center">
  <img src="assets/template-example1.png" alt="Template Example 1" width="60%">
  <br><br>
  <img src="assets/template-example2.png" alt="Template Example 2" width="60%">
</p>

---

## 🖥️ How to Clone This Repo
```bash
# Clone the repository
git clone https://github.com/YourUsername/YourRepo.git

# Navigate into the project folder
cd YourRepo
````

---

## 🛠 Installation

### **Linux**

```bash
sudo apt-get install pyqt5-dev-tools
sudo pip3 install -r requirements/requirements-linux-python3.txt
make qt5py3
python3 labelImg.py
python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

---

### **macOS**

```bash
# Install dependencies via Homebrew
brew install qt       # Installs qt-5.x.x
brew install libxml2

# OR using pip
pip3 install pyqt5 lxml

# Build and run
make qt5py3
python3 labelImg.py
python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

---

### **Windows**

#### Standard Python

```bash
# Open cmd and go to the LabelImg directory
pyrcc4 -o libs/resources.py resources.qrc
# For PyQt5
pyrcc5 -o libs/resources.py resources.qrc

python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

#### Using Anaconda

```bash
# Open Anaconda Prompt and go to the LabelImg directory
conda install pyqt=5
conda install -c anaconda lxml
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

---

## 🎹 Hotkeys

<div align="center">

| Key              | Action                 |
| ---------------- | ---------------------- |
| Ctrl + S         | Save                   |
| Ctrl + T         | Apply Template RectBox |
| Ctrl + Shift + T | Unselect Template      |
| W                | Create a RectBox       |
| D                | Next Image             |
| A                | Previous Image         |
| Delete           | Delete Selected Shape  |
| Ctrl + Z         | Undo                   |
| Ctrl + Shift + Z | Redo                   |
| Space            | Verify Image           |

</div>

---

## 📜 License

```
MIT License  

Copyright (c) 2025 Sarath Chandiran  
Modifications and maintenance by Sarath Chandiran  

Based on LabelImg by Tzutalin, Bryan Russell, Antonio Torralba, William T. Freeman  

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## 🤝 Contributing

We welcome contributions!

1. Fork the project 🍴
2. Create your feature branch 🌱
3. Commit your changes 💡
4. Push to your branch 🚀
5. Open a Pull Request 🎯

---

## 📬 Contact

* **Author:** Sarath Chandiran
* **Email:** [your.email@example.com](mailto:your.email@example.com)
* **GitHub:** [@YourUsername](https://github.com/YourUsername)

<p align="center">⭐ If you find this useful, please give it a star on GitHub! ⭐</p>

