# **🐍 Python Automation Toolkit**

A collection of high-utility scripts designed to automate repetitive tasks and explore computer vision. This toolkit features an **AI-powered Face Unlock system** and a **Smart File Organizer**.

___

## **📂 Included Projects**

### **1. 🔐 AI Face Unlock**
+ **Location:** /AI-Face-Unlock
A security script that uses your webcam to recognize your face in real-time.

+ **Tech:** OpenCV, LBPH Face Recognition, NumPy.

+ **How it works:** It trains on a folder of your photos and detects your face live. If it recognizes you with high confidence, it displays "ACCESS GRANTED."

### **2. 📂 Smart File Organizer**
+ **Location:** /File-Organizer
A script that automatically monitors and sorts cluttered folders (like your Desktop) based on file extensions.

+ **Tech:** Python os and shutil libraries.

+ **How it works:** It moves Images, Documents, Videos, and more into neatly categorized folders automatically.

___

## 🚀 Quick Setup (Get it running!)

### **1. Clone the repository:**
```bash

git clone [https://github.com](https://github.com/Aiman-Creates/Python-Automation-Toolkit)

cd Python-Automation-Toolkit
 ```

### **2. Install the required libraries:**

(You must install these for the Face Unlock to work)
```bash
pip install opencv-python opencv-contrib-python numpy
```

### **3. 📖 How to Use**

### **🔐 Face Unlock**

+ Navigate to the `AI-Face-Unlock` folder.

+ Create a folder named `known_faces` inside it.

+ Add **5-10 clear photos** of your face.

+ **Run the script:**
```bash
python face_unlock.py
```

### **📂 File Organizer**

+ Navigate to the `File-Organizer` folder.

+ Open the script and update the **directory** path to the folder you want to clean up.

+ **Run the script:**
```bash
python organize_files.py
```

___

## **🤝 Support & Contribution**

If you find these scripts useful, please give this repository a ⭐ Star! It helps others find this project.
Developed with ❤️ by Aiman-Creates
