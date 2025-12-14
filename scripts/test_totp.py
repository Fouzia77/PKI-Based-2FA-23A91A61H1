import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.totp_utils import generate_totp_code, verify_totp_code

hex_seed = "1abf5423c26b5f78dc6a1f2c14010e27b8ebd2c545 a13538c7b0e3efd7e4aed4"

code = generate_totp_code(hex_seed)
print("Generated OTP:", code)

is_valid = verify_totp_code(hex_seed, code)
print("Is valid:", is_valid)