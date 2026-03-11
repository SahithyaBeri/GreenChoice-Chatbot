Overview
The Sustainable Shopping Assistant is a chatbot designed to help users make environmentally responsible purchasing decisions. It provides information about eco-friendly products, offers tips to reduce waste, and guides users on recycling and repurposing everyday items. This project supports United Nations Sustainable Development Goal 12: Responsible Consumption and Production.

Features
Recommends eco-friendly product alternatives
Provides tips for reducing waste
Offers guidance on recycling different materials
Suggests ways to repurpose commonly used items
Uses AI-based semantic search to deliver relevant responses
Integrates with Relay.app for automated workflow logging
Technology Stack
Python

Sentence Transformers for vector embeddings
Pandas for data processing
CSV-based sustainability dataset
Relay.app webhook integration
Visual Studio Code and GitHub

Project Structure
sustainable-shopping-assistant/
app.py
chatbot/
    rag_chatbot.py
embeddings/
    vector_store.py
data/
    sustainable_products.csv
requirements.txt
README.md

Running the Project
Run the chatbot using:
python app.py

Example interaction:
You: “What items can be repurposed instead of thrown away?”
Related Question: How to repurpose plastic containers?
Advice: Use them for storage or plant pots.
Relay status: 400

Dataset
The chatbot uses a sustainability dataset that contains product information, environmental benefits, recycling tips, and repurposing suggestions. This allows the system to provide helpful and relevant responses to user queries.

Expected Outcome
The system demonstrates:
A working chatbot that processes sustainability data
Context-aware responses using vector embeddings
Reduced irrelevant responses through semantic search

Automated response logging using Relay.app

Author
