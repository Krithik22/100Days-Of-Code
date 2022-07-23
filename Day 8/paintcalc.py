def paint_calc(height, width, cover):
  no_of_cans=(heighwidth)/cover
  cans=round(no_of_cans)
  print(f"You'll need {cans} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage) #calling function with keyword argument

paint_calc(test_h, test_w, coverage) #calling function with positional argument