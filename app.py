import streamlit as st 
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import keras 

st.write(
    """
    # Jaya Jaya Institut
    """
)

x1 = st.number_input('Curricular units 2nd sem (grade)')
x2 = st.number_input('Curricular units 2nd sem (approved)')
x3 = st.number_input('Curricular units 1st sem (approved)')
x4 = st.number_input('Curricular units 1st sem (grade)')
x5 = st.selectbox(
    "Tuition fees up to date",
    (1, 0,),
)

x6 = st.number_input('Curricular units 2nd sem (evaluations)')
x7 = st.number_input('Curricular units 1st sem (evaluations)')
x8 = st.selectbox(
    'Scholarship holder',
    (1,0),
)
x9 = st.number_input('Admission grade')
x10 = st.number_input('Age at enrollment')

if st.button('predict'):
    x = np.array([x1, x2, x3, x4, x6, x7, x9, x10]).reshape(-1, 1)
    # x5, x8
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)
    


    x_append = [x[0][0], x[1][0], x[2][0], x[3][0], x5, x[4][0], x[5][0], x8, x[6][0], x[7][0]]
    input_array = np.array([x_append])
    model = keras.models.load_model('model.h5')
    y = np.argmax(model.predict(input_array))

    if y == 2:
        st.title("Graduated")
    elif y == 1:
        st.title("Enrolled")
    elif y == 0:
        st.title("Dropout")

    