import requests, datetime
from requests.structures import CaseInsensitiveDict

def makeHoneygainRequest(endpoint: str, reqType: str, headers: dict, timeout: int, v2: bool, data: dict = {}, proxy: dict = {}) -> requests.Response:
    """
    Make a request to the Honeygain API to a given endpoint
    :param endpoint: the API endpoint to request
    :param reqType: GET, POST, DELETE or PUT
    :param headers: authentication headers to send with the request
    :param data (optional): data to send along with the requst
    :return: response object
    """
    
    if reqType == "GET": # if we need to do a GET request
        if proxy != {}: # if we need to use a proxy
            resp = requests.get(("https://dashboard.honeygain.com/api/v1/" if v2 == False else "https://dashboard.honeygain.com/api/v2/") + endpoint, headers=headers, proxies=proxy, timeout=timeout) # do the GET request with the headers required to the correct endpoint using proxy
        else:
            resp = requests.get(("https://dashboard.honeygain.com/api/v1/" if v2 == False else "https://dashboard.honeygain.com/api/v2/") + endpoint, headers=headers, timeout=timeout) # do the GET request with the headers required to the correct endpoint
    elif reqType == "POST": # if we need to do a POST request
        if proxy != {}: # if we need to use a proxy
            resp = requests.post(("https://dashboard.honeygain.com/api/v1/" if v2 == False else "https://dashboard.honeygain.com/api/v2/") + endpoint, headers=headers, data=data, proxies=proxy, timeout=timeout) # do the POST request with the headers required to the correct endpoint with the data using proxy
        else:
            resp = requests.post(("https://dashboard.honeygain.com/api/v1/" if v2 == False else "https://dashboard.honeygain.com/api/v2/") + endpoint, headers=headers, data=data, timeout=timeout) # do the POST request with the headers required to the correct endpoint with the data
    elif reqType == "DELETE": # if we need to do a DELETE request
        if proxy != {}: # if we need to use a proxy
            resp = requests.delete(("https://dashboard.honeygain.com/api/v1/" if v2 == False else "https://dashboard.honeygain.com/api/v2/") + endpoint, headers=headers, proxies=proxy, timeout=timeout) # do the DELETE request with the headers required to the correct endpoint using proxy
        else:
            resp = requests.delete(("https://dashboard.honeygain.com/api/v1/" if v2 == False else "https://dashboard.honeygain.com/api/v2/") + endpoint, headers=headers, timeout=timeout) # do the DELETE request with the headers required to the correct endpoint
    elif reqType == "PUT": # if we need to do a PUT request
        if proxy != {}: # if we need to use a proxy
            resp = requests.put(("https://dashboard.honeygain.com/api/v1/" if v2 == False else "https://dashboard.honeygain.com/api/v2/") + endpoint, headers=headers, data=data, proxies=proxy, timeout=timeout) # do the PUT request with the headers required to the correct endpoint with the data using proxy
        else:
            resp = requests.put(("https://dashboard.honeygain.com/api/v1/" if v2 == False else "https://dashboard.honeygain.com/api/v2/") + endpoint, headers=headers, data=data, timeout=timeout) # do the PUT request with the headers required to the correct endpoint with the data
    else:
        return None
    return resp

class User:
    headers = {}
    proxy = {}
    timeout = 10 # default timeout for requests

    def setProxy(self, proxy: dict) -> bool:
        """
        Set the proxy for the requests
        :param proxy: proxy dictionary
        :return: True
        """
        
        self.proxy = proxy # set the proxy
        return True

    def login(self, token: str) -> bool:
        """
        Attempt to log in to the Honeygain account by requesting the earnings/stats endpoint and if it succeeds, it will write that data to the headers variable
        :param token: Bearer token from the Honeygain dashboard
        :param method (optional): login method, only current option is google.
        :return: True on successful login, False otherwise
        """
        
        if self.proxy != {}: # if we have a proxy
            resp = makeHoneygainRequest("earnings/stats", "GET", {"Authorization": "Bearer " + token}, self.timeout, False, proxy=self.proxy) # test the login data with the user_data endpoint with the proxy
        else:
            resp = makeHoneygainRequest("earnings/stats", "GET", {"Authorization": "Bearer " + token}, self.timeout, False) # test the login data with the user_data endpoint
        
        print(resp.json())

        if resp.status_code == 200: # if the headers were valid
            self.headers = {"Authorization": "Bearer " + token} # save the headers to the variable
            # return the right value depending on succeeding/failing
            return True
        return False
        
    def earningsStats(self) -> dict:
        """
        Get data about the earning stats of the logged in user
        :return: a dictionary containing the stats
        """
        
        if self.proxy != {}: # if we have a proxy
            resp = makeHoneygainRequest("earnings/stats", "GET", self.headers, self.timeout, False, proxy=self.proxy) # get the user data with the proxy
        else:
            resp = makeHoneygainRequest("earnings/stats", "GET", self.headers, self.timeout, False) # get the user data
        
        try:
            jsonData = resp.json() # attempt to get the JSON data
        except:
            return None # if it failed return NoneType
        return jsonData
        
    def balance(self) -> dict:
        """
        Get data about the logged in user's balance (current balance, min payout, earnt today)
        :return: a dictionary containing the user's balance data
        """
        
        if self.proxy != {}: # if we have a proxy
            resp = makeHoneygainRequest("users/balances", "GET", self.headers, self.timeout, False, proxy=self.proxy) # get the money data with the proxy
        else:
            resp = makeHoneygainRequest("users/balances", "GET", self.headers, self.timeout, False) # get the devuce data
        
        try:
            jsonData = resp.json() # attempt to get the JSON data
        except:
            return None # if it failed return NoneType
        return jsonData
        
    def refEarnings(self) -> dict:
        """
        Get data about the logged in user's referral earnings
        :return: a dictionary containing the user's referral earnings data
        """
        
        if self.proxy != {}: # if we have a proxy
            resp = makeHoneygainRequest("referrals/earnings", "GET", self.headers, self.timeout, False, proxy=self.proxy) # get the device data with the proxy
        else:
            resp = makeHoneygainRequest("referrals/earnings", "GET", self.headers, self.timeout, False) # get the device data
        
        try:
            jsonData = resp.json() # attempt to get the JSON data
        except:
            return None # if it failed return NoneType
        return jsonData
        
    def earningsToday(self) -> dict:
        """
        Get the earnings of the logged in user today
        :return: a dictionary containing the latest version
        """
        
        if self.proxy != {}: # if we have a proxy
            resp = makeHoneygainRequest("earnings/today", "GET", self.headers, self.timeout, False, proxy=self.proxy) # get the app version with the proxy
        else:
            resp = makeHoneygainRequest("earnings/today", "GET", self.headers, self.timeout, False) # get the version
        
        try:
            jsonData = resp.json() # attempt to get the JSON data
        except:
            return None # if it failed return NoneType
        return jsonData

    def devices(self) -> dict:
        """
        Get the devices of the logged in user
        :return: a dictionary containing the devices
        """
        
        if self.proxy != {}: # if we have a proxy
            resp = makeHoneygainRequest("devices", "GET", self.headers, self.timeout, True, proxy=self.proxy) # get the devices with the proxy
        else:
            resp = makeHoneygainRequest("devices", "GET", self.headers, self.timeout, True)

        try:
            jsonData = resp.json() # attempt to get the JSON data
        except:
            return None
        return jsonData