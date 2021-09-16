chrome.contextMenus.create({
	title: "填充",
	onclick: function() {
		chrome.tabs.query({
			active: true,
			lastFocusedWindow: true
		}, function (tabs) {
			var t = tabs[0];
			var url = t.url;
			console.log(123, t, url);
			var urls = ['step3/person','step4/person','step3/media','step4/media','step3/gmedia','step4/gmedia','step3/gov','step4/gov','step3/org','step4/org','step3/army','step4/army'];
			for (let u of urls) {
				if(url.indexOf(u) > -1) {
					u = u.replace('/', '-');
					chrome.tabs.executeScript(null, {file: `js/${u}.js`});
				}
			}
		});
		// console.log(122223 ,document);
	}
});

// chrome.runtime.onMessage.addListener(function(request, sender, callback)
// {
// 	// var res = await getCookies();
// 	// console.log(123, res);
// 	// callback(res);
// 	// console.log(123,request);
// 	mainDoc = request;
// 	// getCookies().then(res => {
// 	// 	console.log(123, res);
// 	// 	callback('我是后台11，' + JSON.stringify(res));
// 	// })
	
// 	return true;
// });
