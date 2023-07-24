### custom date class
class date:
    months = ['default','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October'\
             ,'November', 'December']
        
    def __init__(self,_1=0, _2=0, _3=0,format='%d/%m/%y', word=False):
        assert type(_1) == type(1), "Error: must be an integer"
        assert type(_2) == type(1), "Error: must be an integer"
        assert type(_3) == type(1), "Error: must be an integer"

        assert type(format) == type("string"), "format parameter must be a string"
        assert len(format) == 8, "length of format parameter must be 8 characters"
        
        f = format
        import re #import regex

        # creating our list of indices from format 
        f = re.split("\W", f)

        # format assertions
        assert f[1] in ['d', 'm', 'y'], "format string wrong. check index 1"
        assert f[3] in ['d', 'm', 'y'], "format string wrong. check index 3"
        assert f[5] in ['d', 'm', 'y'], "format string wrong. check index 5"
        
        # dictionary for reference
        d = {f[1]: _1, f[3]: _2, f[5]: _3}
        


        self.__day, self.__month, self.__year = self.__validate(d['d'], d['m'], d['y'])
        self.format = format
        self.__word = word
        
        self.__evaluate_date()
    
    
    def __dayh(self, digit):
        if int(digit) == 1:
            return 'st'
        elif int(digit) == 2:
            return 'nd'
        elif int(digit) == 3:
            return 'rd'
        else:
            return 'th'
    
    def __str__(self):
        
        if self.__word:
            return self.months[int(self.__month)] + ' ' + self.__day + self.__dayh(str(self.__day)[-1]) + ', ' + self.__year
        else:
            string = self.format
            string = string.replace("%d", str(self.__day))
            string = string.replace("%m", str(self.__month))
            string = string.replace("%y", str(self.__year))
            return string
    
    def __validate(self,dd,mm,yy):
        
        ####validations follow####
        if len(str(dd)) > 2:
            raise ValueError('Invalid day value. Length exceeded.')
        
        if len(str(mm)) > 2:
            raise ValueError('Invalid month value. Length exceeded.')
        
        if yy < 0:
            raise ValueError('Values of year only start from 0 CE.') # can be adjusted for later
        # if len(str(yy)) < 4:
        #     raise ValueError('Invalid year value. Length exceeded.')
            
        max1=0
        if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
            max1=31
        elif(mm==4 or mm==6 or mm==9 or mm==11):
            max1=30
        elif(yy%4==0 and yy%100!=0 or yy%400==0):
            max1=29
        else:
            max1=28
        
        if mm<1 or mm>12:
            raise ValueError('Invalid month value. Accepted range [1,12]')
        elif dd<1 or dd>max1:
            raise ValueError('Invalid day value.')
        
        ####Validations end here#####
        return str(dd),str(mm),str(yy)
        
    
    def __evaluate_date(self):
        if len(self.__day) != 2:
            self.__day = '0' + self.__day
        if len(self.__month) != 2:
            self.__month = '0' + self.__month
    
    
    def toggle_word(self):
        if self.__word:
            self.__word = False
        else:
            self.__word = True
            
        return self
    
    def __getitem__(self, key):
        """
        Key reference:-
            name  | key 
            -------------
            day   | 'd', 'day', 0
            month | 'm', 'month', 1
            year  | 'y', 'year', 2

        EXAMPLE USAGE:-
        Suppose you want to get the month value.
            >>> x = date(19/2/1998)
            >>> x['month']
            [out]: '02'

            >>> x['m']
            [out]: '02'

            >>> x[1]
            [out]: '02'
            
        """
        if key in ['d', 0, 'day', -3]:
            return self.__day
        elif key in ['m', 1, 'month', -2]:
            return self.__month
        elif key in ['y', 2, 'year', -1]:
            return self.__year
        else:
            raise ValueError("Key value is wrong.")
        
        
    def __setitem__(self, key, value):
        """
         Key reference:-
            name  | key 
            -------------
            day   | 'd', 'day', 0
            month | 'm', 'month', 1
            year  | 'y', 'year', 2
        """
        d = int(self.__day)
        m = int(self.__month)
        y = int(self.__year)
        
        if key in ['d', 0, 'day', -3]:
            self.__day, self.__month, self.__year = self.__validate(value, m, y)
        elif key in ['m', 1, 'month', -2]:
            self.__day, self.__month, self.__year = self.__validate(d, value, y)
        elif key in ['y', 2, 'year', -1]:
            self.__day, self.__month, self.__year = self.__validate(d, m, value)
        else:
            raise ValueError("Key value is wrong.")
        
        self.__evaluate_date()
        

    def to_date(value, format='%d/%m/%y'):
        """
            Convert the date in string to date format
        """
        
        if format[2] not in value:
            raise ValueError("wrong format in string. Use correct `format`.")
        
        d, m, y = value.split(format[2])
        newd = date(int(d), int(m), int(y), format=format)

        return newd
    

    ### some utils. still testing these
    def addYear(shift=1):
        assert type(shift) == type(1), "Value has to be integer."

        yy = self.__year + shift
        if yy < 0:
            raise ValueError("Shift is exceeded limit. raised negative year value.")
        else:
            self.__year += shift

    def addMonth(shift=1):

        """
        note: 07192023
            this one looks counter intuitive as months are 'sort of' cyclical and repeat every year. So if limit exceeds the 12 then
            I must reflect the change in year variable to show that if shifti s more than 12 then I must shift to 1st month of next
        """
        assert type(shift) == type(1), "value has to be integer"

        mm = self.__month + shift

        if mm < 1 or mm > 12:
            raise ValueError("Shift exceeded boundary limit of [1,12].")
        else:
            self.__month += shift
    