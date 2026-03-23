def new_patient(name, age, glucose, bp, hb):
    risk_list = []
    def check_age(a):
        return "senior" if a > 60 else "normal"
    def check_glucose(g):
        return "diabetes" if g > 160 else "normal"
    def check_bp(b):
        return "hypertension" if b > 120 else "normal"
    def check_hb(hb):
        return "low" if hb < 12 else "normal"
    def check_risk(a, g, b, hb):
        return "critical" if g > 160 and b > 120 and hb < 12 else "normal"
    a = check_age(age)
    g = check_glucose(glucose)
    b = check_bp(bp)
    h = check_hb(hb)
    risk = check_risk(age, glucose, bp, hb)
    risk_list.append({
        "name": name,
        "age": a,
        "glucose": g,
        "bp": b,
        "hb": h,
        "risk": risk
    })
    return risk_list
result = new_patient("rahul", 49, 170, 140, 10)
for r in result:
    print(r)
