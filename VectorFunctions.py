# Julien Dhouti
# Started: April 29, 2017
# This script is a library of functions that operate functions on vectors.

def vector_add(v1, v2):
	"""Adds two vectors together and returns the result as a list."""
	return [i + r for i, r in zip(v1, v2)]

def vector_multiply(v1, v2):
	"""Multiplies two vectors together and returns the result as a list."""
	return [i * r for i, r in zip(v1, v2)]

def vector_divide(v1, v2):
	"""Multiplies two vectors together and returns the result as a list."""
	return [i / r for i, r in zip(v1, v2)]

def vector_distance(v1, v2):
	"""Finds the difference of two difference vectors."""
	return (max(i, r) - min(i, r) for i, r in zip(v1, v2))