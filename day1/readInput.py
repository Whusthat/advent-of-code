def read_input(filePath):
    list = []
    with open(filePath) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        
        for line in lines:
            list.append(int(line))
    return list
        
            
            
