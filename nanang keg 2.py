def konversisuhu(c = 0, f = 0):
    a = c * 1.8 + 32
    b = (f - 32) / 1.8
    if f == 0:
        print "suhu", c, "celcius setara dengan", a, "fahrenheit"
    elif c == 0:
        print "suhu", f, "fahrenheit setara dengan", b, "celcius"
    
    
    
