//两种图表的option
OPTION = {
    'line':{
        xAxis: {
            type: 'category',
            data: []
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: [],
            type: 'line'
        }]
    },
    'plot':{
        xAxis: {
             boundaryGap:10,
            min:0,
            max:700,
            offset:-80,
            type:'value',
        },
        yAxis: {
            // boundaryGap:10,
            min:0,
            max:700,
            offset:-200,
            type:'value'
        },
        series: [{
            symbolSize: 20,
            data: [

            ],
            type: 'scatter'
        }]
    }
}

//设置线型Echarts
$.SetLineChart = function(myChart, result){
    // 指定图表的配置项和数据
    var option = OPTION['line']
    console.log(option);
    option.xAxis.data = result['xs']
    for(var i = 0; i < result['ys'].length; i++){
        symbol = null
        switch(result['stage'][i]){
            case 'Develop': symbol = 'rect';break;
            case 'Initial': symbol = 'triangle'; break;
            case 'Growup': symbol = 'diamond'; break;
            case 'Expand': symbol = 'arrow'; break;
            case 'Mature': symbol = 'circle';
        }
        temp = {
            'value': result['ys'][i],
            'symbol': symbol,
            'symbolSize': 20
        }
        option.series[0].data.push(temp);
    }
    console.log(option);
    myChart.setOption(option);
}

//设置散点型Echarts
$.SetPlotChart = function(myChart, result){
    // 指定图表的配置项和数据
    var option = OPTION['plot']
    for(var i = 0; i < result['xs'].length; i++){
        temp = {
            name:result['label'][i],
            label:{
                offset:[30, 0],
                fontSize:15,
                fontWeight:'bold',
                show:true,
                color:'#000',
                formatter:function(param){
                    return param.name
                }
            },
            value:[result['xs'][i], result['ys'][i]]
        }
        option.series[0].data.push(temp);
    }
    console.log(option);
    myChart.setOption(option);
}

//重置大类、小类、国家的选择
$.ResetList = function(){
    //更新二级目录列表
    $.GetData('GetCommonSecondaryClass', {}, function(SecondaryClass){
        //先插入第一个作为title
        $("select[name=SelectSecondaryClass]").empty();
        var $first = $("<option hidden></option>");
        $first.append("请选择大类")
        $first.appendTo($("select[name=SelectSecondaryClass]"));
        for(var i = 0; i < SecondaryClass.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', SecondaryClass[i]);
            $op.append(SecondaryClass[i]);
            //加入二级目录选择列表中
            $op.appendTo($("select[name=SelectSecondaryClass]"));
        }
    })
    //更新国家列表
    $.GetData('GetCommonCountrys', {}, function(Countrys){
        //插入第一条作为国家的title
        $("select[name=SelectCountry]").empty();
        var $first = $("<option hidden></option>");
        $first.append("请选择国家")
        $first.appendTo($("select[name=SelectCountry]"));
        for(var i = 0; i < Countrys.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', Countrys[i]);
            $op.append(Countrys[i]);
            //加入国家选择列表中
            $op.appendTo($("select[name=SelectCountry]"));
        }
    })
    //更新年份列表
    $.GetData('GetCommonYear', {}, function(Years){
        //插入第一条作为年份的title
        $("select[name^=SelectStage]").empty();
        var $first = $("<option hidden></option>");
        $first.append("请选择年份")
        $first.appendTo($("select[name^=SelectStage]"));
        for(var i = 0; i < Years.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', Years[i]);
            $op.append(Years[i]);
            //加入（name以SelectStage开头)年份选择列表中
            $op.appendTo($("select[name^=SelectStage]"));
        }
    })
    //重置所有的小类
    $("#JudgeStageThirdClass").empty();
    var $op = $("<option hidden></option>")
    $op.append('请选择小类');
    //加入对应的三级目录选择列表中
    $op.appendTo($("#JudgeStageThirdClass"));
}

//根据全局变量更新面包屑导航条
$.RefreshBread = function(){
    //先清除其中的元素
    $("#BreadNav").empty();
	var Directory = ['FirstDirectory', 'SecondDirectory', 'ThirdDirectory', 'ForthDirectory']
    $.each(Directory, function(n, direct){
        if(PagePosition[direct] == null){
            return;
        }
        var $li = $("<li></li>");
        $li.attr('class', 'active');
        $li.append(PagePosition[direct]);
        $li.appendTo($("#BreadNav"));
    });
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
