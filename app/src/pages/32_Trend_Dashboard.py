import streamlit as st
import plotly.express as px
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Trend Dashboard")

# Fetch trend data from API - using made up API link
trends = requests.get("https://fashion-api.example.com/trends").json()

# Trend growth chart
df = pd.DataFrame(trends["categories"])
fig = px.bar(df, x="category", y="growth", color="growth")
st.plotly_chart(fig)

# Top trending items
st.subheader("Hottest Items Now")
cols = st.columns(3)
for i, item in enumerate(trends["items"][:3]):
    with cols[i]:
        st.image(item["image"], width=150)
        st.write(f"**{item['name']}**")
        st.write(f"+{item['growth']}% interest")
        if st.button("Track", key=f"track_{i}"):
            requests.post("https://fashion-api.example.com/track", json={"item_id": item["id"]})
