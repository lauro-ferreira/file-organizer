markdown
# File Organizer by Extension (with GUI)

This is a simple Python tool that allows you to select a folder from your computer and automatically organizes all files into subfolders based on their file type/extension (e.g. PDF, JPG, MP4).

### Features

- GUI interface using Tkinter  
- Select any folder on your computer  
- Automatically sort files into folders by extension  
- Creates folders named by file type (e.g. `.PDF`, `.JPG`, `.MP4`, etc.)  
- Handles files without extensions by placing them in a `NO_EXTENSION` folder  
- Works on Windows, Linux, and macOS  

### Technologies

- Python 3
- Tkinter
- OS module
- Shutil

### How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/lauro-ferreira/file-organizer.git

2. Run the script:

   ```bash
   python main.py
   ```

3. A window will open. Click the **"Choose Folder"** button and select the folder you want to organize.

---

### Example

**Before:**

```
MyFolder/
├── image1.jpg
├── video1.mp4
├── document1.pdf
├── notes.txt
```

**After running the script:**

```
MyFolder/
├── JPG/
│   └── image1.jpg
├── MP4/
│   └── video1.mp4
├── PDF/
│   └── document1.pdf
├── TXT/
│   └── notes.txt
```

---

### Author

**Lauro Ferreira**
GitHub: [@lauro-ferreira](https://github.com/lauro-ferreira)
