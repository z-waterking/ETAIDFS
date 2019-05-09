//总体信息展示
//更新小类的选项
$("#RepresentTotalInfoSecondaryClass").change(function(object){
    console.log(object.target);
    //获取当前选中的大类
    var select = object.target;
    NeedSecondaryClass = select.options[select.selectedIndex].value;
    data = Object.assign({}, PagePosition);
    data['SecondaryClass'] = NeedSecondaryClass;
    //更新其对应的三级目录列表
    $.GetData('GetCommonThirdClass', data, function(ThirdClass){
        //先清空三级目录
        $("#RepresentTotalInfoThirdClassContent").empty()
        for(var i = 0; i < ThirdClass.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', ThirdClass[i]);
            $op.append(ThirdClass[i]);
            //加入对应的三级目录选择列表中
            $op.appendTo($("#RepresentTotalInfoThirdClassContent"));
        }
    })
})
//根据大类、小类以及页面状态取得需要的数据
//notice: 科学与技术发展关联聚类预测需要单独判断
$("#TotalClassSelectEnter").click(function(){
    //取得大类和小类的文本，向后端请求数据
    //获取大类
    var SecondarySelect = $("#RepresentTotalInfoSecondaryClass")[0]
    var SecondaryClass = SecondarySelect.options[SecondarySelect.selectedIndex].value
    console.log(SecondaryClass)
    //获取小类
    var ThirdSelect = $("#RepresentTotalInfoThirdClassContent")[0]
    var ThirdClass = ThirdSelect.options[ThirdSelect.selectedIndex].value
    //组织向后端请求的展示数据
    PostDataInfo = {}
    //填充请求数据
    PostDataInfo = Object.assign({}, PagePosition);
    PostDataInfo['SecondaryClass'] = SecondaryClass;
    PostDataInfo['ThirdClass'] = ThirdClass;
    console.log(PostDataInfo);
    //向服务器请求数据
    $.PostData('GetTotalData', PostDataInfo, function(result){
        if(result['success'] == true){
            //设置标题
            $('#TotalTitle').text(result['title'])
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById('TotalChart'));
            //判断需要的图表类型：line / plot
            if(result['graph'] == 'line'){
                //设置线型myChart
                $.SetLineChart(myChart, result);
            }else if(result['graph'] == 'plot'){
                $.SetPlotChart(myChart, result);
            }
        }else{
            //todo 修改为通知：查询失败
            alert("Error");
        }
    })
})