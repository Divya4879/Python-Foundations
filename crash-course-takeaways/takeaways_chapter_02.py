# --- 1. String Sanitization & Reassignment ---
# In backend systems, user input cannot be trusted. 
# Use str.lower() to normalize data before database storage.
raw_email = "  User@Example.com  "

# Strip removes whitespace, lower normalizes case.
# Note: String methods return new strings; they do NOT modify the original in place.
# You MUST reassign the value to keep the changes.
clean_email = raw_email.strip().lower()
print(f"Sanitized Email: {clean_email}")

# --- 2. The Floating-Point Trap ---
# Python defaults to a float in any operation using a float, or during division.
# However, floating-point arithmetic can yield arbitrary decimal places.
a = 0.2
b = 0.1
print(f"0.2 + 0.1 = {a + b}") # Outputs: 0.30000000000000004
# Takeaway: Never use standard floats for exact financial calculations.

# --- 3. Developer Quality of Life (QoL) ---
# Grouping large numbers with underscores makes them readable for humans.
# Python ignores the underscores during execution.
universe_age = 14_000_000_000

# Multiple assignment keeps initialization clean.
x, y, z = 0, 0, 0

# --- 4. Constants ---
# Python does not have a built-in constant type.
# Rely on the ALL_CAPS naming convention to signal that a variable should not be altered.
MAX_CONNECTIONS = 5000

# --- 5. The Zen of Python ---
# Zen of Python-> Tim Peters' philosophy on writing clean code.
import this