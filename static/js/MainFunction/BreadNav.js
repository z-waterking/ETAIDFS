//修改一级目录的点击事件，更新面包屑导航条
$('a[name=FirstDirectory] > button').click(function(object){
    console.log(object.target.innerHTML);
    //一级目录只改第一级的，后面三级设为null
    PagePosition['FirstDirectory'] = object.target.innerHTML;
    PagePosition['SecondDirectory'] = null;
    PagePosition['ThirdDirectory'] = null;
    PagePosition['ForthDirectory'] = null;
    //刷新面包屑导航
    $.RefreshBread();
    //重置侧边栏
    $.ResetSideNav();
    //重置列表
    $.ResetList();
    //获取简介
    $.GetIntroduction(PagePosition['FirstDirectory']);
})

//修改二级目录的点击事件，更新面包屑导航条
$('li[name=SecondDirectory] > a').click(function(object){
    console.log(object.target);
    //去掉自己的类active
    //二级目录只改第二级的，后面设为null
    PagePosition['SecondDirectory'] = object.target.innerHTML;
    PagePosition['ThirdDirectory'] = null;
    PagePosition['ForthDirectory'] = null;
    $.RefreshBread();
    //重置Echarts
    $.ResetChart();
    //重置四级目录
    $.ResetForthDirectory();
})

//修改三级目录的点击事件，更新面包屑导航条
$('li[name=ThirdDirectory] > a').click(function(object){
    console.log(object.target.innerHTML);
    //三级目录只改第三级的，后面设为null
    PagePosition['ThirdDirectory'] = object.target.innerHTML;
    PagePosition['ForthDirectory'] = null;
    $.RefreshBread();
    //重置Echarts
    $.ResetChart();
})

//修改四级目录的点击事件，更新面包屑导航条
$('li[name=ForthDirectory] > a').click(function(object){
    console.log(object.target.innerHTML);
    //四级目录需要修改对应的二级、三级、四级的内容，后面设为null
    //根据四级目录刷新二级、三级目录
    $.RefreshSecThiByFor(object.target);
    PagePosition['ForthDirectory'] = object.target.innerHTML;
    $.RefreshBread();
    //在点击四级目录时，重置所有的List
    $.ResetList();
    //重置Echarts
    $.ResetChart();
    //重置二级、四级目录
    $.ResetSecondDirectory();
    $.ResetForthDirectory();
})