
//全局变量，记录整个页面的状态
PagePosition = {}

//页面加载完成后，更新对应的列表f
$(function(){
    $("div[name=test]").append("abcde");
    //取得二级目录，时间列表，国家列表
    SecondaryClass = ['A', 'B', 'C']
    Times = [2008, 2009, 2010]
    Countrys = ['US', 'UK', 'China']
    //为所有的下拉选择框添加选择动作
    $('div[name=SelectItemsSecondaryClass]').change(function(){
      alert($(this).text());
    });
    //更新二级目录列表
    for(var i = 0; i < SecondaryClass.length; i++){
        //新建一个item
        var $bt = $("<button></button>")
        $bt.attr('class', 'dropdown-item');
        $bt.attr('type', 'button');
        $bt.append(SecondaryClass[i]);
        //加入二级目录选择列表中
        $bt.appendTo($("div[name=SelectItemsSecondaryClass]"));
    }
    //更新国家列表
    for(var i = 0; i < Countrys.length; i++){
            //新建一个item
            var $bt = $("<button></button>")
            $bt.attr('class', 'dropdown-item');
            $bt.attr('type', 'button');
            $bt.append(Countrys[i]);
            //加入国家选择列表中
            $bt.appendTo($("div[name=SelectItemsCountry]"));
        }
    //更新时间列表
    for(var i = 0; i < Times.length; i++){
            //新建一个item
            var $bt = $("<button></button>")
            $bt.attr('class', 'dropdown-item');
            $bt.attr('type', 'button');
            $bt.append(Times[i]);
            //加入时间选择列表中
            $bt.appendTo($("div[name=SelectItemsStageYears]"));
        }
});