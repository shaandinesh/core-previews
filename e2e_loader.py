import requests
import streamlit as st

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def get_scripts(fork="streamlit", branch="develop", headers={}):
    response = requests.get(
        f"https://api.github.com/repos/{fork}/streamlit/contents/e2e/scripts?ref={branch}",
        headers=headers
    )
    response_body = response.json()
    if response.status_code == 200:
        return response_body
    else:
        raise Error

@st.cache(suppress_st_warning=True)
def get_script(url):
    response = requests.get(url)
    e2e_script = response.text
    return e2e_script

def set_auth():
    gh_token = st.text_input("Enter your GH token", key="key")
    if gh_token:
        return {'Authorization': 'token %s' % gh_token}


def select_script(auth={}):
    try:
        scripts = get_scripts(headers=auth)
    except:
        auth_headers = set_auth()
        if auth_headers:
            scripts = get_scripts(headers=auth_headers)

    if scripts:
        return render_script_selector(scripts)

def render_script_selector(scripts):
    print("how many times")
    placeholder_option = [{ "name": "Please select a script"}]
    options = placeholder_option + scripts
    selected_script = st.selectbox(
        "Select E2E script",
        options= options,
        format_func=lambda x: x["name"]
    )
    if selected_script and "download_url" in selected_script:
        return selected_script