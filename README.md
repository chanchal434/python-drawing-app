🎨 Tkinter Whiteboard App

A simple and interactive whiteboard drawing application built using **Python Tkinter**.

---

## 🚀 Features

- ✏️ Freehand drawing using mouse
- 🎨 Color palette selection
- 📏 Brush size control (slider)
- 🧹 Clear canvas (eraser)
- 🖥️ Clean and responsive UI

---

## 🏗️ Tech Stack

- Python
- Tkinter (GUI)

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/tkinter-whiteboard-app.git
cd tkinter-whiteboard-app
````

### 2. Run the application

```bash
python main.py
```

---

## 🎮 Usage

* 🖱️ Click and drag mouse to draw
* 🎨 Select colors from palette
* 📏 Adjust brush size using slider
* 🧹 Click eraser to clear screen

---

## 📁 Project Structure

```
tkinter-whiteboard-app/
│
├── main.py
├── logo.png
├── eraser.png
├── color section.png
├── README.md
```

---

## 🔮 Future Improvements

* Save drawing as image
* Undo/Redo functionality
* Custom color picker
* Shape drawing tools

---

## 👨‍💻 Author

**Chanchal Choudhary**

---

## ⭐ Support

If you like this project, please ⭐ star the repository



## 🔥 Recommended Fix (avoid crash if images missing)

Wrap images like this:

```python
try:
    image_icon = PhotoImage(file="logo.png")
    root.iconphoto(False, image_icon)
except:
    pass
```



