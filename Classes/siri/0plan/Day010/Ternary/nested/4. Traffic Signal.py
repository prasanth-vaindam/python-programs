color = input("Enter signal color: ")

action = "Stop" if color == "Red" else "Wait" if color == "Yellow" else "Go"

print(action)