//全局变量，记录整个系统的用户
User = {
}
//全局变量，记录整个页面的状态
PagePosition = {
    'FirstDirectory':'系统简介',
    'SecondDirectory':null,
    'ThirdDirectory':null,
    'ForthDirectory':null
}
//页面加载完成后，更新对应选择框中的列表
$(function(){
    //从服务器端取得二级目录、国家列表、以及年份列表
    // $.ResetList();
    $.GetIntroduction(PagePosition['FirstDirectory'])
});
