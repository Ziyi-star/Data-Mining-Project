def decryptName(name):
    parts = name.split('_')
    shift = 49

    shifted_parts = [chr(int(part) + ord('a')) for part in parts]
    result = "".join(shifted_parts)

    return result
