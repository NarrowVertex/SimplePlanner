# 우리 애플리케이션에 필요한 다음의 임포트를 먼저 해야 합니다.

import json
import streamlit as st
from pathlib import Path

# Streamlit Elements에서는 다음의 객체들이 필요합니다.
# 모든 사용 가능한 객체와 그 사용법은 여기에 나와 있습니다: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# 대시보드가 전체 페이지를 차지하도록 페이지 레이아웃을 변경합니다.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Streamlit Elements를 사용하여 드래그 가능하고 크기 조절 가능한 대시보드 만들기.")
    st.write("---")

    # 미디어 플레이어에 대한 URL 정의.
    media_url = st.text_input("미디어 URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

layout = [
    # 편집기 항목은 x=0, y=0 좌표에 위치하며, 12/6열을 차지하고 높이는 3입니다.
    dashboard.Item("editor", 0, 0, 6, 3),
    # 차트 항목은 x=6, y=0 좌표에 위치하며, 12/6열을 차지하고 높이는 3입니다.
    dashboard.Item("chart", 6, 0, 6, 3),
    # 미디어 항목은 x=0, y=3 좌표에 위치하며, 12/6열을 차지하고 높이는 4입니다.
    dashboard.Item("media", 0, 2, 12, 4),
]

with elements("demo"):

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        with mui.Card(key="editor"):

            mui.CardHeader(title="Editor", className="draggable")
            mui

            with mui.CardActions:

                mui.Button("변경 사항 적용", onClick=sync())

        # 두 번째 카드, Nivo Bump 차트.
        # 첫 번째 카드와 동일한 flexbox 구성을 사용하여 콘텐츠 높이를 자동으로 조정합니다.

        with mui.Card(key="chart"):

            mui.CardHeader(title="차트", className="draggable")

        with mui.Card(key="media"):
            mui.CardHeader(title="미디어 플레이어", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # 이 요소는 ReactPlayer에 의해 구동되며, YouTube 외에도 많은 플레이어를 지원합니다.
                # 여기에서 확인할 수 있습니다: https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)

