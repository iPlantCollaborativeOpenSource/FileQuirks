"""
Module contains text procession utility functions
"""

def decode_file(file_content):
  ret = decode_file_encoding(file_content)
  if ret:
    ret = decode_file_dos2unix(file_content)
  return ret

def decode_file_encoding(file_content):
    """
    Tries to decode file as UTF-8 (which is superset of ASCII). If that fails,
    tries UTF-16. If file can't be decoded, None is returned.
    """
    try:
        return file_content.decode("utf-8")
    except:
        pass
    try:
        return file_content.decode("utf-16")
    except:
        pass
    return None

def decode_file_dos2unix(file_content):
    return file_content.replace("\r", "")
