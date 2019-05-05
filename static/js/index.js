
//全局变量，记录整个页面的状态
PagePosition = {
    'FirstDirectory':'默认',
    'SecondDirectory':null,
    'ThirdDirectory':null,
    'ForthDirectory':null
}
//页面加载完成后，更新对应选择框中的列表
$(function(){
    //从服务器端取得二级目录、国家列表、以及年份列表
    //更新二级目录列表
    $.GetData('GetCommonSecondaryClass', {}, function(SecondaryClass){
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
            for(var i = 0; i < Years.length; i++){
                //新建一个option
                var $op = $("<option></option>")
                $op.attr('value', Years[i]);
                $op.append(Years[i]);
                //加入（name以SelectStage开头)年份选择列表中
                $op.appendTo($("select[name^=SelectStage]"));
            }
        }
    )
});
