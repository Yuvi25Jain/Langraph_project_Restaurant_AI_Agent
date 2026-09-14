**# 🍕 Restaurant AI Agent**
An AI‑powered simulation of a restaurant ordering system built with LangGraph (backend workflow engine) and **Streamlit** (frontend UI).  
This project demonstrates how real‑life restaurant scenarios can be modeled as decision flows — from happy paths to unexpected failures.

---

## 🚀 Quick Start
1. Clone the repo:
   bash
   git clone https://github.com/Yuvi25Jain/Langraph_project_Restaurant_AI_Agent.git
   cd Langraph_project_Restaurant_AI_Agent

2.  Install dependencies:

bash
pip install -r requirements.txt
Run the app locally:

bash
streamlit run app.py

3. live demo : https://restaurant-ai-agent-yuvi.streamlit.app/

🏗️ Architecture Overview
LangGraph Backend

Defines the workflow: Take Order → Cook → Serve → End.

Decision nodes handle exceptions: Unavailable, Kitchen Busy, Cancelled.

Each dish flows through a unique path, simulating real restaurant logic.

Streamlit Frontend

Dropdown menu for dish selection.

Button to place order.

Real‑time status updates shown step by step.

Clear feedback with colors: ✅ success, ⚠️ warning, ❌ error.

🍽️ Dishes & Scenarios
This app tells a restaurant story during festive seasons:

Pizza → Always available, smoothly cooked and served.
Like Diwali night when everyone wants a hot cheesy slice.

Burger → Kitchen busy, order delayed.
Think of Holi celebrations — too many hungry friends, kitchen overloaded.

Pasta → Order cancelled midway.
On Valentine’s Day, pasta demand spikes, but sometimes the chef runs out of sauce.

Sushi → Not on the menu, marked unavailable.
During Christmas, customers ask for exotic dishes, but not every kitchen can serve them.

