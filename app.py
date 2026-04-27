print("Welcome to Trip Budget Planner 🌴")

budget = int(input("Enter your budget: "))

if budget < 5000:
    print("\nLow Budget Plan 💸")
    print("Travel: Bus - ₹800")
    print("Stay: Hostel - ₹1000")
    print("Food: ₹600")
    print("Places: Gokarna Beach, Om Beach")

elif budget < 10000:
    print("\nMedium Budget Plan 💰")
    print("Travel: Train - ₹1500")
    print("Stay: Hotel - ₹3000")
    print("Food: ₹1200")
    print("Places: Gokarna + Hidden Beaches")

else:
    print("\nPremium Plan 💎")
    print("Travel: Flight/AC Train - ₹4000")
    print("Stay: Resort - ₹6000")
    print("Food: ₹2500")
    print("Places: Gokarna + Goa")
