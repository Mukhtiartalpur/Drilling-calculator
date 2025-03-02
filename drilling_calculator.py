import streamlit as st
import math

# Set page config for background and layout
st.set_page_config(page_title="Drilling Calculator", layout="wide")

# Background styling
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: url("https://raw.githubusercontent.com/Mukhtiartalpur/Drilling-calculator/main/drilling_rig.jpg");
    background-size: cover;
}
[data-testid="stSidebar"] {
    background-color: #87CEEB;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Profile Picture URL
profile_pic_url = "https://raw.githubusercontent.com/Mukhtiartalpur/Drilling-calculator/main/mukhtiar.jpg"

# Layout: Left for content, Right for profile picture
col1, col2 = st.columns([7, 1])  # Left (content) | Right (profile)
with col2:
    st.image(profile_pic_url, width=100)
    st.markdown("<div style='text-align: center;'><b>Mukhtiar</b><br>Mehran University</div>", unsafe_allow_html=True)

# Welcome Message
st.title("🔹 Welcome to the Drilling Engineering Calculator! 🔹")
st.write("Select a category below to perform drilling-related calculations.")

# Function Definitions
def calculate_hydrostatic_pressure(mud_weight, depth):
    return round(mud_weight * 0.052 * depth, 2)

def calculate_annular_velocity(pump_output, hole_diameter, pipe_diameter):
    area_annulus = (math.pi / 4) * ((hole_diameter ** 2) - (pipe_diameter ** 2))
    velocity = (pump_output * 24.51) / area_annulus  # in ft/min
    return round(velocity, 2)

def calculate_ecd(mud_weight, pressure_loss, depth):
    return round(mud_weight + (pressure_loss / (0.052 * depth)), 2)

def calculate_kill_mud_weight(initial_mud_weight, influx_gradient, tvd, influx_height):
    return round(initial_mud_weight + (influx_gradient * influx_height / (0.052 * tvd)), 2)

def calculate_casing_burst_pressure(depth, mud_weight, safety_factor):
    return round(mud_weight * 0.052 * depth * safety_factor, 2)

# Sidebar Navigation
option = st.sidebar.radio("Choose a Calculation:", [
    "Mud Weight & Hydrostatic Pressure", "Drilling Hydraulics",
    "Well Control Calculations", "Casing & Tubing Design"], index=0)

# Mud Weight & Hydrostatic Pressure
if option == "Mud Weight & Hydrostatic Pressure":
    st.header("Mud Weight & Hydrostatic Pressure")
    mud_weight = st.number_input("Mud Weight (ppg)", min_value=5.0, max_value=20.0, format="%.2f")
    depth = st.number_input("Hole Depth (ft)", min_value=100.0, max_value=30000.0, format="%.2f")
    if st.button("Calculate Hydrostatic Pressure"):
        pressure = calculate_hydrostatic_pressure(mud_weight, depth)
        st.success(f"Hydrostatic Pressure: {pressure} psi")

# Drilling Hydraulics
elif option == "Drilling Hydraulics":
    st.header("Drilling Hydraulics")
    pump_output = st.number_input("Pump Output (gpm)", min_value=50.0, max_value=1000.0, format="%.2f")
    hole_diameter = st.number_input("Hole Diameter (in)", min_value=6.0, max_value=36.0, format="%.2f")
    pipe_diameter = st.number_input("Pipe Diameter (in)", min_value=3.0, max_value=12.0, format="%.2f")
    pressure_loss = st.number_input("Pressure Loss (psi)", min_value=50.0, max_value=5000.0, format="%.2f")
    depth = st.number_input("Depth (ft)", min_value=100.0, max_value=30000.0, format="%.2f")
    if st.button("Calculate Annular Velocity"):
        velocity = calculate_annular_velocity(pump_output, hole_diameter, pipe_diameter)
        st.success(f"Annular Velocity: {velocity} ft/min")
    if st.button("Calculate Equivalent Circulating Density (ECD)"):
        ecd = calculate_ecd(mud_weight, pressure_loss, depth)
        st.success(f"Equivalent Circulating Density: {ecd} ppg")

# Well Control Calculations
elif option == "Well Control Calculations":
    st.header("Well Control Calculations")
    initial_mud_weight = st.number_input("Initial Mud Weight (ppg)", min_value=5.0, max_value=20.0, format="%.2f")
    influx_gradient = st.number_input("Influx Gradient (ppg)", min_value=0.1, max_value=10.0, format="%.2f")
    tvd = st.number_input("True Vertical Depth (ft)", min_value=100.0, max_value=30000.0, format="%.2f")
    influx_height = st.number_input("Influx Height (ft)", min_value=1.0, max_value=500.0, format="%.2f")
    if st.button("Calculate Kill Mud Weight"):
        kill_mud_weight = calculate_kill_mud_weight(initial_mud_weight, influx_gradient, tvd, influx_height)
        st.success(f"Kill Mud Weight: {kill_mud_weight} ppg")

# Casing & Tubing Design
elif option == "Casing & Tubing Design":
    st.header("Casing & Tubing Design")
    depth = st.number_input("Casing Depth (ft)", min_value=100.0, max_value=30000.0, format="%.2f")
    mud_weight = st.number_input("Mud Weight in Casing (ppg)", min_value=5.0, max_value=20.0, format="%.2f")
    safety_factor = st.number_input("Safety Factor", min_value=1.0, max_value=2.0, format="%.2f")
    if st.button("Calculate Casing Burst Pressure"):
        burst_pressure = calculate_casing_burst_pressure(depth, mud_weight, safety_factor)
        st.success(f"Casing Burst Pressure: {burst_pressure} psi")
