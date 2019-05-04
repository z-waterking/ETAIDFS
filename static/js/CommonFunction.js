
//根据全局变量更新面包屑导航条
$.RefreshBread = function(){
	alert('refreshaaa');
//	$("#BreadNav").clear();
	var $li = $("<li></li>")
	$li.append("abcde")
	$li.appendTo($("#BreadNav"))
};
//封装的Get函数，callback为传递进来的回调
$.GetData = function(url, data, callback){
    $.ajax({
		type: "get",
		async: true, // 异步执行
		url: url,
		data: data,
		contentType: 'application/json',
		dataType: "json", // 返回数据形式为json
		success: function (json) {
			callback(json);
		},
		error: function (errorMsg) {
		}
    });
}
//封装的Post函数
$.PostData = function(url, data, callback){
    $.ajax({
            type: "post",
            async: true, // 异步执行
            url: url,
            data: JSON.stringify(data),
            contentType: 'application/json',
            dataType: "json", // 返回数据形式为json
            success: function (json) {
                callback(json);
            },
            error: function (errorMsg) {
            }
        });
}
