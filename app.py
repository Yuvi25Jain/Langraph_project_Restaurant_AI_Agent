import streamlit as st
from typing import TypedDict
from langgraph.graph import END, StateGraph

# --- Backend State ---
class State(TypedDict):
    order: str
    status: str

def take_order(state: State) -> dict:
    order = state["order"]
    st.write(f"Taking order for {order}")
    return {"order": order, "status": "ordered"}

def cook(state: State) -> dict:
    order = state["order"]
    st.write(f"Cooking {order}")
    return {"order": order, "status": "cooked"}

def serve(state: State) -> dict:
    order = state["order"]
    st.write(f"Serving {order}")
    return {"order": order, "status": "served"}

def decision(state: State) -> str:
    status = state["status"]
    if status == "ordered":
        return "cook"
    elif status == "cooked":
        return "serve"
    else:
        return "end"

builder = StateGraph(State)
builder.add_node("take_order", take_order)
builder.add_node("cook", cook)
builder.add_node("serve", serve)
builder.set_entry_point("take_order")
builder.add_conditional_edges("take_order", decision, {"cook": "cook"})
builder.add_conditional_edges("cook", decision, {"serve": "serve"})
builder.add_edge("serve", END)
graph = builder.compile()

# --- Streamlit Frontend ---
st.title("🍕 Restaurant AI Agent")
order_choice = st.selectbox("Choose your order:", ["pizza", "burger", "pasta"])
if st.button("Place Order"):
    result = graph.invoke({"order": order_choice, "status": "ordered"})
    st.success(f"Final State: {result}")
