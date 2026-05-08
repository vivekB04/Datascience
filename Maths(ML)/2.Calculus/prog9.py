#properties
# 5.1

slopes=[0.5,0.01,0.001]
for s in slopes:
    if abs(s)<0.1:
        print(f"Slope{s} : Close to converging")

