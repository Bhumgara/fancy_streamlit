import time

import streamlit as st


class StreamlitTimer:
    def __init__(self):
        self._start = None
        self._end = None
        self._reverse = False
        self._done = False

    def start(self, reverse=False, end=None):
        """Starts or resets the timer.

        reverse=True requires an end time to be provided either now or previously.
        """
        if reverse and end is None and self._end is None:
            raise ValueError("reverse mode requires an end time")

        self._reverse = reverse
        if end is not None:
            self._end = end

        self._start = time.time()
        self._done = False

    def is_done(self):
        self.get_time()
        return self._done

    def get_time(self):
        """Returns the current timer value.

        In normal mode this is elapsed seconds; in reverse mode this is remaining seconds.
        """
        if self._start is None:
            return "Timer Not Started"

        elapsed = int(time.time() - self._start)
        if self._reverse:
            if self._end is None:
                raise ValueError("reverse mode requires an end time")
            remaining = max(self._end - elapsed, 0)
            self._done = remaining == 0
            return remaining

        if self._end is not None:
            self._done = elapsed >= self._end
        return elapsed

    def render_ui(self, label="Stopwatch"):
        """Isolated UI fragment that ticks without reloading the whole page."""
        @st.fragment(run_every=1.0)
        def _render_loop():
            current_seconds = self.get_time()
            st.write(label, f"{current_seconds}s")
            if self.is_done():
                st.write("**Done**")

        _render_loop()
