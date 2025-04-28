import streamlit as st
import time
import hashlib

# Initialize an empty blockchain (list)
blockchain = []

# Function to create a block
def create_block(index, data, previous_hash):
    block = {
        "index": index,
        "data": data,
        "timestamp": time.time(),
        "previous_hash": previous_hash  # Stores the hash of the previous block
    }
    return block

# Function to generate a unique hash for each block
def generate_hash(block):
    block_string = f"{block['index']}{block['data']}{block['timestamp']}{block['previous_hash']}"
    return hashlib.sha256(block_string.encode()).hexdigest()

# Function to add a new block
def add_block(data):
    previous_block = blockchain[-1]  # Get the last block in the chain
    new_index = previous_block["index"] + 1  # New block index
    new_hash = generate_hash(previous_block)  # Hash of the last block
    
    # Create a new block
    new_block = create_block(new_index, data, new_hash)
    blockchain.append(new_block)  # Add to the blockchain

# Creating the Genesis Block (First Block)
genesis_block = create_block(1, "First Ticket Booking", "0")  # Previous hash is "0" for the first block
blockchain.append(genesis_block)  # Add to the blockchain

# Add some new blocks for bus ticket bookings
add_block({
    "ticket_id": 101,
    "customer_name": "Aditya",
    "bus_route": "Route A",
    "departure_time": "2025-05-01 08:00",
    "seat_number": "A12"
})
add_block({
    "ticket_id": 102,
    "customer_name": "Arohi",
    "bus_route": "Route B",
    "departure_time": "2025-05-01 09:00",
    "seat_number": "B5"
})
add_block({
    "ticket_id": 103,
    "customer_name": "Rasha",
    "bus_route": "Route C",
    "departure_time": "2025-05-01 10:00",
    "seat_number": "C9"
})

# Streamlit user interface
st.title("Bus Ticket Booking Blockchain")

st.subheader("Genesis Block Created")
st.write(f"Index: {genesis_block['index']}")
st.write(f"Data: {genesis_block['data']}")
st.write(f"Timestamp: {genesis_block['timestamp']}")
st.write(f"Previous Hash: {genesis_block['previous_hash']}")

st.subheader("Updated Blockchain")

for block in blockchain:
    st.write(f"\n**Block Index:** {block['index']}")
    st.write(f"**Data:** {block['data']}")
    st.write(f"**Timestamp:** {block['timestamp']}")
    st.write(f"**Previous Hash:** {block['previous_hash']}")
    st.write(f"**Current Hash:** {generate_hash(block)}")  # Displaying the hash for each block

