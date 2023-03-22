#%%
import streamlit as st
import extract
import pandas as pd
import eda
#%% Downloading Files fromKaggle website
st.title("Cyber_Security_Anomaly_Detection")

@st.cache_data
def execute():
    with st.spinner('Please wait extracting dataset by API...'):
        files = extract.extract_data()
    st.sidebar.success('files successfully downloaded')
    return files
list_of_file = execute()

#%% Sample view of the downloaded files
df_view = st.sidebar.selectbox('choose a dataframe want to view', list_of_file)

if len(df_view) > 0:
    df_view = df_view.replace("'", "").replace("[", "").replace("]", "")
    df = pd.read_csv(f'./data/{df_view}')
    st.sidebar.dataframe(df.head(5))

#%% Performing Exploratory data analysis
#train_df = pd.read_csv(f'./data/labelled_training_data.csv')
if st.button('Exploratory Analysis Dataframe'):
    c1, c2, c3, = st.columns(3)

    with c1:
        st.header('Overview')
        st.write('Total rows', eda.total_observation(df))
        st.write('Total features', eda.total_feature(df))
        st.write("Missing Value", eda.missing(df))
        st.write('Duplicate Rows', eda.duplicate(df))
        st.write('Data Type', eda.data_type(df))

    with c2:
        st.header('Feature_view')

        def feature_show(col):
            return eda.features(df[str(col)])

        val = feature_show(st.selectbox('select one feature', df.columns))
        st.write(val)

        #column = st.selectbox('select one feature', df.columns)
        #if st.button('show'):
        #    val = feature_show(column)
        #    st.write(val)

        #for column in df.columns: # to run all the column in feature one-by-one
        #    feature_view = eda.features(df[str(column)])
        #    st.dataframe(feature_view)


