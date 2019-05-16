$.GetIntroduction = function(FirstDirectory){
    page = null
    if(FirstDirectory == '系统简介'){
        page = $('#SystemIntroduction')[0]
    }else{
        page = $('#SubSystemIntroduction')[0]
    }
    $.GetData('GetIntroduction', PagePosition, function(introduction){
        //先插入第一个作为title
        page.innerHTML = introduction['introduction']
    })
}