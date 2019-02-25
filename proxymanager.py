import random


class ProxyManager:
	def __init__(self, proxy_list):
		self.proxies = self.format(proxy_list)
		self.currentIndex = 0

	@staticmethod
	def format(proxy_list, returnRaw=False):
		"""
			returnRaw: True -> ["127.0.0.1:80", {"https": "https://127.0.0.1:80", "http": "http://127.0.0.1:80"}]
			returnRaw: False -> {"https": "https://127.0.0.1:80", "http": "http://127.0.0.1:80"}
		"""

		formattedProxies = []
		for proxy in proxy_list:
			if len(proxy.split(":")) >= 3:
				hasAuth = True
			else:
				hasAuth = False

			if hasAuth:
				ip = proxy.split(":")[0]
				port = proxy.split(":")[1]
				ipPortProxy = ip + ':' + port
				proxyUser = proxy.split(":")[2].rstrip()
				proxyPass = proxy.split(":")[3].rstrip()

				proxies = {
					'http': 'http://' + proxyUser + ':' + proxyPass + '@' + ipPortProxy,
					'https': 'https://' + proxyUser + ':' + proxyPass + '@' + ipPortProxy
				}
			else:
				proxies = {
					'http': 'http://' + proxy,
					'https': 'https://' + proxy
				}

			if not returnRaw:
				formattedProxies.append(proxies)
			else:
				formattedProxies.append([proxy, proxies])
		return temp

	def nextProxy(self):
		if len(self.proxies) == 0:
			return None

		if self.currentIndex >= len(self.proxies):
			self.currentIndex = 0

		proxy = self.proxies[self.currentIndex]
		self.currentIndex += 1
		return proxy

	def randomProxy(self):
		if len(self.proxies) == 0:
			return None

		return random.choice(self.proxies)
