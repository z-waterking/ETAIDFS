$("#ExpertInfoEnter").click(function(){
    //获取此页面中的全部控件中的值
    //获取技术领域
//    TechnicalField = $('#TechnicalField')[0]
//    TechnicalField_Value = TechnicalField.options[TechnicalField.selectedIndex].value
//    //获取姓名
//    // name = $('#name')[0];
//    // name_value = $('#name').val();
//    //获取出生年份
//    birthday = $('#Birthday')[0]
//    birthday_value = birthday.options[birthday.selectedIndex].value
//    console.log('TechnicalField')
//    console.log(TechnicalField_Value)
//    // console.log('name')
//    // console.log(name_value)
//    console.log('Birthday')
//    console.log(birthday_value)

    //提交的最终数据
    PostInfo = {}
    PostInfo['TechnicalField'] = "TechnicalField"
    PostInfo['Name'] = "Name"
    PostInfo['Birthday'] = "Birthday"
    PostInfo['Sex'] = "Sex"
    PostInfo['Nation'] = "Nation"
    PostInfo['WorkPlace'] = "WorkPlace"
    PostInfo['Title'] = "Title"
    PostInfo['Job'] = "Job"
    PostInfo['City'] = "City"
    PostInfo['Province'] = "Province"
    PostInfo['Address'] = "Address"
    PostInfo['PostCode'] = "PostCode"
    PostInfo['HighestDegree'] = "HighestDegree"
    PostInfo['GrantTime'] = "GrantTime"
    PostInfo['GrantUniversity'] = "GrantUniversity"
    PostInfo['GrantCountry'] = "GrantCountry"
    PostInfo['HonorAndReward'] = "HonorAndReward"
    PostInfo['Email'] = "Email"
    PostInfo['Phone'] = "Phone"


    //提交数据向服务器保存，让其保存
    $.PostData('SaveExpertInformation', PostInfo, function(result){
        if(result['success'] == true){
            //todo:将alert修改为消息提示框
            alert("提交成功");
            //   $.dialog({ title: '消息提示',content:"成功保存"});
        }else{
            alert("Error");
        }
    })
})