function start() {
	chrome.runtime.sendMessage(document.outerHTML, function(response) {
		console.log(111, response);
	});
}

async function main(url) {
	await sleep(10);
	for (let index = 0; index < 10; index++) {
		var res = checkTime();
		if(res) {
			break;
		}
		await sleep(5);
	}
	window.open(url, "_self");
}

function checkTime() {
	try {
		var _t = document.getElementsByClassName('bilibili-player-video-time-now')[0].innerText;
		var sec = _t.split(':')[1];
		console.log(330, _t);
		return Number(sec) > 20;
	} catch (error) {
		console.error(error);
	}
	return false;
}

// start();
