$("#ExpertInfoEnter").click(function(){
    //获取此页面中的全部控件中的值
    //获取技术领域
    TechnicalField = $('#TechnicalField')[0]
    TechnicalField_Value = TechnicalField.options[TechnicalField.selectedIndex].value
    //获取姓名
    name = $('#name')[0]
    name_value = $('#name').val()
    //获取出生年份
    birthday = $('#birthday')[0]
    birthday_value = birthday.options[birthday.selectedIndex].value

    console.log('TechnicalField')
    console.log(TechnicalField_Value)
    console.log('name')
    console.log(name_value)
    console.log('birthday')
    console.log(birthday_value)

//    //提交数据向服务器保存，让其保存
//    $.PostData('JudgeResult', PostDataInfo, function(result){
//        if(result['success'] == true){
//            //todo:将alert修改为消息提示框
//            alert("提交成功");
//            //   $.dialog({ title: '消息提示',content:"成功保存"});
//        }else{
//            alert("Error");
//        }
//    })
})