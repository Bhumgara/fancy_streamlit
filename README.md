# fancy-streamlit

A lightweight Python package for adding a simple timer component to Streamlit apps.

## Features

- Start, stop, and track elapsed time
- Optional reverse countdown mode
- Simple Streamlit UI integration
- Easy to use from Python code

## Installation
Install from PyPI:

```bash
pip install fancy-streamlit
```

## Quick Start

```python
import streamlit as st
from fancy_streamlit import StreamlitTimer

st.title("Timer Example")

timer = StreamlitTimer()

if st.button("Start Timer"):
    timer.start()

if st.button("Start Reverse Countdown"):
    timer.start(reverse=True, end=10)

timer.render_ui(label="Elapsed")
```

## API

### StreamlitTimer

```python
timer = StreamlitTimer()
```

#### Methods

- `start(reverse=False, end=None)`: Start or reset the timer.
- `get_time()`: Return the current elapsed or remaining time.
- `is_done()`: Check whether a countdown has completed.
- `render_ui(label="Stopwatch")`: Render the timer in a Streamlit app.

## License

This project is licensed under the Apache Version 2.0 License. See the [LICENSE](LICENSE) file for details.

