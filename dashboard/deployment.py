import streamlit as st
import awesome_streamlit as ast
import page.web


ast.core.services.other.set_logging_format()

# create the choices
PAGES = {
    "Home": page.web,
    
}


# render the pages
def main():
   
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This App Rosemann pharmaceutical company to 
        view predictions.
"""
    )

# run it
if __name__ == "__main__":
    main()