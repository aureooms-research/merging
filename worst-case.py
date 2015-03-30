
import math

def pairwise ( iterable ) :

	iterator = iter( iterable )

	curr = next( iterator )

	for item in iterator :

		yield curr , item

		curr = item

def intervals ( n , partition ) :

	yield from pairwise ( ( 0 , ) + partition + ( n , ) )

def key ( n , partition ) :

	return sum ( math.log ( j - i , 2 ) for i , j in intervals ( n , partition )  )


if __name__ == "__main__" :

	import sys , itertools

	n , = map ( int , sys.argv[1:] )

	# n - 1 positions

	positions = tuple( range( 1 , n ) )

	best = ( )
	val  = key ( n , best )

	for k in range ( 1 , n + 1 ) :

		p = k - 1 # number of positions to pick

		for partition in itertools.combinations( positions , p ) :

			candidate = key ( n , partition )

			if candidate > val or candidate == val and partition > best :

				best , val = partition , candidate

	print ( best , val )
