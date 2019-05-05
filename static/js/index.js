
//全局变量，记录整个页面的状态
PagePosition = {
    'FirstDirectory':'默认',
    'SecondDirectory':null,
    'ThirdDirectory':null,
    'ForthDirectory':null
}
//页面加载完成后，更新对应选择框中的列表
$(function(){
    //更新面包屑导航
    $.RefreshBread();
    $("div[name=test]").append("abcde");
    //取得二级目录，时间列表，国家列表
    SecondaryClass = ['A', 'B', 'C']
    Times = [2008, 2009, 2010]
    Countrys = ['US', 'UK', 'China']
    //更新二级目录列表
    for(var i = 0; i < SecondaryClass.length; i++){
        //新建一个option
        var $op = $("<option></option>")
        $op.attr('value', SecondaryClass[i]);
        $op.append(SecondaryClass[i]);
        //加入二级目录选择列表中
        $op.appendTo($("select[name=SelectSecondaryClass]"));
    }
    //更新国家列表
    for(var i = 0; i < Countrys.length; i++){
        //新建一个option
        var $op = $("<option></option>")
        $op.attr('value', Countrys[i]);
        $op.append(Countrys[i]);
        //加入国家选择列表中
        $op.appendTo($("select[name=SelectCountry]"));
    }
    //更新时间列表
    for(var i = 0; i < Times.length; i++){
        //新建一个option
        var $op = $("<option></option>")
        $op.attr('value', Times[i]);
        $op.append(Times[i]);
        //加入国家选择列表中
        $op.appendTo($("select[name=SelectStageYears]"));
    }
});
