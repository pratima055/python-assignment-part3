file_name = "python_notes.txt"
# =============================================
# Author: Pratima Chavan (bitsom_ba_2511746 )
# READ AND WRITE BASICS
# =============================================
# PART A — Weite
# ==============================================

# -----------------------------------------------
# Step 1: Write initial content
# -----------------------------------------------
try:    
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
        file.write("Topic 2: Lists are ordered and mutable.\n")
        file.write("Topic 3: Dictionaries store key-value pairs.\n")
        file.write("Topic 4: Loops automate repetitive tasks.\n")
        file.write("Topic 5: Exception handling prevents crashes.\n")
    print("File written successfully")
except Exception as e:
    print("Error:", e)

# -----------------------------------------------
# Step 2: Append extra lines
# -----------------------------------------------

try:
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("Topic 6: Functions improve code reusability.\n")
        file.write("Topic 7: Modules help to organize code.\n")
    print("Lines append successfuly")
except Exception as e:
    print("Error in append operations:", e)


# ==============================================
# PART B — READ 
# ==============================================

# -----------------------------------------------
# Step 3: Read and Print numbered Lines 
# -----------------------------------------------

try:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    print("\n================== FILE CONTENT ==================\n")
    for i, line in enumerate(lines, start = 1):
        print(f"{i}. {line.strip()}")
except Exception as e:
    print("Error in reading file:", e)


# -----------------------------------------------
# Step 4: Keyword search (case-Insensitive)
# -----------------------------------------------

try:
    keyword = input("\nEnter keyword to search in file: ").lower()

    found = False

    print("\n================== SEARCH RESULTS ==================\n")
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if keyword in line.lower():
                print("-", line.strip())
                found = True
    if not found:
        print("No matching lines found for keyword.")
except Exception as e:
    print("Error during keyword search:", e)

import requests

# -----------------------------------------------
# Step 1 : Fetch 20 Products
# -----------------------------------------------

url = "https://dummyjson.com/products?limit=20"
response = requests.get(url)

data = response.json()
products = data["products"]

print("\nID  | Title                          | Category      | Price    | Rating")
print("----|------------------------------|---------------|----------|--------")

for p in products:
    print(f"{p['id']:<3} | {p['title']:<30} | {p['category']:<13} | ${p['price']:<8} | {p['rating']}")

# -----------------------------------------------
# Step 2 : Filter + Sort
# ----------------------------------------------- 

filtered = [p for p in products if p ["rating"] >= 4.5]
sorted_products = sorted (filtered, key=lambda x: x["price"], reverse=True)
print("\n\nFiltered( >= 4.5) and sorted by price (High to Low)\n")

print("ID  | Title                            | Price    | Rating")
print("----|----------------------------------|----------|--------")
for p in sorted_products:
    print(f"{p['id']:<3} | {p['title']:<30} | ${p['price']:<8} | {p['rating']}")

# -----------------------------------------------
# Step 3 : Category search Laptops
# -----------------------------------------------

print("\n\nLAPTOP PRODUCTS:\n")
laptop_url = "https://dummyjson.com/products/category/laptops"
lap_response = requests.get(laptop_url) 
lap_data = lap_response.json()

for item in lap_data["products"]:
    print(f"{item['title']} - $ {item['price']}")

# -----------------------------------------------
# Step 4 : Post request stimulated
# -----------------------------------------------            

post_url = "https://dummyjson.com/products/add"
payload = {
  "title": "My Custom Product",
  "price": 999,
  "category": "electronics",
  "description": "A product I created via API"
}
post_response = requests.post(post_url, json=payload)
print("\n\nPOST RESPONSE :\n ")
print(post_response.json())

# =============================================
#  Exception Handling
# =============================================

import requests

while True:
    user_input = input("\nEnter product ID (1–100) or 'quit': ")

    if user_input.lower() == "quit":
        print("Exiting...")
        break

    if not user_input.isdigit():
        print("Invalid input. Enter number 1–100.")
        continue

    product_id = int(user_input)
    if product_id < 1 or product_id > 100:
        print("Invalid range. Enter 1-100.")
        continue
    

    try:
        url = "https://dummyjson.com/products/{products_id}"
        response = requests.get (url, timeout=5)
        
        if response.status_code == 404:
            print("Product not found.")
        elif response.status_code == 200:
            product = response.json()
            print(f"Title: {product['title']}") 
            print(f"Price: {product['price']}") 
    except requests.exceptions.ConnectionError:
        print("connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Please try later.")
    except Exception as e:
        print("Unexpected error:", str(e))

import requests
from datetime import datetime

# ====================================
# LOGGING FUNCTION
# ====================================

def log_error (function_name, error_message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR in {function_name}: {error_message}\n"

    with open ("error_log.txt", "a", encoding="utf-8") as file:
        file.write(log_entry)

# ====================================
# FETCH PRODUCTS (NORMAL CASE)
# ==================================== 

def fetch_products():
    try:
        url = "https://dummyjson.com/products?limit=5"
        response = requests.get (url, timeout=5)
        if response.status_code != 200:
            log_error("fetch_products", f"HTTPError - {response.status_code}")
        else:
            print("Products fetched successfully")
    except requests.exceptions.ConnectionError:
        log_error("fetch_products", "ConnectionError — No connection could be made")
    except requests.exceptions.Timeout:
        log_error("fetch_products", "TimeoutError — Request timed out")
    except Exception as e:
        log_error("fetch_products", str(e))

# ====================================
# LOOKUP PRODUCTS (404 CASE)
# ====================================      

def lookup_product(product_id):
    try:
        url = f"https://dummyjson.com/products/{product_id}"
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            log_error("lookup_product", f"HTTPError-404 Not Found for product ID {product_id}")
        elif response.status_code != 200:
            log_error("lookup_product", f"HTTPError-{response.status_code}") 
        else:
            print("Product found:", response.json()["title"])
    except requests.exceptions.ConnectionError:
        log_error("lookup_products", "ConnectionError — No connection could be made")
    except requests.exceptions.Timeout:
        log_error("lookup_products", "TimeoutError — Request timed out")
    except Exception as e:
        log_error("lookup_product", str(e))     

# ====================================
# INTENTIONAL ERROR 1 (Connection Error)
# ====================================


def trigger_connection_error():
    try:
        url = "https://this-host-does-not-exist-xyz.com/api"
        requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError:
        log_error("fetch_products", "ConnectionError — No connection could be made")

# ====================================
# RUN TEST (TO GEBERATE LOGS)
# ====================================

fetch_products()

lookup_product(999)  # intentional 404 case

trigger_connection_error()

# ====================================
# READ AND PRINT LOG FILE
# ====================================

print("\n================== ERROR LOG FILE ==================\n")

try:
    with open ("error_log.txt","r",encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("No log file found yet.")






    




















