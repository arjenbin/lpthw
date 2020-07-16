

def limit(n, minn, maxn):
	return max(min(maxn, n), minn)

cars = 10
space_in_a_car = 2
passenger_space = 1.5
drivers = 10
passengers = 5
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = round(cars_driven * space_in_a_car)
average_passengers_per_car = cars_driven*space_in_a_car / passengers*passenger_space
passengers_left_over = passengers - (cars_driven * space_in_a_car)

#hoeveel ruimte neemt een passagier op?
#hoeveel ruimte totaal nodig
#hoeveel plekken totaal beschikbaar?
#totaal ruimte / totaal ruimte nodig

print("There are", cars, "Cars Available.")
print("There are only", drivers, "Drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to drive today.")
print("We need to put", average_passengers_per_car, "passengers in each car.")
print("We have", passengers_left_over, "Passengers left over")