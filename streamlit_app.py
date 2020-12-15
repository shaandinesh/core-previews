import streamlit as st
from execbox import execbox
from e2e_loader import select_script, get_script

with open('requirements.txt') as requirements:
    s3_url = requirements.read().split('\n')[-2]
import re

col1, padding, col2 = st.beta_columns([3, .1, 1])

match = re.search('/pr-(\\d+)/', s3_url)
if match:
    pr_number = match.group(1)

    col2.write(f"🔭 [View PR on Github](https://github.com/streamlit/streamlit/pull/{pr_number})")
    col2.write(f"🎡 [Download wheel]({s3_url})")

with col1:
    selected_script = select_script()

if selected_script:
    script = get_script(selected_script["download_url"])
else:
    script = """
import streamlit as st
from pathlib import Path
from streamlit_player import st_player, _SUPPORTED_EVENTS

with st.sidebar:
    "## ⚙️ Parameters"

    options = {
        "events": st.multiselect("Events to listen", _SUPPORTED_EVENTS, ["onProgress"]),
        "progress_interval": st.slider("Progress refresh interval (ms)", 200, 2000, 500, 1),
        "volume": st.slider("Volume", 0.0, 1.0, 1.0, .01),
        "playing": st.checkbox("Playing", False),
        "loop": st.checkbox("Loop", False),
        "controls": st.checkbox("Controls", True),
        "muted": st.checkbox("Muted", True),
        "play_inline": st.checkbox("Play inline", False),
    }

c1, c2 = st.beta_columns(2)

with c1:
    url = st.text_input("First URL", "https://youtu.be/CmSKVW1v0xM")
    event = st_player(url, **options, key=1)
    event

with c2:
    url = st.text_input("Second URL", "https://soundcloud.com/imaginedragons/demons")
    event = st_player(url, **options, key=2)
    event

    """

st.header("Edit my source 👇")
execbox(script,
    autorun=True,
    line_numbers=True,
    height=300,
)
