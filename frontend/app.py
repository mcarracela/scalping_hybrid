import streamlit as st
import requests

st.title("🚀 Bot de Scalping Híbrido")
st.write("Interfaz para operar con MT5")

symbol = st.selectbox("Par", ["EURUSD", "GBPUSD", "XAUUSD"])
lot = st.number_input("Lote", min_value=0.01, value=0.1)

if st.button("🟢 Comprar"):
    response = requests.post(
        "http://localhost:5000/api/order",
        json={"symbol": symbol, "lot": lot, "type": "BUY"}
    )
    st.success(response.json()["status"])