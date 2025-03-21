import json
with open("lab 4/json/sample-data.json", 'r') as file:

    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':10} {'MTU':5}")
print("-" * 50, "-" * 20, "-" * 10, "-" * 5)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    
    dn = attributes.get("dn", "").strip()
    description = attributes.get("description", "").strip()
    speed = attributes.get("speed", "inherit").strip()
    mtu = attributes.get("mtu", "9150").strip()
    
    dn = dn[:50]
    description = description[:20]
    speed = speed[:10]
    mtu = mtu[:5]
    
    print(f"{dn:50} {description:20} {speed:10} {mtu:5}")
