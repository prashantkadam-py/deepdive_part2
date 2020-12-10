# deepdive_part2

# Project1
 ## Goal1
   We need to create Polygon class with following properties :

 - number of vertices n - passed to the initializer
 - circumradius R - passed to the initializer
 - number of edges
 - number of sides
 - interior angle (in degrees)
 - side length
 - apothem
 - surface area
 - perimeter
 - supports equality (==) based on number of vertices and circumradius
 - supports greater than (>) based on number of vertices

## Goal2
Implement a Polygons sequence type:

### Initializer
- number of vertices for largest polygon in the sequence
- common circumradius for all polygons

### Properties
- max efficiency polygon : returns the Polygon with the highest area : perimeter ratio

### Functionality
- Functions as a sequence type (\_\_getitem\_\_)

# ===========================
# Coding Exercise

## Iterators vs Iterables

- Iterator Implements following protocol :
    - \_\_next\_\_  : returns next item from the data collection
    - \_\_iter\_\_  : returns class instance (self)
    - Iterators exhaust.
    
- Iterable implements following protocol : 
    - \_\_iter\_\_ : returns new instance of the iterator object used to iterate over iterable.
    - Iterables are non-exhaustive.
