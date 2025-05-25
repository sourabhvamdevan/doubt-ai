

PHYSICS_CONSTANTS = {
    "speed_of_light": {"value": 299792458, "unit": "m/s"},
    "gravitational_constant": {"value": 6.67430e-11, "unit": "N·m²/kg²"},
    "plancks_constant": {"value": 6.62607015e-34, "unit": "J·s"},
    "electron_mass": {"value": 9.10938356e-31, "unit": "kg"},
}

class PhysicsConstants:
    def lookup(self, constant_name: str):
        normalized = constant_name.lower().replace(" ", "_")
        return PHYSICS_CONSTANTS.get(normalized, {"error": "Constant not found"})