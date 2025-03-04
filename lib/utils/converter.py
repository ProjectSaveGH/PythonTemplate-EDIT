from typing import Any
from lib.logger.logger import Logger

l: Logger = Logger(printLog=True)

def convert(from_type: str, to_type: str, value: Any) -> Any:
    """
    Convert a value from one type to another.

    :param from: The type of the value to convert from.
    :param to: The type of the value to convert to.
    :param value: The value to convert.
    :return: The converted value.
    """

    l.info(f"Converting \'{value}\' from \'{from_type}\' to \'{to_type}\'")
    
    if from_type == to_type:
        return value
    

    if from_type == None or to_type == None:
        return None
    if from_type == "None" or to_type == "None":
        return None
    

    if from_type not in ["str", "int", "float", "list", "tuple", "dict", "set", "bool", "bytes"]:
        raise ValueError(f"Unkown type in \'from_type\': {from_type}")
    if to_type not in ["str", "int", "float", "list", "tuple", "dict", "set", "bool", "bytes"]:
        raise ValueError(f"Unkown type in \'to_type\': {to_type}")
    

    # STRING
    if from_type == "str":
        match to_type:
            case "int":
                try:
                    return int(value)
                except:
                    return None
                
            case "float":
                try:
                    return float(value)
                except:
                    return None
                
            case "list":
                return [value]
            
            case "tuple":
                return (value)
            
            case "dict":
                return {value: None}
            
            case "set":
                return {value}
            
            case "bool":
                return True if value else False
            
            case "bytes":
                return value.encode()
    
    elif from_type == "int":
        match to_type:
            case "str":
                return str(value)
            
            case "float":
                return float(value)
            
            case "list":
                return [value]
            
            case "tuple":
                return (value)
            
            case "dict":
                return {value: None}
            
            case "set":
                return {value}
            
            case "bool":
                return True if value else False
            
            case "bytes":
                return bytes(value)
    
    elif from_type == "float":
        match to_type:
            case "str":
                return str(value)
            
            case "int":
                return int(value.round())
            
            case "list":
                return [value]
            
            case "tuple":
                return (value)
            
            case "dict":
                return {value: None}
            
            case "set":
                return {value}
            
            case "bool":
                return True if value else False
            
            case "bytes":
                return bytes(value)
    
    elif from_type == "list":
        match to_type:
            case "str":
                return str(value[0])
            
            case "int":
                try:
                    return int(value[0])
                except:
                    return None
            case "float":
                try:
                    return float(value[0])
                except:
                    return None
            
            case "tuple":
                return tuple(value)
            
            case "dict":
                try:
                    return {value[0]: value[1]}
                except KeyError:
                    return {value[0]: None}
                except:
                    return None
            
            case "set":
                return set(value)
            
            case "bool":
                return True if value else False
            
            case "bytes":
                return bytes(value)
    
    elif from_type == "tuple":
        match to_type:
            case "str":
                return str(value[0])
            
            case "int":
                try:
                    return int(value[0])
                except:
                    return None
            
            case "float":
                try:
                    return float(value[0])
                except:
                    return None
            
            case "list":
                return list(value)
            
            case "dict":
                try:
                    return {value[0]: value[1]}
                except KeyError:
                    return {value[0]: None}
                except:
                    return None
            
            case "set":
                return set(value)
            
            case "bool":
                return True if value else False
            
            case "bytes":
                return bytes(value)
    
    elif from_type == "dict":
        match to_type:
            case "str":
                return str(list(value.keys())[0])
            
            case "int":
                try:
                    return int(list(value.keys())[0])
                except:
                    return None
            
            case "float":
                try:
                    return float(list(value.keys())[0])
                except:
                    return None
            
            case "list":
                return list(value.items())
            
            case "tuple":
                return tuple(value.items())
            
            case "set":
                return set(value.items())
            
            case "bool":
                return True if value else False
            
            case "bytes":
                return bytes(value.items())
    
    elif from_type == "set":
        match to_type:
            case "str":
                return str(list(value)[0])
            
            case "int":
                try:
                    return int(list(value)[0])
                except:
                    return None
            
            case "float":
                try:
                    return float(list(value)[0])
                except:
                    return None
            
            case "list":
                return list(value)
            
            case "tuple":
                return tuple(value)
            
            case "dict":
                return {value.pop(): None}
            
            case "bool":
                return True if value else False
            
            case "bytes":
                return bytes(value)
    
    elif from_type == "bool":
        match to_type:
            case "str":
                return str(value)
            
            case "int":
                return None
            
            case "float":
                return None
            
            case "list":
                return [value]
            
            case "tuple":
                return (value)
            
            case "dict":
                return {value: None}
            
            case "set":
                return {value}
            
            case "bytes":
                return bytes(value)
    
    elif from_type == "bytes":
        match to_type:
            case "str":
                return value.decode()
            
            case "int":
                return int(value)
            
            case "float":
                return float(value)
            
            case "list":
                return [value]
            
            case "tuple":
                return (value)
            
            case "dict":
                return {value: None}
            
            case "set":
                return {value}
            
            case "bool":
                return True if value else False