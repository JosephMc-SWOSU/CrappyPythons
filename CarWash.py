def calculate_total_price(base_price, additional_services, selected_services):
    total_price = base_price
    selected_services_output = []

    for service in selected_services:
        if service != '-':
            if service in additional_services:
                cost = additional_services[service]
                selected_services_output.append(f"{service} - ${cost}")
                total_price += cost

    return selected_services_output, total_price

def primaryfunction():
    base_price = 10
    additional_services = {
        'Tire shine': 2,
        'Wax': 3,
        'Rain repellent': 2,
        'Interior vacuum': 5
    }

    # Input the selected services
    selected_services = []
    for _ in range(2):
        service = input("Enter an additional service or '-' if none: ").strip()
        selected_services.append(service)

    # Calculate the total price
    selected_services_output, total_price = calculate_total_price(base_price, additional_services, selected_services)

    # Output the selected services and total price
    print("Regular Joe Wash")
    print(f"Base car wash - ${base_price}")
    for service_output in selected_services_output:
        print(service_output)
    print("-----")
    print(f"Total price: ${total_price}")

if __name__ == "__main__":
    primaryfunction()