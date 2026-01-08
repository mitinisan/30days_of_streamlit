import pandas as pd
import numpy as np
import streamlit as st
import altair as alt



st.header('st.write')

st.write('Hello *world* :sunglasses:')

st.write(917604)

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)


st.subheader('st.markdown')

st.markdown('''The text to display as GitHub-flavored Markdown.  
            Syntax information can be found at:  
            https://github.github.com/gfm.''')

st.markdown("*Streamlit* is **really** ***cool***.")
# *italic*
# **bold**
# ***italic-bold***

st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :orange-background[highlight] text.''')
# :color[text]
# :color-background[]

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# :emoji-name:
# https://share.streamlit.io/streamlit/emoji-shortcodes

st.markdown("Click the :material/search: button.")

# :material/~menu~:
# https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
    # snake case = icon_name
    # camel case = iconName
    # Pascal case = IconName

multi = '''If you end a line with two spaces,  
a soft return is used for the next line.

Two (or more) newline characters in a row
will result in a hard return.
'''
#soft return = two spaces (novo verso)
#hard return = two lines (nova estrofe)

st.markdown(multi)

# st.header
#declared method generate a explanation box of the method 

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")
#creates a text area

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)


# st.help(st.subheader)
# st.subheader
# don't even need to call st.help()



if st.button(':material/water:'):
    st.write('Why Hello there')
else:
    st.write('Goodbye')


st.header('END OF FILE')
