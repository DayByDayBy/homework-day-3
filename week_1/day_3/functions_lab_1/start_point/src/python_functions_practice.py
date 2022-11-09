#  def test_return_10(self):
#       return_10_result = return_10()
#       self.assertEqual( 10, return_10_result )



def return_10():
    return 10

# def test_add(self):
#       add_result = add( 1, 2 )
#       self.assertEqual( 3, add_result )

def add(num_1, num_2):
    return num_1 + num_2 

# def test_subtract(self):
#     subtract_result = subtract( 10, 5 )
#     self.assertEqual( 5, subtract_result )

def subtract(num_3, num_4):
    return num_3 - num_4

# def test_multiply(self):
#       multiply_result = multiply( 4, 2 )
#       self.assertEqual( 8, multiply_result )

def multiply(num_5, num_6):
    return num_5 * num_6


# def test_divide(self):
#     divide_result = divide( 10, 2 )
#     self.assertEqual( 5, divide_result )

def divide(num_1, num_2):
    return num_1 / num_2

# def test_length_of_string(self):
#     test_string = "A string of length 21"
#     string_length = length_of_string( test_string )
#     self.assertEqual( 21, string_length )

def length_of_string(input_string):
    return len(input_string)

# def test_join_string(self):
#     string_1 = "Mary had a little lamb, "
#     string_2 = "its fleece was white as snow"
#     joined_string = join_string( string_1, string_2 )
#     self.assertEqual( "Mary had a little lamb, its fleece was white as snow", joined_string )

def join_string(string_1, string_2):
    joined_string = string_1 + string_2
    return joined_string

# def test_add_string_as_number(self):
#       add_result = add_string_as_number( "1", "2" )
#       self.assertEqual( 3, add_result )


def add_string_as_number(first_1, second_1):
    add_result = int(first_1) + int(second_1)
    return add_result
        
#  def test_number_to_full_name__month_1(self):
#       result = number_to_full_month_name( 1 )
#       self.assertEqual( "January", result )

months = {
        1 : {"shortname": "Jan", "longname" : "January"},
        2 : {"shortname": "Feb", "longname" : "February"},
        3 : {"shortname": "Mar", "longname" : "March"},
        4 : {"shortname": "Apr", "longname" : "April"},
        5 : {"shortname": "May", "longname" : "May"},
        6 : {"shortname": "Jun", "longname" : "June"},
        7 : {"shortname": "Jul", "longname" : "July"},
        8 : {"shortname": "Aug", "longname" : "August"},
        9 : {"shortname": "Sep", "longname" : "September"},
        10 : {"shortname": "Oct", "longname" : "October"},
    }

def number_to_full_month_name(month_num):
    number_to_full_name_month = months[month_num]["longname"]
    return number_to_full_name_month

# def test_number_to_full_name__month_3(self):
#       result = number_to_full_month_name( 3 )
#       self.assertEqual( "March", result )


# def test_number_to_short_month_name__month_1(self):
#       first_month_string = number_to_short_month_name( 1 )
#       self.assertEqual( "Jan", first_month_string )

def number_to_short_month_name(month_num):
    number_to_full_name_month = months[month_num]["shortname"]
    return number_to_full_name_month

# def test_number_to_short_month_name__month_4(self):
#       fourth_month_string = number_to_short_month_name( 4 )
#       self.assertEqual( "Apr", fourth_month_string )

# def test_number_to_short_month_name__month_10(self):
#       tenth_month_string = number_to_short_month_name( 10 )
#       self.assertEqual( "Oct", tenth_month_string )

# def test_volume_of_cube(self):
#     #add test code here
#     result = pow(cube_side, 3)
#     self.assertEqual(volume_of_cube, volume)


def volume(cube_edge):
    cube_edge = 5
    cube_volume = (cube_edge)*(cube_edge)*(cube_edge)
    return cube_volume

def reverse_string(input_string):
    rev_string = input_string[::-1]
    return rev_string

#   def test_fahrenheit_to_celsius(self):
#     #add test code here
#     pass



def fahrenheit_to_celsius(f_temp):
    c_temp = 0.5556 * (f_temp - 32.0)
    return c_temp

