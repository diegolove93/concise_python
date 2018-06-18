def grade(score):
    if score >= 90:
        return "A"
    elif score < 90 and score >= 80:
        return "B"
    elif score < 80 and score >= 70:
        return "C"
    elif score < 70 and score >= 60:
        return "D"
    elif score < 60 and score >= 50:
        return "E"
    elif score < 50 and score >= 0:
        return "F"

def main():
    for score in range(0,101,5):
        print("%-5i%-5s" % (score,grade(score)) )
    return

if __name__ == "__main__":
    main()