import streamlit as st

# Streamlit app title
st.title("Video Processing App")

# Dropdown options for each field
centers = ["Center A", "Center B", "Center C"]
classrooms = ["Classroom 101", "Classroom 102", "Classroom 103"]
fps_options = ["15", "24", "30", "60"]
quality_options = ["Low", "Medium", "High"]

# Creating the dropdown menus
center = st.selectbox("Select Center", centers)
classroom = st.selectbox("Select Classroom", classrooms)
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")
fps = st.selectbox("Frames per Second (fps)", fps_options)
quality = st.selectbox("Video Quality", quality_options)

# Display the selected values
st.write("Selected Options:")
st.write(f"Center: {center}")
st.write(f"Classroom: {classroom}")
st.write(f"Start Time: {start_time}")
st.write(f"End Time: {end_time}")
st.write(f"FPS: {fps}")
st.write(f"Quality: {quality}")
