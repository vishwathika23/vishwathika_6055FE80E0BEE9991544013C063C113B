def leap(year):
  if((year % 400 == 0) or
     (year % 100 != 0) and
     (year % 4 == 0)):
    print("Given year is a leap year.");
  else:
    print("Guven year is not leap year.");
year = int(input("Enter the number: "))
leap(year)