import streamlit as st
from datetime import datetime

# Streamlit app title
st.title("Video Processing App")

# Dropdown options for each field
centers = ["Center A", "Center B", "Center C"]
classrooms = ["Classroom 101", "Classroom 102", "Classroom 103"]
fps_options = [str(i) for i in range(1, 31)]
quality_options = [str(i) for i in range(1, 18)]

# Creating the dropdown menus
center = st.selectbox("Select Center", centers)
classroom = st.selectbox("Select Classroom", classrooms)

# Start and end time inputs
start_time = st.text_input("Start Time (YYYY/MM/DD HH:MM:SS)", value="2024/01/01 00:00:00")
end_time = st.text_input("End Time (YYYY/MM/DD HH:MM:SS)", value="2024/01/01 01:00:00")

# Validate datetime format for start and end times
try:
    start_time = datetime.strptime(start_time, "%Y/%m/%d %H:%M:%S")
except ValueError:
    st.error("Please enter the start time in the format YYYY/MM/DD HH:MM:SS")

try:
    end_time = datetime.strptime(end_time, "%Y/%m/%d %H:%M:%S")
except ValueError:
    st.error("Please enter the end time in the format YYYY/MM/DD HH:MM:SS")

fps = st.selectbox("Frames per Second (fps)", fps_options)
quality = st.selectbox("Video Quality (1 to 17)", quality_options)

# Display the selected values
st.write("Selected Options:")
st.write(f"Center: {center}")
st.write(f"Classroom: {classroom}")
st.write(f"Start Time: {start_time}")
st.write(f"End Time: {end_time}")
st.write(f"FPS: {fps}")
st.write(f"Quality: {quality}")
