# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Submission",  
    )

    st.write("# Selamat Datang di Dashboard Proyek Analisis Data saya!")
    st.sidebar.success("Select a city above.")
    st.markdown(
        """
        Perkenalkan saya Shelwan Riaudy U. Proyek yang saya buat ini digunakan sebagai Submission Kelas Belajar Analisis Data dengan Python Dicoding.
        Pada proyek ini dataset yang digunakan adalah Dataset yang digunakan pada penelitian ini adalah Air Quality Sumber
        """
    )
    st.write(
        """
        ## Dataset Air Quality
        Dataset ini terdiri dari 11 station dengan 18 variabel.
        
        Dataset memiliki informasi kualitas udara dari 11 station dalam rentan waktu 2013 hingga 2017. Informasi kualitas udara
        pada dataset diataranya Bulan, Tahun, Hari, Jam, Data Polutan PM2.5,PM10,SO2,NO2,CO,O3,TEMP,PRES,DEWP,RAIN,wd,WSPM.

        """
    )


if __name__ == "__main__":
    run()
