# 🛡️ AI Secure Face Unlock

A real-time facial recognition system built with **Python** and **OpenCV**. This tool uses the **LBPH (Local Binary Patterns Histograms)** algorithm to provide a secure, local, and 100% free way to unlock your system.

---

## ✨ Features
*   **Family-Proof Accuracy:** Analyzes facial texture and geometry to differentiate between similar-looking family members.
*   **Trust Counter:** Features a built-in stability logic that requires consistent recognition before granting access.
*   **100% Free & Local:** No expensive cloud APIs (like AWS or Azure). All processing happens on your local CPU.
*   **Lightweight:** Runs smoothly on standard laptops without a dedicated GPU.

---

## 🚀 How to Setup
1.  **Install Requirements:**
    ```bash
    pip install opencv-contrib-python numpy
    ```
2.  **Add Your Face:**
    * Create a folder named `known_faces` in the same directory as the script.
    * Add 1-5 clear photos of **only your face**.
3.  **Run the Script:**
    ```bash
    python face_unlock.py
    ```
4.  **Usage:**
    * **Green Box:** Access Granted (Recognized).
    * **Red Box:** Locked (Unauthorized or unrecognized).
    * Press **'q'** to exit the camera feed.

---

## 🛠️ Technical Details
The system uses the `cv2.face.LBPHFaceRecognizer` which summarizes local facial features into a histogram. By comparing the live feed histogram to your saved photos, it calculates a **confidence distance**.
*   **Lower Confidence Score = Higher Accuracy.**
*   The threshold is currently set to `55` to ensure family members cannot trigger a false positive.
