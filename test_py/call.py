from class_objects import point as pt

pt1 = pt(3,12,412)
pt2 = pt(6,16,987)

print(pt1.srs)
print(pt1.distance_to(pt2))
print(pt1)