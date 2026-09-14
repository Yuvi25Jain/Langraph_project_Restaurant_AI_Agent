import streamlit as st
from typing import TypedDict
from langgraph.graph import END, StateGraph

# --- Backend State ---
class State(TypedDict):
    order: str
    status: str

# --- Nodes ---
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

def unavailable(state: State) -> dict:
    order = state["order"]
    st.error(f"Sorry, {order} is not available right now.")
    return {"order": order, "status": "unavailable"}

def kitchen_busy(state: State) -> dict:
    order = state["order"]
    st.warning(f"Kitchen is busy, {order} will be delayed.")
    return {"order": order, "status": "delayed"}

def cancelled(state: State) -> dict:
    order = state["order"]
    st.error(f"Order for {order} has been cancelled.")
    return {"order": order, "status": "cancelled"}

# --- Decision Function ---
def decision(state: State) -> str:
    status = state["status"]
    order = state["order"]

    # Dish not available
    available_dishes = ["pizza", "burger", "pasta"]
    if order not in available_dishes:
        return "unavailable"

    # Simulate random failures (for demo)
    if order == "burger":
        return "kitchen_busy"
    if order == "pasta":
        return "cancelled"

    if status == "ordered":
        return "cook"
    elif status == "cooked":
        return "serve"
    else:
        return "end"

# --- Build Graph ---
builder = StateGraph(State)
builder.add_node("take_order", take_order)
builder.add_node("cook", cook)
builder.add_node("serve", serve)
builder.add_node("unavailable", unavailable)
builder.add_node("kitchen_busy", kitchen_busy)
builder.add_node("cancelled", cancelled)

builder.set_entry_point("take_order")

builder.add_conditional_edges("take_order", decision,
                              {"cook": "cook", "unavailable": "unavailable",
                               "kitchen_busy": "kitchen_busy", "cancelled": "cancelled"})
builder.add_conditional_edges("cook", decision, {"serve": "serve"})
builder.add_edge("serve", END)
builder.add_edge("unavailable", END)
builder.add_edge("kitchen_busy", END)
builder.add_edge("cancelled", END)

graph = builder.compile()

# --- Streamlit Frontend ---
st.title("🍕 Restaurant AI Agent")

order_choice = st.selectbox("Choose your order:", ["pizza", "burger", "pasta", "sushi"])  # sushi not available

if st.button("Place Order"):
    result = graph.invoke({"order": order_choice, "status": "ordered"})
    if result["status"] == "served":
        st.success(f"Final State: {result}")
    elif result["status"] == "unavailable":
        st.error(f"Final State: {result}")
    elif result["status"] == "delayed":
        st.warning(f"Final State: {result}")
    elif result["status"] == "cancelled":
        st.error(f"Final State: {result}")
