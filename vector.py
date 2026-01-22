# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import collections

class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

  def __len__(self):
      """Return the dimension of the vector."""
      return len(self._coords)

  def __getitem__(self, j):
      """Return jth coordinate of vector."""
      return self._coords[j]

  def __setitem__(self, j, val):
      """Set jth coordinate of vector to given value."""
      self._coords[j] = val

  def __add__(self, other):
      """Return sum of two vectors."""
      if len(self) != len(other):
          raise ValueError('dimensions must agree')
      result = Vector(len(self))
      for j in range(len(self)):
          result[j] = self[j] + other[j]
      return result

  def __sub__(self, other):
      """Return difference of two vectors."""
      if len(self) != len(other):
          raise ValueError('dimensions must agree')
      result = Vector(len(self))
      for j in range(len(self)):
          result[j] = self[j] - other[j]
      return result

  def __neg__(self):
      """Return negation of the vector."""
      result = Vector(len(self))
      for j in range(len(self)):
          result[j] = -self[j]
      return result

  def __mul__(self, other):
      """Return dot product of two vectors or scalar multiplication."""
      if isinstance(other, Vector):
          if len(self) != len(other):
              raise ValueError('dimensions must agree')
          return sum(self[j] * other[j] for j in range(len(self)))
      elif isinstance(other, (int, float)):
          result = Vector(len(self))
          for j in range(len(self)):
              result[j] = self[j] * other
          return result
      else:
          raise TypeError('unsupported operand type for *')

  def __rmul__(self, other):
      """Return scalar multiplication with reversed operands."""
      return self * other

  def cross(self, other):
      """Return cross product of two vectors."""
      if len(self) != len(other) or len(self) != 3:
          raise ValueError('vectors must be of length 3 for cross product')
      i = self[1] * other[2] - self[2] * other[1]
      j = self[2] * other[0] - self[0] * other[2]
      k = self[0] * other[1] - self[1] * other[0]
      return Vector([i, j, k])

  def __eq__(self, other):
      """Return True if vector has the same coordinates as other."""
      return self._coords == other._coords

  def __ne__(self, other):
      """Return True if vector differs from other."""
      return not self == other

  def __str__(self):
      """Produce string representation of vector."""
      return '<' + str(self._coords)[1:-1] + '>'

  def __lt__(self, other):
      """Compare vectors based on lexicographical order."""
      if len(self) != len(other):
          raise ValueError('dimensions must agree')
      return self._coords < other._coords

  def __le__(self, other):
      """Compare vectors based on lexicographical order."""
      if len(self) != len(other):
          raise ValueError('dimensions must agree')
      return self._coords <= other._coords

def cross(self, other):
        """Return cross product of two vectors."""
        if len(self) != len(other) or len(self) != 3:
            raise ValueError('vectors must be of length 3 for cross product')
        i = self[1] * other[2] - self[2] * other[1]
        j = self[2] * other[0] - self[0] * other[2]
        k = self[0] * other[1] - self[1] * other[0]
        return Vector([i, j, k])
  
if __name__ == '__main__':
    # The following demonstrates usage of a few methods
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    total = 0
    for entry in v:
        total += entry
