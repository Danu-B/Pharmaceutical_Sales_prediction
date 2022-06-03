import streamlit as st



def write():
    """Used to write the page in the app.py file"""
    st.title('LSTM Report')

    st.write('---')
    st.markdown('## Descriptive Statistics and Visualization of the data')
    st.image("./images/01.png")
    
    st.write('---')
    st.markdown('## Autocorrelations plot')
    st.write('The correlation of the time series observations is calculated with values of the same series at previous times, this is called an autocorrelation.')
    st.image("./images/02.png")
    
    st.write('---')
    st.markdown('## Partial Autocorrelation Plot')
    st.image("./images/03.png")
    st.write(' Partial Autocorrelation Plot: is a summary of the relationship between an observation in a time series with observations at prior time steps with the relationships of intervening observations removed .')


    st.write('---')
    st.markdown('## Estimate The LSTM')
    st.write('Using Hober loss- chosen because it is quite robust or nonlinear regression models and non normal errors.')
    st.image("./images/04.png")
    
    
    st.write('---')
    st.markdown('## Forecast the lstm of the validation set and assess accuracy')
    st.image("./images/05.png")
    st.write('Validation vs Forecast series')
    
   