import string
import random

def generate_short_code(prefix="url", length=4):
    suffix = ''.join(random.choices('abcdefghijkmnopqrstuvwxyz23456789', k=length))
    return f"{prefix}-{suffix}"


