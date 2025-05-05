def calculate_bmi(height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def main():
    import os

    height = float(os.getenv("HEIGHT", "1.75"))
    weight = float(os.getenv("WEIGHT", "68"))

    bmi = calculate_bmi(height, weight)
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"BMI: {bmi}")

if __name__ == "__main__":
    main()
