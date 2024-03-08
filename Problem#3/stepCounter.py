def feet_to_steps(user_feet):
    feet_per_step = 2.5  # Assuming an average step length of 2.5 feet
    return user_feet / feet_per_step

if __name__ == '__main__':
    user_feet = float(input("Enter feet: "))
    print(f'Steps: {feet_to_steps(user_feet):.2f}')
