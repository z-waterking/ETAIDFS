$("#ExpertInfoEnter").click(function(){
    alert('OK')
    //获取此页面中的全部控件中的值
    //获取技术领域,Value为一个列表
    TechnicalField = $('#TechnicalField')[0]
    technicalfield = $('#TechnicalField').selectpicker('val')
    //获取姓名
    name_value = $('#Name').val();
    //获取出生年份
    Birthday = $('#Birthday')[0]
    birthday = Birthday.options[Birthday.selectedIndex].value
    //获取性别
    sex = $('input[name=sex]:checked').val();
    //获取民族
    nation = $('#Nation').val();
    //获取所在单位
    workplace = $('#WorkPlace').val();
    //获取职称
    title = $('#Title').val();
    //获取职务
    job = $('#Job').val();
    //获取城市
    city = $('#City').val();
    //获取省份
    Province = $('#Province')[0]
    province = Province.options[Province.selectedIndex].value
    //获取通信地址
    address = $('#Address').val();
    //获取邮政编码
    postcode = $('#PostCode').val();
    //获取最高学历
    HighestDegree = $('#HighestDegree')[0]
    highestdegree = HighestDegree.options[HighestDegree.selectedIndex].value
    //授予时间
    GrantYear = $('#GrantYear')[0]
    GrantMonth = $('#GrantMonth')[0]
    GrantDay = $('#GrantDay')[0]
    GrantYear_Value = GrantYear.options[GrantYear.selectedIndex].value
    GrantMonth_Value = GrantMonth.options[GrantMonth.selectedIndex].value
    GrantDay_Value = GrantDay.options[GrantDay.selectedIndex].value
    granttime = GrantYear_Value + '年' + GrantMonth_Value + '月' + GrantDay_Value + '日'
    //授予学校
    grantuniversity = $('#GrantUniversity').val();
    //授予国家
    grantcountry = $('#GrantCountry').val();
    //荣誉奖励
    honorandreward = $('#HonorAndReward').val();
    //授予国家
    email = $('#Email').val();
    //授予国家
    phone = $('#Phone').val();


    //查看是否正确
//    console.log('TechnicalField')
//    console.log(TechnicalField_Value)
//    console.log('name')
//    console.log(name_value)
//    console.log('Birthday')
//    console.log(birthday_value)
//    console.log('Sex')
//    console.log(sex)
//    console.log('Nation')
//    console.log(nation)
//    console.log('WorkPlace')
//    console.log(workplace)
//    console.log('Title')
//    console.log(title)
//    console.log('Job')
//    console.log(job)
//    console.log('City')
//    console.log(city)
//    console.log('Province')
//    console.log(province)
//    console.log('Address')
//    console.log(address)
//    console.log('PostCode')
//    console.log(postcode)
//    console.log('HighestDegree')
//    console.log(highestdegree)
//    console.log('GrantTime')
//    console.log(granttime)
//    console.log('GrantUniversity')
//    console.log(grantuniversity)
//    console.log('GrantCountry')
//    console.log(grantcountry)
//    console.log('HonorAndReward')
//    console.log(honorandreward)
//    console.log('Email')
//    console.log(email)
//    console.log('Phone')
//    console.log(phone)

    //提交的最终数据
    PostInfo = {}
    PostInfo['TechnicalField'] = technicalfield
    PostInfo['Name'] = name_value
    PostInfo['Birthday'] = birthday
    PostInfo['Sex'] = sex
    PostInfo['Nation'] = nation
    PostInfo['WorkPlace'] = workplace
    PostInfo['Title'] = title
    PostInfo['Job'] = job
    PostInfo['City'] = city
    PostInfo['Province'] = province
    PostInfo['Address'] = address
    PostInfo['PostCode'] = postcode
    PostInfo['HighestDegree'] = highestdegree
    PostInfo['GrantTime'] = granttime
    PostInfo['GrantUniversity'] = grantuniversity
    PostInfo['GrantCountry'] = grantcountry
    PostInfo['HonorAndReward'] = honorandreward
    PostInfo['Email'] = email
    PostInfo['Phone'] = phone


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