# ⚙️ Control Systems Simulator

An interactive web-based simulator for **Control Systems Engineering**, built using **Python**, **Streamlit**, **Matplotlib**, and the **python-control** library.

This tool allows you to:

- Define custom **transfer functions**
- Apply **PID control (Kp, Ki, Kd)**
- Visualize system responses: **Step Response**, **Bode Plot**, and **Nyquist Plot**
- Interactively tune and analyze system behavior in real-time

---

## 🚀 Features

- 🎛️ Enter **numerator & denominator coefficients** to generate transfer functions  
- 🔧 Tune **PID parameters** (Kp, Ki, Kd) interactively  
- 📈 Visualize:
  - Step Response
  - Bode Plot (Magnitude + Phase)
  - Nyquist Plot
- 🖥️ Smooth, responsive UI powered by **Streamlit**

---

## 📸 Screenshots

### Input Transfer Function & PID Parameters  
![UI Example](screenshots/1.png)

### Step Response  
![Step Response](screenshots/2.png)

### Bode Plot  
![Bode Plot](screenshots/3.png)

### Nyquist Plot  
![Nyquist Plot](screenshots/4.png)

---

## 🛠️ Installation

Clone the repository:

bash
git clone https://github.com/your-username/control-systems-simulator.git
cd control-systems-simulator
▶️ Usage
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Then open:
👉 http://localhost:8501

📦 Dependencies
streamlit

matplotlib

numpy

scipy

python-control

Install them manually:

bash
Copy code
pip install streamlit matplotlib numpy scipy control
