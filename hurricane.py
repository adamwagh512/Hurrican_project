# names of hurricanes

names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# Step 1: Met Prereqs
# ********************************************************
# Step 2: 
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
# Create an empty string to hold values.
updated_damages = []
# defining a function called update_damages which accepts one arguement of lst (couldnt use the word list).
def update_damages(lst):
#For loop for updating damages:
  for i in range(0, len(lst)):
    # if the lst item is 'Damages not recorded', append as is.
    if lst[i] == "Damages not recorded":
      updated_damages.append(damages[i])

    # if the lst item has either an 'M' or 'B' after it, this else
    # statement will strip the letter and convert it from a string into a
    # float before multiplying it by the conversion variable.
    else:
      updated_damages.append(float(lst[i].strip(lst[i][-1])) * 
      conversion[lst[i][-1]]) 

# Calling the update_damages function with the damages arguement to 
# populate the updated_damages list. 
update_damages(damages)

# Checking my work with print statement. 
# print(updated_damages)

# **************************************************
# Step 3: 
# Create an empty dictionary named hurricanes.
hurricanes = {}
# defining a function with no arguements needed
def hurricane_name():
# This for loop will iterate through the names of the hurricanes, creating
# entries in a dictionary for each hurricane that includes name, month,
# year, max sustained winds, areas affected, damage and deaths
  for i in range(0, len(names)):
      hurricanes[names[i]] = {"Name": names[i], 
      "Month": months[i], "Year": years[i],
      "Max Sustained Winds": max_sustained_winds[i], 
      "Areas Affected": areas_affected[i], "Damage": damages[i],
      "Deaths": deaths[i]}
# This line executes the function that was written above
hurricane_name()
# These print statements were only used for testing.
# print(hurricanes['Cuba I'])
# print(hurricanes)

# ************************************************
# Step 4:
# Organizing by Year
# Creating an empty dictionary to fill with our function
canes_by_year = {}
# defining our function with one arguement, the current year we are interested in
def cane_year(current_year):
  # for each entry in the year library, we are going to check if that
  # year is the same as our current year arguement. If it is we will add
  # it to our canes_by_year dictionary along with all the other info 
  # that defines that hurricane.  
  for i in range(0, len(years)):
    if years[i] == current_year:
      canes_by_year[years[i]] = {"Name": names[i],
      "Month": months[i], "Year": years[i],
      "Max Sustained Winds": max_sustained_winds[i], 
      "Areas Affected": areas_affected[i], "Damage": damages[i],
      "Deaths": deaths[i]}
      # prints out all info on hurricanes that occured during that year
      print(canes_by_year)
      # prints a line between records, makes it easier for me to read. 
      print() 
# Print statement to test
# cane_year(2005)

# *************************************************
# Step 5:
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
damaged_areas = {}
# defining a function that doesnt accept any arguements
def area_counter():
    # accessing the individual area_lists in the areas_affected list
  for area_list in areas_affected:
    # accessing the individual area in the area_list
    for area in area_list:
    # If the indiviual area is not already in the damaged_areas dictionary, it will be added to it, with a value of 1 
      if area not in damaged_areas:
        damaged_areas[area] = 1
    # if the individual area is already in the damaged_areas dictionary, 1 will be added to its value  
      else:
        damaged_areas[area] += 1
#   print(damaged_areas)
  # print()
area_counter()

# *********************************************************
# Step 6:
# Calculating Maximum Hurricane Count
# define a function that does not accept any arguements
def max_cain_count():
#sets area as an empty string and cane_count to 0. These will be used later in our function. 
  area = ''
  cane_count = 0
# compares impact_count to current cane_count, and if the impact_count is greater, than it will replace the cane_count and impact_area will become the new area  
  for impact_area, impact_count in damaged_areas.items():
    if impact_count > cane_count:
      area = impact_area
      cane_count = impact_count
# This is a print statement that is easier to read and understand for the user. 
  print( area + ' has the greatest impact count with ' + str(cane_count) + ' since 1924' )
# max_cain_count()

#************************************************************
# Step 7: 
# This step is similar to Step 6
# Defining a function that does not accept any arguements
def deadliest_cane():
# Sets cane_deaths to 0 and cane_name as an empty string to be used later in the function
  cane_deaths = 0
  cane_name = ''
# for loop that checks each entry in the deaths list and compares it to the current cane_deaths, and if it is larger deaths[i] becomes the new cane_deaths and names[i] becomes new cane_name
  for i in range(0, len(deaths)):
    if deaths[i] > cane_deaths:
      cane_deaths = deaths[i]
      cane_name = names[i]
#Printing the answer in a format that is easier to understand for the reader, with extra line break.  
  print(cane_name + ' is the deadliest Atlantic hurricane since 1924 with a death count of : ' + str(cane_deaths))
  print()
#Calling the deadliest_cane function 
# deadliest_cane()

# ***********************************************************
# Step 8: 
# Rating Hurricanes by Mortality
# The mortality_scale is used to rate the deadliness of a hurricane, to fall into a category you must have a death toll <= the number listed, but greater than the next lowest grade. 
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
# Create a directory with empty lists which we can append our hurricanes to when the function mortality_scaler runs.
mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

def mortality_scaler():
# for every hurricane on record, we will compare it to the mortality_scale and append it to the appropriate list.
  for i in range(0, len(hurricanes)):
    if deaths[i] > mortality_scale[4]:
      mortality[5].append(hurricanes[names[i]])
    elif deaths[i] > mortality_scale[3]:
      mortality[4].append(hurricanes[names[i]])  
    elif deaths[i] > mortality_scale[2]:
      mortality[3].append(hurricanes[names[i]])
    elif deaths[i] > mortality_scale[1]:
      mortality[2].append(hurricanes[names[i]])
    elif deaths[i] > mortality_scale[0]:
      mortality[1].append(hurricanes[names[i]])
    else:
      mortality[0].append(hurricanes[names[i]])
# Calling my mortality_scaler function
mortality_scaler()
# Print mortality dictionary
# print(mortality)

# ***********************************************************
# Step 9: 
# find highest damage inducing hurricane and its total cost
def costliest_canes():
  costly_cane = ''
  dollars = 0 
  for i in range(0, len(hurricanes)):
# if the damages were not recorded for the hurricane, we are going to pass over it.
    if updated_damages[i] == 'Damages not recorded':
      pass
# if the cost of hurricane[i] is greater than the current costly_cane, we replace costly_cane with name[i], and dollars with updated_damage[i]. This way we end up with only the costliest hurricane when the function is done running.
    elif updated_damages[i] > dollars:
      costly_cane = names[i]
      dollars = updated_damages[i]
# Displaying information in easier to understand format for the reader
  print('The costliest Atlantic hurricane on record was ' + costly_cane + ' which cost $' + str(dollars))
# calling the function i defined above.
# costliest_canes()
# print()

# ***********************************************************
# Step 10: 
# Rating Hurricanes by Damage
# The damage_scale is used to rate the costliness of a hurricane, to fall into a category you must have a total cost <= the number listed, but greater than the next lowest grade. 
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
# Create a directory with empty lists which we can append our hurricanes to when the function damage_assessor runs.
hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}

def damage_assessor():
  for i in range(0, len(hurricanes)):
# Once again, if the hurricane's damages were not recorded, we will pass over it. 
    if updated_damages[i] == 'Damages not recorded':
      pass
    elif updated_damages[i] > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[names[i]])
    elif updated_damages[i] > damage_scale[3]:
      hurricanes_by_damage[4].append(hurricanes[names[i]])
    elif updated_damages[i] > damage_scale[2]:
      hurricanes_by_damage[3].append(hurricanes[names[i]])
    elif updated_damages[i] > damage_scale[1]:
      hurricanes_by_damage[2].append(hurricanes[names[i]])
    elif updated_damages[i] > damage_scale[0]:
      hurricanes_by_damage[1].append(hurricanes[names[i]])
    else:
      hurricanes_by_damage[0].append(hurricanes[names[i]])  
  
damage_assessor()
print(hurricanes_by_damage)
