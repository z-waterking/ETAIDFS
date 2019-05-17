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
    });
    //更新专家信息管理中的技术领域
    $.GetData('GetExpertTecnology', PagePosition, function(Tecnologys){
        // console.log()
        for(var i = 0; i < Tecnologys.length; i++){
            $('#TechnicalField').append("<option value=" + Tecnologys[i] + ">" + Tecnologys[i] + "</option>");
        }
        $('#TechnicalField').selectpicker('refresh');
        $('#TechnicalField').selectpicker('render');
    });
    //更新专家信息管理中的出生年份
    $.GetData('GetExpertBirthYear', {}, function(Birthday){
        $('#Birthday').empty();
        var $op1 = $("<option value='请选择' hidden>请选择</option>");
        $op1.appendTo($('#Birthday'));
        for(var i = 0; i < Birthday.length; i++){
            //新建一个option
            var $op = $("<option></option>");
            $op.attr('value', Birthday[i]);
            $op.append(Birthday[i]);
            //加入（name以SelectStage开头)年份选择列表中
            $op.appendTo($('#Birthday'));
        }
    });
    //更新专家信息管理中的省
    $.GetData('GetExpertProvince', {}, function(Province){
        $('#Province').empty();
        var $op1 = $("<option value='请选择' hidden>请选择</option>");
        $op1.appendTo($('#Province'));
        for(var i = 0; i < Province.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', Province[i]);
            $op.append(Province[i]);
            //加入（name以SelectStage开头)年份选择列表中
            $op.appendTo($('#Province'));
        }
    });
    //获取最高学历
    $.GetData('GetHighestDegree', {}, function(HighestDegree){
        $('#HighestDegree').empty();
        var $op1 = $("<option value='请选择' hidden>请选择</option>");
        $op1.appendTo($('#HighestDegree'));
        for(var i = 0; i < HighestDegree.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', HighestDegree[i]);
            $op.append(HighestDegree[i]);
            //加入（name以SelectStage开头)年份选择列表中
            $op.appendTo($('#HighestDegree'));
        }
    });
    //获取授予年
    $.GetData('GetGrantYear', {}, function(GrantYear){
        $('#GrantYear').empty();
        var $op1 = $("<option value='请选择' hidden>请选择</option>");
        $op1.appendTo($('#GrantYear'));
        for(var i = 0; i < GrantYear.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', GrantYear[i]);
            $op.append(GrantYear[i]);
            //加入（name以SelectStage开头)年份选择列表中
            $op.appendTo($('#GrantYear'));
        }
    });
    //获取授予月
    $.GetData('GetGrantMonth', {}, function(GrantMonth){
        $('#GrantMonth').empty();
        var $op1 = $("<option value='请选择' hidden>请选择</option>");
        $op1.appendTo($('#GrantMonth'));
        for(var i = 0; i < GrantMonth.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', GrantMonth[i]);
            $op.append(GrantMonth[i]);
            //加入（name以SelectStage开头)年份选择列表中
            $op.appendTo($('#GrantMonth'));
        }
    });
    //获取授予日
    $.GetData('GetGrantDay', {}, function(GrantDay){
        $('#GrantDay').empty();
        var $op1 = $("<option value='请选择' hidden>请选择</option>");
        $op1.appendTo($('#GrantDay'));
        for(var i = 0; i < GrantDay.length; i++){
            //新建一个option
            var $op = $("<option></option>")
            $op.attr('value', GrantDay[i]);
            $op.append(GrantDay[i]);
            //加入（name以SelectStage开头)年份选择列表中
            $op.appendTo($('#GrantDay'));
        }
    })
};

//重置所有的小类
$.ResetThirdClass = function(){
    //重置专家判断部分的小类
    $("#JudgeStageThirdClass").empty();
    var $op = $("<option hidden></option>")
    $op.append('请选择小类');
    //加入对应的三级目录选择列表中
    $op.appendTo($("#JudgeStageThirdClass"));
    //重置整体信息展示部分的小类
    $("#RepresentTotalInfoThirdClassContent").empty();
    var $op = $("<option hidden></option>");
    $op.append('请选择小类');
    //加入对应的三级目录选择列表中
    $op.appendTo($("#RepresentTotalInfoThirdClassContent"));
    //重置国家信息展示部分的小类
    $("#RepresentClassCountryInfoThirdClass").empty();
    var $op = $("<option hidden></option>");
    $op.append('请选择小类');
    //加入对应的三级目录选择列表中
    $op.appendTo($("#RepresentClassCountryInfoThirdClass"));
};

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

//重置二级目录
$.ResetSecondDirectory = function(){
    $('li[name=SecondDirectory] > a').removeClass("active");
}
//重置三级目录
$.ResetThirdDirectory = function(){
    $('li[name=ThirdDirectory] > a').removeClass("active");
}
//重置四级目录
$.ResetForthDirectory = function(){
    $('li[name=ForthDirectory] > a').removeClass("active");
}
//重置collapse
$.ResetCollapseBox = function(){
    //对可折叠元素进行折叠
    $("div[name=CollapseBox]").removeClass("show");
}

//重置sidebar导航条
$.ResetSideNav = function(){
    //重置二、三、四级目录，及下拉框
    $.ResetSecondDirectory();
    $.ResetThirdDirectory();
    $.ResetForthDirectory();
    //收起下拉框
    $.ResetCollapseBox();
    //点击第一条
    $("#ResetSideBarTarget")[0].click();
}

