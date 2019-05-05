//国家信息展示
//更新小类的选项
$("#RepresentClassCountryInfoSecondaryClass").change(function(object){
    console.log(object.target);
    //获取当前选中的大类
    var select = object.target;
    NeedSecondaryClass = select.options[select.selectedIndex].value;
    //更新其对应的三级目录列表
    $.GetData('GetCommonThirdClass', {'SecondaryClass': NeedSecondaryClass}, function(ThirdClass){
        //先清空三级目录
        $("#RepresentClassCountryInfoThirdClass").empty()
        for(var i = 0; i < ThirdClass.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', ThirdClass[i]);
            $op.append(ThirdClass[i]);
            //加入对应的三级目录选择列表中
            $op.appendTo($("#RepresentClassCountryInfoThirdClass"));
        }
    })
})
//根据大类、小类以及页面状态取得需要的数据
//notice: 科学与技术发展关联聚类预测需要单独判断
$("#ClassCountrySelectEnter").click(function(){

})