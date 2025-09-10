def to_hex_string(data):
    """Convert string or bytes to a hex string representation as a list of hex elements."""
    if isinstance(data, str):
        byte_data = data.encode()
    else:
        byte_data = data
    result = [f"{byte:02x}" for byte in byte_data]
    return result

def add_start_end_markers(byte_data):
    """Add start and end markers to the data."""
    result = list()
    result.append(0x74)  # Start marker
    result.extend(byte_data)
    result.append(0xff)
    result.append(0xff)
    result.append(0xff)  # End marker
    return result

def get_ready_message(target, value):
    """
    Формує повідомлення для Nextion: 0x74 + target + '.txt="' + value + '"' + 0xff 0xff 0xff
    """
    message = bytearray()
    message.append(0x74)  # Стартовий байт
    message.extend(target.encode())
    message.extend(b'.txt="')
    message.extend(value.encode())
    message.append(0x22)  # Закриваюча лапка
    message.extend([0xff, 0xff, 0xff])  # Кінцеві байти
    return list(message)