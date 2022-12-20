import requests, datetime
from requests.structures import CaseInsensitiveDict

_apiURL = "https://dashboard.honeygain.com/api/"

def _makeHoneygainRequest(
    endpoint: str,
    method: str,
    headers: dict,
    timeout: int,
    v2: bool,
    data: dict = None,
    proxy: dict = None,
) -> requests.Response:
    """
    Make a request to the Honeygain API to a given endpoint
    :param endpoint: the API endpoint to request
    :param method: GET, POST, DELETE or PUT
    :param headers: authentication headers to send with the request
    :param timeout: the amount of time to wait for a response
    :param v2: whether or not to use the v2 API
    :param data (optional): data to send along with the requst
    :param proxy (optional): a dictionary containing the proxy to use
    :return: response object
    """


    url = _apiURL + ("v2/" if v2 else "v1/") + endpoint

    resp = requests.request(
        method,
        url,
        json=data,
        proxies=proxy,
        timeout=timeout,
        headers=headers
    )

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
            resp = _makeHoneygainRequest("earnings/stats", "GET", {"Authorization": "Bearer " + token}, self.timeout, False, proxy=self.proxy) # test the login data with the user_data endpoint with the proxy
        else:
            resp = _makeHoneygainRequest("earnings/stats", "GET", {"Authorization": "Bearer " + token}, self.timeout, False) # test the login data with the user_data endpoint

        if resp.status_code == 200: # if the headers were valid
            self.headers = {"Authorization": "Bearer " + token} # save the headers to the variable
            # return the right value depending on succeeding/failing
            return True
        return False
        
    def jtEarningsStats(self) -> dict:
        """
        Get data about the earning stats of the logged in user
        :return: a dictionary containing the stats
        """
        
        if self.proxy != {}: # if we have a proxy
            resp = _makeHoneygainRequest("jt-earnings/stats", "GET", self.headers, self.timeout, False, proxy=self.proxy) # get the user data with the proxy
        else:
            resp = _makeHoneygainRequest("jt-earnings/stats", "GET", self.headers, self.timeout, False) # get the user data
        
        try:
            jsonData = resp.json() # attempt to get the JSON data
        except:
            return None # if it failed return NoneType
        return jsonData
    
    def earningsStats(self) -> dict:
        """
        Get data about the earning stats of the logged in user
        :return: a dictionary containing the stats
        """
        
        if self.proxy != {}: # if we have a proxy
            resp = _makeHoneygainRequest("earnings/stats", "GET", self.headers, self.timeout, False, proxy=self.proxy) # get the user data with the proxy
        else:
            resp = _makeHoneygainRequest("earnings/stats", "GET", self.headers, self.timeout, False) # get the user data
        
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
            resp = _makeHoneygainRequest("users/balances", "GET", self.headers, self.timeout, False, proxy=self.proxy) # get the money data with the proxy
        else:
            resp = _makeHoneygainRequest("users/balances", "GET", self.headers, self.timeout, False) # get the devuce data
        
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
            resp = _makeHoneygainRequest("referrals/earnings", "GET", self.headers, self.timeout, False, proxy=self.proxy) # get the device data with the proxy
        else:
            resp = _makeHoneygainRequest("referrals/earnings", "GET", self.headers, self.timeout, False) # get the device data
        
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
            resp = _makeHoneygainRequest("earnings/today", "GET", self.headers, self.timeout, False, proxy=self.proxy) # get the app version with the proxy
        else:
            resp = _makeHoneygainRequest("earnings/today", "GET", self.headers, self.timeout, False) # get the version
        
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
            resp = _makeHoneygainRequest("devices", "GET", self.headers, self.timeout, True, proxy=self.proxy) # get the devices with the proxy
        else:
            resp = _makeHoneygainRequest("devices", "GET", self.headers, self.timeout, True)

        try:
            jsonData = resp.json() # attempt to get the JSON data
        except:
            return None
        return jsonData