import numpy as np

points = np.random.randint(1,100,size=(4,2))
# points = np.array([[22,31]
#  ,[74, 42]
#  ,[ 1,  6]
#  ,[63,  3]
#  ,[75, 61]
#  ,[82,52]
#  ,[42, 72]
#  ,[57, 82]
#  ,[18, 79]
#  ,[53, 93]])

# points = np.array([[14,95]
#  ,[31,  9]
#  ,[44, 89]
#  ,[16, 35]
#  ,[14,95]])

points = np.array([[42, 72]
 ,[93, 20]
 ,[ 4, 22]
 ,[ 3, 79]])

# points = np.array([[1.0  , 0.0]
#   ,[2.0   ,1.0]
#   ,[1.0   ,3.0]
#   ,[0.0   ,1.0]
#  ,[-1.0  , 1.5]
#  ,[-2.0 , -1.0]
#   ,[0.5,  -2.0]
#   ,[1.0,   0.0]])
def volume_of_polygon(points)->float:

	#Make the polygon closed if not already
	if not np.array_equal(points[0], points[-1]):
	    points = np.vstack([points, points[0]])
	rows = np.size(points, axis=0) # get number of rows
	if(np.size(points,axis=1)!=2): 
		raise Exception
		# not square 
	area = 0.0
	# Iterating for each consecutive rows, all columns from 0 to second last element
	area = sum((np.linalg.det(points[i:i+2,:])/2 )for i in range(0,rows-1))
	return abs(area)

print(points)
print(f"{volume_of_polygon(points):15f}")