import enum
class Message(object):
    def __init__(self,message):
        from string import Template
        self.header    = Template(message["header"])
        self.body      = Template(message["body"])
        self.eventType =          message["eventType"]

    def substitute(self,**kwargs):
    
        from string import Template
    
        for key,value in kwargs.items():
            i = {"{}".format(key):value}
    
            # Substitute the keywords into the tempate and save the result (string)
            self.header = self.header.safe_substitute(i)
            self.body = self.body.safe_substitute(i)
    
            # Convert the resulting string back into a template
            self.header = Template(self.header)
            self.body = Template(self.body)
    
        if ((    len(Template.pattern.findall(self.header.safe_substitute())) is 0) and
            (    len(Template.pattern.findall(self.body.safe_substitute())) is 0)):
            self.header = self.header.safe_substitute()
            self.body = self.body.safe_substitute()
            return True  # True that the string is substituted completely
        else:
            return False # False that the string is substitute completely
