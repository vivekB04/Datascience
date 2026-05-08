mean= 50
std=10
transaction= 500

threshold =mean +3*std

if transaction>threshold:
    print("Alert : Potential Fraudulent Transaction")