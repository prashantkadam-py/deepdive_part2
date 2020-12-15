
class Myclass:

    def __init__(self):
        self.obj = None


    def __enter__(self):
        print("entering context.....")
        self.obj = "returning the object"
        return self.obj


    def __exit__(self, exc_type, exc_value, exc_tb):
        print("exiting the context.........")
        if exc_type:
            print(f"*** ERROR occured  exc_type : {exc_type}\
                    exc_value : {exc_value} exc_tb : {exc_tb}")
        #return False
        return True



class File:

    def __init__(self, fname, mode):
        self.mode = mode
        self.file_name = fname
        self.f_obj = None

    def __enter__(self):
        print("opening file.....")
        self.f_obj = open(self.file_name, self.mode)
        return self.f_obj

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("closing file....")
        self.f_obj.close()
        return True

if __name__ == "__main__":
    with Myclass() as ctx:
        print("inside context with block....")
        raise ValueError("Value Error ")
        print("after error")

    with File("README.md", "r") as f:
        print("reading file....")
        print(next(f))


