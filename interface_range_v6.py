list_of_interfaces = ['Fi1/0/1', 'Fi1/0/3', 'Fi1/0/4', 'Fi1/0/5', 'Fi1/0/6', 'Fi1/0/8', 'Fi1/0/10', 'Fi1/0/11', 'Fi1/0/12', 'Fi1/0/13', 'Fi1/0/14', 'Fi1/0/15', 'Fi1/0/16', 'Fi1/0/17', 'Fi1/0/18', 'Fi1/0/19', 'Fi1/0/20', 'Fi2/0/1', 'Fi2/0/2', 'Fi2/0/24', 'Fi2/0/25', 'Fi2/0/26', 'Fi2/0/34', 'Fi2/0/35', 'Fi2/0/36', 'Fi2/0/37', 'Fi2/0/38', 'Fi3/0/1', 'Fi3/0/2', 'Fi3/0/3', 'Fi3/0/4', 'Fi3/0/5', 'Fi3/0/6', 'Fi3/0/10', 'Fi3/0/44', 'Fi3/0/46', 'Fi3/0/47', 'Fi3/0/48']
        
def int_range(list_of_interfaces):
    
    slots_and_interfaces = {}
    interface_types = ['Fi', 'Gi']
    for slot in range(1,10):
        ports = []
        for interface in list_of_interfaces:
            for interface_type in interface_types:
                if f"{interface_type}{slot}" in interface:
                    parts = interface.split("/")
                    ports.append(parts[2])
                    slots_and_interfaces[f"{interface_type}{slot}"] = ports
    
    slots_and_ranges = {}
    for key in slots_and_interfaces.keys():
        ranges = ""
        ports1 = slots_and_interfaces[key]
        for index in range(len(ports1)):
            if index == 0:
                if int(ports1[index]) == len(ports1) - 1:
                    ranges += ports1[index]
                elif int(ports1[index + 1]) == int(ports1[index]) + 1:
                    ranges += ports1[index] + "-"
                elif int(ports1[index + 1]) != int(ports1[index]) + 1:
                    ranges += ports1[index] + ","
            elif index + 1 == int(len(ports1)):
                if ranges[-1] == "-" or ",":
                    ranges += ports1[index]
            else:
                if ranges[-1] == "," and int(ports1[index + 1]) != int(ports1[index]) + 1:
                    ranges += ports1[index] + ","
                elif ranges[-1] == "," and int(ports1[index + 1]) == int(ports1[index]) + 1:
                    ranges += ports1[index] + "-"
                elif ranges[-1] == "-" and int(ports1[index + 1]) != int(ports1[index]) + 1:
                    ranges += ports1[index] + ","
                elif ranges[-1] == "-" and int(ports1[index + 1]) == int(ports1[index]) + 1:
                    continue
                
        slots_and_ranges[key] = ranges.split(",")
    
    list_of_ranged_interfaces = []
    for key in slots_and_ranges.keys():
        for index in slots_and_ranges[key]:
            list_of_ranged_interfaces.append(f"{key}/{parts[1]}/{index}")
    
    list_of_5_ranged_interfaces = []
    five_ranged_interfaces = ""
    count = 1
    for port_range in range(len(list_of_ranged_interfaces)):
        if port_range != len(list_of_ranged_interfaces) - 1:
            if count != 5:
                five_ranged_interfaces += list_of_ranged_interfaces[port_range] +","
                count += 1
            elif count == 5:
                five_ranged_interfaces += list_of_ranged_interfaces[port_range] +"."
                count = 1
        elif port_range == len(list_of_ranged_interfaces) - 1:
            five_ranged_interfaces += list_of_ranged_interfaces[port_range]
    list_of_5_ranged_interfaces = five_ranged_interfaces.split(".")

    list_of_int_range_commands = []
    for interface_group in list_of_5_ranged_interfaces:
        list_of_int_range_commands.append(f"interface range {interface_group}")

    return list_of_int_range_commands

            

print(int_range(list_of_interfaces))