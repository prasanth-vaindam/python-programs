def outer():
    count = 0
    def inner():
        count +=1
    inner()

outer()