//重置大类、小类、国家的选择
$.ResetList = function(){
    //更新二级目录列表
    $.GetData('GetCommonSecondaryClass', PagePosition, function(SecondaryClass){
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

//重置echarts
$.ResetChart = function(){
    //清空Title
    $("#TotalTitle").empty();
    $("#CountryTitle").empty();
    //
    $("div[name=ChartContainer]").empty();
    $chartTotal = $('<canvas class="my-4" id="TotalChart" width="900" height="380"></canvas>')
    $chartTotal.appendTo($("#TotalChartContainer"))
    $chartCountry = $('<canvas class="my-4" id="CountryChart" width="900" height="380"></canvas>')
    $chartCountry.appendTo($("#CountryChartContainer"))
}

//重置sidebar导航条
$.ResetSideNav = function(){
    // alert('a');
    //todo：完成侧边导航栏重置逻辑
    $("#ResetSideBarTarget").click();
}