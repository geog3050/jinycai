# return leaves status based on the threshold for different climate types and the temperature of different days
def leaves_status(climate, temp_list):
    threshold = 0
    if climate.lower() == 'tropical':
        threshold = 30
    elif climate.lower() == 'continental':
        threshold = 25
    else:
        threshold = 18
    
    leaves_status_list = []
    for temp in temp_list:
        if temp > threshold:
            leaves_status_list.append('U')
        else:
            leaves_status_list.append('F')
    return leaves_status_list


climate = input('Please enter the climate (Tropical, Continental, or others): ')

try:
    temp_list_org = input('Please enter the temperature list: ')
    temp_list = eval(temp_list_org)
    if isinstance(temp_list, list) == False:
        raise TypeError("Input temperature is not a list")
except TypeError as e:
    print(e)
except Exception:
    print("Input temperature is not valid")
else:
    leaves_status_list = leaves_status(climate, temp_list)
    for leaves_status in leaves_status_list:
        print(leaves_status)