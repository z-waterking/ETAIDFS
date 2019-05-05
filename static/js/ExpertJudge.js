//更新小类的选项
$("#JudgeStageSecondaryClass").change(function(object){
    console.log(object.target);
    //获取当前选中的大类
    var select = object.target;
    NeedSecondaryClass = select.options[select.selectedIndex].value;
    //更新其对应的三级目录列表
    $.GetData('GetCommonThirdClass', {'SecondaryClass': NeedSecondaryClass}, function(ThirdClass){
        //先清空三级目录
        $("#JudgeStageThirdClass").empty()
        for(var i = 0; i < ThirdClass.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', ThirdClass[i]);
            $op.append(ThirdClass[i]);
            //加入对应的三级目录选择列表中
            $op.appendTo($("#JudgeStageThirdClass"));
        }
    })
})
//提交全部的选择
$("#JudgeStageEnter").click(function(){
    //获取此页面中的全部控件中的值
    //获取大类
    var SecondarySelect = $("#JudgeStageSecondaryClass")[0]
    var SecondaryClass = SecondarySelect.options[SecondarySelect.selectedIndex].value
    console.log(SecondaryClass)
    //获取小类
    var ThirdSelect = $("#JudgeStageThirdClass")[0]
    var ThirdClass = ThirdSelect.options[ThirdSelect.selectedIndex].value
    console.log(ThirdClass)
    //获取所有的起始年份
    var AllStartYearsSelect = $('select[name=SelectStageStartYears]')
    var AllStartYears = []
    $.each(AllStartYearsSelect, function(n, select){
        var start = select.options[select.selectedIndex].value
        AllStartYears.push(start);
    })
    //获取所有的终止年份
    var AllStopYearsSelect = $('select[name=SelectStageStartYears]')
    var AllStopYears = []
    $.each(AllStopYearsSelect, function(n, select){
        var stop = select.options[select.selectedIndex].value
        AllStopYears.push(stop);
    })
    //组织成对应格式提交
    Stages = ["DevelopStage", "InitialStage", "GrowupStage", "ExpandStage", "MatureStart"];
    PostData = {
        "SecondaryClass": SecondaryClass,
        "ThirdClass": ThirdClass,
    }
    //遍历阶段，组织数据
    for(var i = 0; i < Stages.length; i++)
    {
        temp = {
                "start": AllStartYears[i],
                "stop": AllStopYears[i]
        }
        PostData[Stages[i]] = temp;
    }
    //提交数据向服务器保存，让其
    $.PostData('JudgeResult', PostData, function(result){
        if(result['success'] == true){
            //todo:将alert修改为消息提示框
            alert("Success");
        }else{
            alert("Error");
        }
    })
})