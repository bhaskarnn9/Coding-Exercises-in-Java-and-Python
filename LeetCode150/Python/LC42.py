
def get_cavities(heights, left_boundary_index, right_boundary_index):
	# 2,1,0,1,3 -> if 2 is left_boundary and 3 is right_boundary, 1, 0, 1 are the 3 cavities -> 1 + 0 + 1 = 3
	cavities = 0
	for i in range(left_boundary_index+1, right_boundary_index):
		cavities += heights[i]
	return cavities


def helper(heights, start):
	water_blocks = 0
	left_boundary = None
	left_boundary_index = None
	right_boundary = None
	right_boundary_index = None
	interim_boundary = None
	interim_boundary_index = None
	stop = False  # when false, we will start/continue recursion

	for i in range(start, len(heights)):

		if i == len(heights)-1:
			print("reached end of heights")
			stop = True
			# we are going to use interim boundary as right boundary, so the recursion should not be terminated
			if interim_boundary is not None:
				stop = False

		h = heights[i]

		# try to get the left boundary
		if h > 0 and left_boundary is None:
			left_boundary = h
			left_boundary_index = i
			continue

		# interim boundary is first non-zero boundary before we find the right boundary
		# eg: 3,0,2,1,2,1 -> Ideally we would want right boundary to be 3 or higher with some 0s in between
		# we select 3 as left boundary, zero as cavity
		# next we select 2 as interim boundary and then keep looking for 3 or higher value
		# if 3 or higher is not find we will use interim boundary as right boundary
		if left_boundary is not None and 0 < h < left_boundary and interim_boundary is None:
			interim_boundary = h
			interim_boundary_index = i
			print("selecting interim_boundary", h, "interim_boundary_index", interim_boundary_index)

		# try to get the right boundary
		if left_boundary is not None and h >= left_boundary:
			right_boundary = h
			right_boundary_index = i

		# if right boundary is found exit loop - rest of the heights will be processed recursively
		if right_boundary is not None:
			break

	# if interim boundary is found and right boundary is not found, we will use interim boundary as right boundary
	# example of this case is 3,2,1,2
	if right_boundary is None and interim_boundary is not None and stop == False:
		right_boundary = interim_boundary
		right_boundary_index = interim_boundary_index

	# if either of the boundaries is not found, we will not be able to calculate the water blocks
	# example of this case is 1, 0, 0, 0
	if left_boundary is None or right_boundary is None:
		return water_blocks

	# if boundaries have no cavities, we will not be able to calculate the water blocks
	# example of this case is 3, 2 in [1,3,2,1,2]
	if right_boundary_index == right_boundary_index + 1:
		print("left_boundary_index == right_boundary_index")
		return water_blocks

	# ideal conditions for calculating water blocks
	if left_boundary is not None and right_boundary is not None:
		cavities = get_cavities(heights, left_boundary_index, right_boundary_index)
		print("left_boundary", left_boundary, "right_boundary", right_boundary, "cavities", cavities)
		temp = (min(left_boundary, right_boundary) * ((right_boundary_index - left_boundary_index)-1)) - cavities
		water_blocks += temp
		print("temp", temp)


	# stop = false means, we haven't reached traversing the end of heights
	if not stop:
		water_blocks += helper(heights, right_boundary_index)
	# else:
	# recursion will get terminated

	return water_blocks

	
def find_trapped_water(heights):
	print("final water blocks", helper(heights, 0))

		
find_trapped_water([0,1,0,2,1,0,1,3,2,1,2,1])
find_trapped_water([4, 2, 0, 3, 2, 5])
