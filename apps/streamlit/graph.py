import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)


# Create a grid of points
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define a complex function (for example, f(x, y) = e^(x + yi))
z = np.exp(x + 1j*y)

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(z=np.real(z), x=x, y=y)])

# Set the background color to white and text/axis color to black
fig.update_layout(
    scene=dict(
        bgcolor='white',  # Set the background color to white
        xaxis=dict(color='black'),  # Set the x-axis color to black
        yaxis=dict(color='black'),  # Set the y-axis color to black
        zaxis=dict(color='black'),  # Set the z-axis color to black
    )
)

# Customize the layout, labels, and titles as needed
fig.update_layout(
    scene=dict(
        xaxis_title='X Axis Label',
        yaxis_title='Y Axis Label',
        zaxis_title='Z Axis Label',
    ),
    title='3D surface'
)

# Render the Plotly figure using st.plotly_chart
st.plotly_chart(fig, use_container_height=True)

