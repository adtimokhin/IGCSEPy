class Parcel:
    rejections = []

    def __init__(self, width, height, length, weight):
        self.width = width
        self.height = height
        self.length = length
        self.weight = weight

    def __add_rejection(self, message):
        self.rejections.append(message)

    def __no_rejections(self):
        return (True if len(self.rejections) == 0 else False)

    def _print_rejections(self):
        rejection_value = len(self.rejections)
        if rejection_value == 0:
            print("no rejections")
        else:
            for i in range(rejection_value):
                print(str(i) + ". " + self.rejections[i])


reject_reason_one = "width is invalid"
reject_reason_two = "height is invalid"
reject_reason_three = "length is invalid"
reject_reason_four = "invalid weight"

reject_reason_five = "expected width: less than 80 cm. Entered width is "
reject_reason_six = "expected height: less than 80 cm. Entered height is "
reject_reason_seven = "expected length: less than 80 cm. Entered length is "
reject_reason_eight = "expected weight: 1 to 10 kg. Entered weight is "
reject_reason_nine = "total sum of all 3 dimensions should be no more that 200. Total sum of the parcel is "

parcels = []


def check_for_integer(value):
    try:
        return type(int(value)) == int
    except:
        return False


def check_for_float(value):
    try:
        return type(float(value)) == float
    except:
        return False


def init_parcel():  # todo: remove exception counter.
    # Method checks if all entered data is in valid types
    exception_counter = 0;
    width = input("enter width")
    if check_for_integer(width): # can be swapped with check_for_float()  if float number is required
        width = int(width)
    else:
        print(reject_reason_one)
        exception_counter += 1
    height = input("enter height")
    if check_for_integer(height):
        height = int(height)

    else:
        print(reject_reason_two)
        exception_counter += 1
    lenght = input("enter length")
    if check_for_integer(lenght):
        lenght = int(lenght)
    else:
        print(reject_reason_three)
        exception_counter += 1
    weight = input("enter weight")
    if check_for_float(weight):
        weight = float(weight)

    else:
        print(reject_reason_four)
        exception_counter += 1
    if exception_counter == 0:
        parcels.append(Parcel(width, height, lenght,
                              weight))  # add new parcel to the list of all parcels entered the system
    return exception_counter


def less_than_80(dimension):
    return True if 0 < dimension < 80 else False


def right_weigh(dimension):
    return True if 10 >= dimension >= 1 else False


def check_dimensions(parcel):
    if type(parcel) is not Parcel:  # todo: check if works
        print("fatal error")
        return
    rejections = []
    if not less_than_80(parcel.width):
        rejections.append(reject_reason_five + str(parcel.width))
    if not less_than_80(parcel.height):
        rejections.append(reject_reason_six + str(parcel.height))
    if not less_than_80(parcel.length):
        rejections.append(reject_reason_seven + str(parcel.length))
    if not right_weigh(parcel.weight):
        rejections.append(reject_reason_eight + str(parcel.weight))
    sum = parcel.width + parcel.height + parcel.length
    if sum > 200:
        rejections.append(reject_reason_nine + str(sum))

    if len(rejections) == 0:
        valid_parcels.append(parcel)
        print("accepted")
    else:
        invalid_parcels.append(parcel)
        print("rejected")
        for i in range(len(rejections)):
            print(str(i+1) + ". " + rejections[i])


valid_parcels = []
invalid_parcels = []

trigger = bool(False if input("Add another parcel?") == "-1" else True)  # -1 no, otherwise - yes
index = 0
while trigger:  # by making -1 a string we exclude the need need to check the value for validation
    if init_parcel() == 0:
        check_dimensions(parcels[index])
        index += 1
    trigger = bool(False if input("Add another parcel?") == "-1" else True)

