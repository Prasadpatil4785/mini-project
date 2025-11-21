import json
import os

# Predefined resources with costs
TOOLS = {
    'plow': 500,
    'hoe': 200,
    'tractor': 5000
}

SEEDS = {
    'wheat': 100,
    'rice': 150,
    'maize': 120
}

FERTILIZERS = {
    'urea': 300,
    'dap': 400,
    'potash': 350
}

DATA_FILE = 'farmers.json'

def load_data():
    global farmers
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            farmers = json.load(f)
    else:
        farmers = {}

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(farmers, f, indent=4)

def farmer_registration():
    name = input("Enter farmer name: ")
    village = input("Enter village: ")
    crop_type = input("Enter crop type: ")
    land_size = float(input("Enter land size (acres): "))
    farmer_id = f"F{len(farmers) + 1:03d}"
    farmers[farmer_id] = {
        'name': name,
        'village': village,
        'crop_type': crop_type,
        'land_size': land_size,
        'resources': {'tools': [], 'seeds': [], 'fertilizers': []},
        'loan_value': 0,
        'harvests': [],
        'repayment_status': 'active',
        'failure_count': 0
    }
    print(f"Farmer registered with ID: {farmer_id}")

def resource_allocation(farmer_id):
    if farmer_id not in farmers:
        print("Farmer not found.")
        return
    farmer = farmers[farmer_id]
    if farmer['repayment_status'] != 'active':
        print("Farmer support closed.")
        return
    print("Available tools:")
    for tool, cost in TOOLS.items():
        print(f"{tool}: {cost}")
    tools = input("Enter tools (comma separated): ").split(',')
    farmer['resources']['tools'] = [t.strip() for t in tools]

    print("Available seeds:")
    for seed, cost in SEEDS.items():
        print(f"{seed}: {cost}")
    seeds = input("Enter seeds (comma separated): ").split(',')
    farmer['resources']['seeds'] = [s.strip() for s in seeds]

    print("Available fertilizers:")
    for fert, cost in FERTILIZERS.items():
        print(f"{fert}: {cost}")
    fertilizers = input("Enter fertilizers (comma separated): ").split(',')
    farmer['resources']['fertilizers'] = [f.strip() for f in fertilizers]

    loan_value = 0
    for t in farmer['resources']['tools']:
        loan_value += TOOLS.get(t, 0)
    for s in farmer['resources']['seeds']:
        loan_value += SEEDS.get(s, 0)
    for f in farmer['resources']['fertilizers']:
        loan_value += FERTILIZERS.get(f, 0)
    farmer['loan_value'] = loan_value
    print(f"Loan value: {loan_value}")

def harvest_profit(farmer_id):
    if farmer_id not in farmers:
        print("Farmer not found.")
        return
    farmer = farmers[farmer_id]
    if farmer['repayment_status'] != 'active':
        print("Farmer support closed.")
        return
    yield_q = float(input("Enter yield (quintals): "))
    price = float(input("Enter selling price per quintal: "))
    profit = (yield_q * price) - farmer['loan_value']
    farmer['harvests'].append({
        'yield': yield_q,
        'price': price,
        'profit': profit
    })
    print(f"Profit/Loss: {profit}")

def repayment_waiver(farmer_id):
    if farmer_id not in farmers:
        print("Farmer not found.")
        return
    farmer = farmers[farmer_id]
    if farmer['repayment_status'] != 'active':
        print("Farmer support closed.")
        return
    if not farmer['harvests']:
        print("No harvest data.")
        return
    last_harvest = farmer['harvests'][-1]
    profit = last_harvest['profit']
    if profit > 0:
        repayment = 0.2 * profit
        farmer['loan_value'] -= repayment
        print(f"Repaid: {repayment}, Remaining loan: {farmer['loan_value']}")
        farmer['failure_count'] = 0  # reset on success
    else:
        farmer['failure_count'] += 1
        if farmer['failure_count'] >= 3:
            farmer['repayment_status'] = 'reclaimed'
            print("Resources reclaimed after 3 failures.")
        else:
            print(f"Repayment postponed. Failures: {farmer['failure_count']}")

def generate_report(farmer_id):
    if farmer_id not in farmers:
        print("Farmer not found.")
        return
    farmer = farmers[farmer_id]
    print(f"Farmer ID: {farmer_id}")
    print(f"Name: {farmer['name']}")
    print(f"Village: {farmer['village']}")
    print(f"Crop Type: {farmer['crop_type']}")
    print(f"Land Size: {farmer['land_size']} acres")
    print(f"Resources: {farmer['resources']}")
    print(f"Loan Value: {farmer['loan_value']}")
    print("Harvests:")
    for h in farmer['harvests']:
        print(f"  Yield: {h['yield']}, Price: {h['price']}, Profit: {h['profit']}")
    print(f"Repayment Status: {farmer['repayment_status']}")
    print(f"Failure Count: {farmer['failure_count']}")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Farmer Registration")
        print("2. Resource Allocation")
        print("3. Harvest & Profit")
        print("4. Repayment & Waiver")
        print("5. Generate Report")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            farmer_registration()
        elif choice == '2':
            fid = input("Enter Farmer ID: ")
            resource_allocation(fid)
        elif choice == '3':
            fid = input("Enter Farmer ID: ")
            harvest_profit(fid)
        elif choice == '4':
            fid = input("Enter Farmer ID: ")
            repayment_waiver(fid)
        elif choice == '5':
            fid = input("Enter Farmer ID: ")
            generate_report(fid)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    load_data()
    main_menu()
    save_data()
