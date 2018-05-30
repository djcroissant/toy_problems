import random

class Codec(object):
    HASHINDEX={}

    def encode(self, longUrl):
        """
        This function takes any url and returns a tinyurl
        Example:
        >>> encode("http://www.longurl.com")
        "http://tinyurl.com/4e9iAk"
        """
        characters="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        c = lambda: characters[random.randrange(len(characters))]
        code=c()+c()+c()+c()+c()+c()
        self.HASHINDEX[code] = longUrl
        return "http://tinyurl.com/" + code

    def decode(self, shortUrl):
        """
        This function takes an encoded url and returns the original
        Example:
        >>> decode("http://tinyurl.com/4e9iAk")
        "http://www.longurl.com"
        """
        code = shortUrl[-6:]
        return self.HASHINDEX[code]

url = "http://www.thisisalongurl.com"
codec = Codec()
print(codec.decode(codec.encode(url)) == url)
