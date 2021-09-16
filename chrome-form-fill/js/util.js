const getStorageData = (key) =>
	new Promise((resolve, reject) =>
		chrome.storage.local.get(key, result =>
	  		chrome.runtime.lastError ? reject(Error(chrome.runtime.lastError.message)) : resolve(result)
		)
	)


const setStorageData = data =>
	new Promise((resolve, reject) =>
		chrome.storage.local.set(data, () => 
			chrome.runtime.lastError ? reject(Error(chrome.runtime.lastError.message)) : resolve()
		)
	)


const sleep = s => {
	return new Promise(resolve => setTimeout(resolve, s * 1000))
}