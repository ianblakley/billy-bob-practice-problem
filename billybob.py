def main():
    #billy bob wants 2000 dollar yeezys, needs $8000 total
    wage = float(input("\nHow much is Billy Bob's hourly wage?: "))
    #will 43 hours per week, 20 weeks of work get ≥8000
    #equation should be (43*$)*20 = 8000
    if ((43 * wage) * 20) >= 8000:
        print("\nyeezy\n")
    else:
        print("\nno yeezy\n")
main()