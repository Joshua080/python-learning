file = input("Please submit the name of your file: ")
match file.lower().split(".")[1]:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
