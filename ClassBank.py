from math import *

question_var = [
    "Enter the value of s: ",
    "Enter the value of u: ",
    "Enter the value of v: ",
    "Enter the value of a: ",
    "Enter the value of t: ",
]


class FindS:

    def noV(self):
        a = float(input(question_var[3]))
        t = float(input(question_var[4]))
        u = float(input(question_var[1]))
        s = u * t + 0.5 * (a * pow(t, 2))
        return s

    def noA(self):
        t = float(input(question_var[4]))
        u = float(input(question_var[1]))
        v = float(input(question_var[2]))
        s = 0.5 * (u + v) * t
        return s

    def noT(self):
        a = float(input(question_var[3]))
        u = float(input(question_var[1]))
        v = float(input(question_var[2]))
        s = (pow(v, 2) - pow(u, 2)) / (2 * a)
        return s


# Function to find "u"
class FindU:
    def noV(self):
        a = float(input(question_var[3]))
        s = float(input(question_var[0]))
        t = float(input(question_var[4]))
        u = (s - 0.5 * a * pow(t, 2)) / t
        return u

    def noA(self):
        s = float(input(question_var[0]))
        t = float(input(question_var[4]))
        v = float(input(question_var[2]))
        u = (2 * s) / t - v
        return u

    def noT(self):
        a = float(input(question_var[3]))
        s = float(input(question_var[0]))
        v = float(input(question_var[2]))
        u = sqrt(pow(v, 2) - 2 * a * s)
        return u

    def noS(self):
        a = float(input(question_var[3]))
        t = float(input(question_var[4]))
        v = float(input(question_var[2]))
        u = v - a * t
        return u


# Function to find "v"
class FindV:
    def noA(self):
        s = float(input(question_var[0]))
        t = float(input(question_var[4]))
        u = float(input(question_var[1]))
        v = (2 * s) / t - u
        return v

    def noT(self):
        a = float(input(question_var[3]))
        s = float(input(question_var[0]))
        u = float(input(question_var[1]))
        v = sqrt(pow(u, 2) + 2 * a * s)
        return v

    def noS(self):
        a = float(input(question_var[3]))
        t = float(input(question_var[4]))
        u = float(input(question_var[1]))
        v = u + a * t
        return v


# Function to find "a"
class FindA:
    def noV(self):
        s = float(input(question_var[0]))
        t = float(input(question_var[4]))
        u = float(input(question_var[1]))
        a = 2 * (s - u * t) / pow(t, 2)
        return a

    def noT(self):
        s = float(input(question_var[0]))
        u = float(input(question_var[1]))
        v = float(input(question_var[2]))
        a = (pow(v, 2) - pow(u, 2)) / (2 * s)
        return a

    def noS(self):
        t = float(input(question_var[4]))
        u = float(input(question_var[1]))
        v = float(input(question_var[2]))
        a = (v - u) / t
        return a


# Function to find "t"
class FindT:
    def noA(self):
        s = float(input(question_var[0]))
        u = float(input(question_var[1]))
        v = float(input(question_var[2]))
        t = (2 * s) / (u + v)
        return t

    def noS(self):
        a = float(input(question_var[3]))
        u = float(input(question_var[1]))
        v = float(input(question_var[2]))
        t = (v - u) / a
        return t

    # Error encountered when complex number attained
    def noU(self):
        a = float(input(question_var[3]))
        s = float(input(question_var[0]))
        v = float(input(question_var[2]))
        if pow(v, 2) < (2 * a * s):
            print("Complex number attained!")
        else:
            u = sqrt(pow(v, 2) - 2 * a * s)
            t = (v - u) / a
            return t