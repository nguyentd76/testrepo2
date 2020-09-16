#savings_current

low = 0
high = 1
guess = (low + high)/2
down_payment = 250000
num_guess = 0 

def savings(x):
	annual_salary = 300000
	current_savings = 0
	r = 0.04
	semi_annual_raise = 0.07
	for month in range(1,37):
		current_savings = current_savings*(1 + (r/12))
		current_savings = current_savings + (guess*annual_salary)/12
		if month % 6 == 0:
				annual_salary = annual_salary*(1 + semi_annual_raise)
	return current_savings

while abs(down_payment - savings(guess)) > 100:
	if savings(guess) < down_payment:
		low = guess
	else: 
		high = guess
	guess = (low + high)/2
	num_guess += 1
	if num_guess == 20:
		print("It is not possible to pay the down payment in three years.")
print("Best savings rate:", guess)
print("Steps in bisection search:", num_guess)

#interval = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
#for guess in interval:
	#if savings(guess) < 250000:
	#print(savings(guess))
