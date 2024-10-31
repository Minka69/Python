age = 20
has_driving_license = True
licence_country = "EE"

if age >= 18 and has_driving_license and (licence_country in ["LV", "CA", "EE", "LT"]):
    print("Tu vari vadīt auto.")
else:
    print("Tu nevari vadīt auto.")