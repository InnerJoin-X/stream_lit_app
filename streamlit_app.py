import pandas
import streamlit

my_fruit_list = pandas.read_csv(' https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streeamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avacoda','Strawberries'])

streamlit.dataframe(my_fruit_list)
