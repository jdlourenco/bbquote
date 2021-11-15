import streamlit as st

from bbquote.lib import get_quote

"let's get some quotes from breaking bad"


if st.button("Get quote"):
    quote = get_quote()
    st.text(quote)
