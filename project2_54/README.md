# Project2

## Goal1 
Refactor Polygon class so that:
  - all the calculated properties are lazy properties.
  (i.e.) they should still be calculated properties, but they should not have to get recalculated more than once.
  (since we made our Polygon class "immutable").
  
## Goal2
Refactor Polygons (Sequence) type, into an iterable. Make sure the elements in the iterator are computed lazily.
(i.e.) You can no longer use a list as an underlying storage mechanism for your Polygons.
You'll need to implement both an iterable and an iterator.
