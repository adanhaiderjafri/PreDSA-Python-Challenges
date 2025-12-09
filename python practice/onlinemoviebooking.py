try:
    total_tickets = 100
    user_ticket = int(input("How Many Tickets the user wants :"))
    if user_ticket > total_tickets:
        raise Exception("You are Demanding more Tickets!")
except ValueError:
    print("make user to input numbers(integers)")
else:
    if user_ticket <= total_tickets:
        total_tickets -=user_ticket
        print(f"The Number of Tickets that left are {total_tickets}")
finally:
    print("Thank you for using our service!")
