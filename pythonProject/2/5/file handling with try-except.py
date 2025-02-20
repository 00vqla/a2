try:
    f = open("demofile.txt")
    try:
        f.write("monkey")
    except:
        print("error occurred")
    finally:
        f.close()
except:
    print("file not found")

