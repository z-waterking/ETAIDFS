
$("#bt_post").click(function () {
	$.RefreshBread();
	$.ajax({
		type: "post",
		async: true, // 异步执行
		url: "post_data",
		data: JSON.stringify({'a':1}),
		contentType: 'application/json',
		dataType: "json", // 返回数据形式为json
		success: function (json) {
			console.log(json);
			$("#dv_post").html("完成测试：" + json["result"])
		},
		error: function (errorMsg) {
		}
	});
});

$("#bt_get").click(function () {
	alert('OK');
	$.ajax({
		type: "get",
		async: true, // 异步执行
		url: "get_data",
		data: {"a":1, "b":2},
		contentType: 'application/json',
		dataType: "json", // 返回数据形式为json
		success: function (json) {
			console.log(json);
			$("#dv_get").html("完成测试:" + json["result"]);
		},
		error: function (errorMsg) {
		}
    });
});