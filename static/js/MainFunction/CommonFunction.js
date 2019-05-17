//两种图表的option
OPTION = {
    'line':{
        legend:{
            data:['研发期', '初创期', '成长期', '扩张期', '成熟期']
        },
        xAxis: {
            name: '年份',
            type: 'category',
            data: []
        },
        yAxis: {
            name: '',
            type: 'value'
        },
        series: [{
            data: [],
            type: 'scatter'
        }]
    },
    'plot':{
        xAxis: {
            name:'科学热度',
            boundaryGap:10,
            // min:0,
            // max:700,
            offset:-80,
            type:'value',
        },
        yAxis: {
            // boundaryGap:10,
            name:'技术热度',
            // min:0,
            // max:700,
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
    // 清空之前的数据
    option.series = [];
    option.xAxis.data = [];
    //整理收到的数据
    len = result['xs'].length;
    develop = new Array(len).fill(null);
    initial = new Array(len).fill(null);
    growup = new Array(len).fill(null);
    expand = new Array(len).fill(null);
    mature = new Array(len).fill(null);
    console.log('************');
    console.log(result['stage']);
    for(i = 0; i < result['ys'].length; i++){
        switch(result['stage'][i]){
            case 'Develop': develop[i] = result['ys'][i];break;
            case 'Initial': initial[i] = result['ys'][i]; break;
            case 'Growup': growup[i] = result['ys'][i]; break;
            case 'Expand': expand[i] = result['ys'][i]; break;
            case 'Mature': mature[i] = result['ys'][i];
        }
    }
    all_stage_data = [develop, initial, growup, expand, mature];
    symbols = ['rect', 'triangle', 'diamond', 'pin', 'circle'];
    //将数据逐个加入到Echarts组件中
    //设置x轴
    option.xAxis.data = result['xs'];
    //设置y轴
    for(i = 0; i < option.legend.data.length; i++){
        temp = {
            symbolSize: 20,
            data: all_stage_data[i],
            type: 'scatter',
            name:option.legend.data[i],
            symbol:symbols[i]
        };
        option.series.push(temp)
    }
    console.log('***************');
    console.log(option);
    myChart.setOption(option);
};

//设置散点型Echarts
$.SetPlotChart = function(myChart, result){
    // 指定图表的配置项和数据
    var option = OPTION['plot'];
    //清空之前的数据
    option.series[0].data = [];
    for(var i = 0; i < result['xs'].length; i++){
        temp = {
            name:result['label'][i],
            label:{
                offset:[40, 0],
                fontSize:15,
                // fontWeight:'bold',
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

//根据全局变量更新面包屑导航条
$.RefreshBread = function(){
    //先清除其中的元素
    $("#BreadNav").empty();
	var Directory = ['FirstDirectory', 'SecondDirectory', 'ThirdDirectory', 'ForthDirectory']
    $.each(Directory, function(n, direct){
        //console.log(n + direct);
        if(PagePosition[direct] == null){
            return;
        }
        var $li = $("<li></li>");
        $li.attr('class', 'active');
        $li.append(PagePosition[direct]);
        $li.appendTo($("#BreadNav"));
    });
};

//根据点击的第四级目录更新对应的第二级、第三级名称
$.RefreshSecThiByFor = function(Forth){
    console.log(Forth);
    //寻找往上两级的目录
    ThirdId = Forth.getAttribute("data-parent");
    Third = $(ThirdId)[0];
    console.log(Third);
    SecondId = Third.getAttribute("data-parent");
    Second = $(SecondId)[0];
    console.log(Second);
    //设置对应的二级、三级目录
    PagePosition['SecondDirectory'] = Second.innerHTML;
    PagePosition['ThirdDirectory'] = Third.innerHTML;
}

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
