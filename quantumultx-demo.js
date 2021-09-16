if ($request.url.indexOf('json') > -1) {

	console.log(111);
	var body = $response.body;
	console.log(body);
} else {
	console.log(222);
}
console.log(new Date());
$done(body);