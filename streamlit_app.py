import streamlit
from urllib.error import URLError
import pandas 
import snowflake.connector
import requests

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Bluberry Oatmeal')
streamlit.text(' 🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

# try:
    
#     fruit_choice = streamlit.text_input('What fruit would you like information about?')
#     if not fruit_choice:
#         streamlit.error('Please select a fruit to get information')
#     else:

def get_fruityvice_data(this_fruit_choice):
fruityvice_response = requests.get('https://fruityvice.com/api/fruit', fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
return fruityvice_normalized

streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.write('Please select a fruit to get information')
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)


# except Exception as e:
#     streamlit.write(f"An error occurred when adding the fruit: {e}")
    
streamlit.write('The user entered fruit choice', fruit_choice)

streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
try:
    my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
except Exception as e:
    streamlit.write(f"An error occurred: {e}")


my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

fruit_name = streamlit.text_input('Enter the name of the fruit:')

# Add a button to insert the fruit name into the database
if streamlit.button('Add Fruit to List'):
    try:
        insert_query = "INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST (FRUIT_NAME) VALUES (%s)"  # Replace 'column_name' with the appropriate column name
        my_cur.execute(insert_query, (fruit_name,))
        my_cnx.commit()  # Commit the transaction to save changes
        streamlit.success('Fruit added successfully!')
    except Exception as e:
        streamlit.write(f"An error occurred when adding the fruit: {e}")

try:
    my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
    my_data_rows = my_cur.fetchall()
    streamlit.text("The fruit load list contains:")
    streamlit.dataframe(my_data_rows)
except Exception as e:
    streamlit.write(f"An error occurred: {e}")

