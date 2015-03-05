def gather(transport, unit_list, value):
	"""
	Finds the maximum possible "value" of troops that can be loaded
	in to the remaining space of a transport.

	Input:
	 transport - The transport unit to be loaded.
	 unit_list - The list of units that can be loaded onto transport.
	   You may assume that these units are non-transport ground units
	   that are already on the same team as the transport, have not
	   moved this turn, and can reach the transport with a single move.
	 value - a function that maps a unit to some value

	Output:
	 A list of units from unit_list. Do NOT load them into the transport
	 here, just compute the list of units with maximum possible value whose
	 total size is at most the remaining capacity of the transport.

	 The calling function from gui.py will take care of loading them.

	Target Complexity:
	 It is possible to implement this method to run in time
	 O(n * C) where n is the number of units in unit_list and C
	 is the remaining capacity in the transport. Remember, the capacity
	 of a transport and the sizes of the units are all integers.
	"""
	capacity = transport.capacity
	n = len(unit_list)

	m = [[0 for x in range(capacity)] for x in range(n)]
	for j in range(capacity):
		m[0][j] = 0

	for i in range(1, n):
		for j in range(capacity):
			if unit_list[i].unit_size <= j:
				m[i][j] = max(m[i-1][j], m[i-1][j-unit_list[i].unit_size] + value(unit_list[i]))
			else:
				m[i][j] = m[i-1][j]

	gathered = []

	i = n - 1
	k = capacity - 1
	while i + k > 0:
		if m[i][k] != m[i-1][k]:
			gathered += [unit_list[i]]
			i -= 1
			k -= unit_list[i].unit_size
		else:
			i -= 1

	return gathered

# def memoize(f):
# 	memo = {}
# 	def memoFunc(a, b, c):
# 		if not (a, tuple(b), c) in memo:
# 			memo[(a, tuple(b), c)] = f(a, b, c)
# 		return memo[(a, tuple(b), c)]
# 	return memoFunc
#
# def gather(transport, unit_list, value):
# 	"""
# 	Finds the maximum possible "value" of troops that can be loaded
# 	in to the remaining space of a transport.
#
# 	Input:
# 	 transport - The transport unit to be loaded.
# 	 unit_list - The list of units that can be loaded onto transport.
# 	   You may assume that these units are non-transport ground units
# 	   that are already on the same team as the transport, have not
# 	   moved this turn, and can reach the transport with a single move.
# 	 value - a function that maps a unit to some value
#
# 	Output:
# 	 A list of units from unit_list. Do NOT load them into the transport
# 	 here, just compute the list of units with maximum possible value whose
# 	 total size is at most the remaining capacity of the transport.
#
# 	 The calling function from gui.py will take care of loading them.
#
# 	Target Complexity:
# 	 It is possible to implement this method to run in time
# 	 O(n * C) where n is the number of units in unit_list and C
# 	 is the remaining capacity in the transport. Remember, the capacity
# 	 of a transport and the sizes of the units are all integers.
# 	"""
# 	densities = []
# 	# Create a list of tuples of the unit and its value density
# 	for unit in unit_list:
# 		unitValue = value(unit)
# 		unitSize = unit.unit_size
# 		valueDensity = unitValue / unitSize
# 		densities += [(valueDensity, unit)]
# 	# Sort the density list
# 	densities.sort(key=lambda x: x[0])
# 	# Put the units in the transport
# 	remainingSpace = transport.capacity
# 	gathered = []
# 	for u in densities:
# 		if u[1].unit_size <= remainingSpace:
# 			remainingSpace -= u[1].unit_size
# 			gathered.append(u[1])
# 		else:
# 			break
# 	return gathered
#
# gather = memoize(gather)

# def getValue(capacity, units, value):
# 	"""
# 	Calculates the value using the value function
# 	If the units exceed the capacity, returns -1
# 	"""
# 	totalValue = 0
# 	remain = capacity
# 	for u in units:
# 		if u.unit_size <= remain:
# 			remain -= u.unit_size
# 			totalValue += value(u)
# 		else:
# 			return -1
# 	return totalValue
#
# def _gather(transport, units, value, memo = None):
# 	"""
# 	Does gather with memo. Returns (bestValue, gatheredUnits)
# 	units is a tuple of every unit that was passed in
# 	"""
# 	#memo is a dictionary that you can use to make your solution use memoization
# 	if memo is None:
# 		memo = {}
#
# 	# Check for the case where no elements are left
# 	if len(units) == 0:
# 		return (0, ())
# 	# Check to see if the value was already calculated for this tuple of units
# 	if units in memo:
# 		return (memo[units], units)
#
# 	bestValue = getValue(transport.capacity, units, value)
# 	bestUnits = units
# 	if bestValue == -1:
# 		for i in range(len(units)):
# 			tempUnits = units[:i] + units[i+1:]
# 			(tempValue, tempUnits) = _gather(transport, tempUnits, value, memo)
# 			if tempValue > bestValue:
# 				bestValue = tempValue
# 				bestUnits = tempUnits
# 	memo[units] = bestValue
# 	return (bestValue, bestUnits)

# def gather(transport, unit_list, value):
# 	"""
# 	Finds the maximum possible "value" of troops that can be loaded
# 	in to the remaining space of a transport.
#
# 	Input:
# 	 transport - The transport unit to be loaded.
# 	 unit_list - The list of units that can be loaded onto transport.
# 	   You may assume that these units are non-transport ground units
# 	   that are already on the same team as the transport, have not
# 	   moved this turn, and can reach the transport with a single move.
# 	 value - a function that maps a unit to some value
#
# 	Output:
# 	 A list of units from unit_list. Do NOT load them into the transport
# 	 here, just compute the list of units with maximum possible value whose
# 	 total size is at most the remaining capacity of the transport.
#
# 	 The calling function from gui.py will take care of loading them.
#
# 	Target Complexity:
# 	 It is possible to implement this method to run in time
# 	 O(n * C) where n is the number of units in unit_list and C
# 	 is the remaining capacity in the transport. Remember, the capacity
# 	 of a transport and the sizes of the units are all integers.
# 	"""
# 	# Convert to tuples
# 	unit_tuple = tuple(unit_list)
# 	# Process
# 	gathered = _gather(transport, unit_tuple, value)
# 	# Convert to list
# 	gatheredList = list(gathered[1])
#
# 	t = 0
# 	for u in gatheredList:
# 		t += u.unit_size
# 	print(t)
#
# 	return gatheredList
