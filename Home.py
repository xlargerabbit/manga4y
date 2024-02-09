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

import re
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Manga4You",
        page_icon="👋",
    )

    st.write("# Welcome! 👋")

    st.sidebar.success("Select Chapter.")

    st.markdown(
        """
        Enter the name to start
    """
    )

    # Function to validate input containing only alphabetic characters
    def validate_input(input_text):
        if not re.match("^[a-zA-Z]*$", input_text):
            st.error("Input must contain only alphabetic characters.")
            return False
        elif len(input_text) > 100:
            st.error("Input must not exceed 100 characters.")
            return False
        return True

    # Input box to accept alphabetic letters with maximum length of 100 characters
    name = st.text_input("Enter name", max_chars=100)

    # Validate the input
    if name and validate_input(name):
        st.write(f"Hello, {name}!")


if __name__ == "__main__":
    run()
