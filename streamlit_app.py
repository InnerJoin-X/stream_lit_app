import streamlit
import requests
import pandas as pd

# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json())

streamlit.header('Fruityvice fruit advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit" + fruit_choice)

# fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# streamlit.dataframe(fruityvice_normalized)
