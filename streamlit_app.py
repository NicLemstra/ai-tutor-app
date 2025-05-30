import sys
import os

# Add the frontend folder to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))

# Run the Streamlit app
import app
