import numpy as np
import pandas as pd
import streamlit as st

# Title of the application
st.title('Hello From Streamlit')

# Display simple text
st.write('Some simple text')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# Display the dataframe
st.write('Here is the dataframe')
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
  np.random.randn(200, 3),
  columns=['Column A', 'Column B', 'Column C']
)
st.line_chart(chart_data)
