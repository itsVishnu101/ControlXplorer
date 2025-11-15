# control_simulator.py
import numpy as np
import matplotlib.pyplot as plt
import control
import streamlit as st

# Function to create transfer function
def create_system(num, den):
    return control.TransferFunction(num, den)

# Function to add PID controller
def add_pid_controller(system, Kp, Ki, Kd):
    # PID: Kp + Ki/s + Kd*s
    pid = control.TransferFunction([Kd, Kp, Ki], [1, 0])
    closed_loop = control.feedback(pid * system, 1)
    return closed_loop

# Plot Step Response
def plot_step_response(system, title="Step Response"):
    t, y = control.step_response(system)
    fig, ax = plt.subplots()
    ax.plot(t, y)
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    st.pyplot(fig)

# Plot Bode Plot
def plot_bode(system):
    mag, phase, omega = control.bode(system, dB=True, Plot=False)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6,6))
    ax1.semilogx(omega, 20 * np.log10(mag))
    ax1.set_title("Bode Plot - Magnitude")
    ax1.set_ylabel("Magnitude (dB)")
    ax1.grid(True, which="both")

    ax2.semilogx(omega, phase * 180/np.pi)
    ax2.set_title("Bode Plot - Phase")
    ax2.set_xlabel("Frequency (rad/s)")
    ax2.set_ylabel("Phase (deg)")
    ax2.grid(True, which="both")
    st.pyplot(fig)

# Plot Nyquist
def plot_nyquist(system):
    fig, _ = plt.subplots()
    control.nyquist(system, Plot=True)
    plt.title("Nyquist Plot")
    st.pyplot(fig)

# Streamlit App
def main():
    st.title("⚙️ Control Systems Simulator")
    st.write("Enter transfer function and simulate responses")

    num = st.text_input("Numerator coefficients (comma-separated)", "1")
    den = st.text_input("Denominator coefficients (comma-separated)", "1,3,2")

    num = [float(x.strip()) for x in num.split(",")]
    den = [float(x.strip()) for x in den.split(",")]

    system = create_system(num, den)
    st.write("### Transfer Function:")
    st.code(str(system))

    # PID parameters
    Kp = st.number_input("Kp (Proportional Gain)", 0.0)
    Ki = st.number_input("Ki (Integral Gain)", 0.0)
    Kd = st.number_input("Kd (Derivative Gain)", 0.0)

    if Kp != 0 or Ki != 0 or Kd != 0:
        system = add_pid_controller(system, Kp, Ki, Kd)
        st.write("### With PID Controller Applied")

    if st.button("Simulate"):
        plot_step_response(system)
        plot_bode(system)
        plot_nyquist(system)

if __name__ == "__main__":
    main()
