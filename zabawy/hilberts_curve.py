from turtle import *
def hilbert(n, k):
    def __hilbert(n, k):
        def __hilbert1(n, k):
            if n == 0:
                forward(k)
                left(90)
                forward(k)
                left(90)
                forward(k)
            else:
                __hilbert3(n-1, k/2)
                if n%2 == 1:
                    left(90)
                forward(k / (2 ** n))
                if n%2 == 0:
                    left(90)
                __hilbert1(n-1, k/2)
                if n%2 == 1:
                    right(90)
                forward(k / (2 ** n))
                if n%2 == 1:
                    right(90)
                __hilbert1(n-1, k/2)
                if n%2 == 0:
                    left(90)
                forward(k / (2 ** n))
                if n%2 == 1:
                    left(90)
                __hilbert3(n-1, k/2)



        def __hilbert2(n, k):
            if n == 0:
                forward(k)
                right(90)
                forward(k)
                right(90)
                forward(k)
            else:
                __hilbert1(n - 1, k / 2)
                if n % 2 == 1:
                    right(90)
                forward(k / (2 ** n))
                if n%2 == 0:
                    right(90)
                __hilbert3(n - 1, k / 2)
                if n % 2 == 1:
                    left(90)
                forward(k / (2 ** n))
                if n % 2 == 1:
                    left(90)
                __hilbert3(n - 1, k / 2)
                if n % 2 == 0:
                    right(90)
                forward(k / (2 ** n))
                if n % 2 == 1:
                    right(90)
                __hilbert1(n - 1, k / 2)


        def __hilbert3(n, k):
            if n == 0:
                forward(k)
                right(90)
                forward(k)
                right(90)
                forward(k)
            else:
                __hilbert2(n, k)

        def __hilbert4(n, k):
            if n == 0:
                forward(k)
                left(90)
                forward(k)
                left(90)
                forward(k)
            else:
                __hilbert1(n, k)

        if n == 0:
            left(90)
            __hilbert3(0, k)
        else:
            if n%2 == 0:
                left(90)
            __hilbert1(n-1, k/2)
            if n%2 == 1:
                right(90)
            forward(k/(2**n))
            if n%2 == 0:
                right(90)
            __hilbert2(n-1, k/2)
            if n%2 == 1:
                left(90)
            forward(k / (2 ** n))
            if n%2 == 1:
                left(90)
            __hilbert3(n-1, k/2)
            if n%2 == 0:
                right(90)
            forward(k / (2 ** n))
            if n%2 == 1:
                right(90)
            __hilbert4(n-1, k/2)



    color('red', 'yellow')
    begin_fill()

    __hilbert(n, k)

    end_fill()
    done()


k = 256
speed(0)
penup()
left(180)
forward(k/2)
left(90)
forward(k/2)
left(90)
pendown()

hilbert(5, k)