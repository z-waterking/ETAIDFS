function dataFormat(data)
{	
	return data.substring(0, data.indexOf("."));
}

function dataFormat_onlyDate(data)
{	
	return data.substring(0, data.indexOf(".")).split(" ")[0];
}

function detail(type, id)
{	
	if(document.body.scrollTop)
	{
		var scrollTopValue = document.body.scrollTop;
		window.onscroll = function()
		{
			document.body.scrollTop = scrollTopValue;
		}
	}
	else if(document.documentElement.scrollTop)
	{
		var scrollTopValue = document.documentElement.scrollTop;
		window.onscroll = function()
		{
			document.documentElement.scrollTop = scrollTopValue;
		}
	}
	$.layer(
	{
	    type: 2,
	    title: "详情",
	    iframe: {src: "detail.action?type=" + type + "&id=" + id},
	    area : ['820px' , '600px'],
	    success : function()
	    {
	        layer.shift('top', 400);	
	    }
	});
}

function detail_message(id)
{	
	if(document.body.scrollTop)
	{
		var scrollTopValue = document.body.scrollTop;
		window.onscroll = function()
		{
			document.body.scrollTop = scrollTopValue;
		}
	}
	else if(document.documentElement.scrollTop)
	{
		var scrollTopValue = document.documentElement.scrollTop;
		window.onscroll = function()
		{
			document.documentElement.scrollTop = scrollTopValue;
		}
	}
	$.layer(
	{
	    type: 2,
	    title: "详情",
	    iframe: {src: "ucmessage_open.action?id=" + id},
	    area : ['720px' , '420px'],
	    success : function()
	    {
	        layer.shift('top', 400);	
	    }
	});
}

function edetail(md5)
{	
	if(document.body.scrollTop)
	{
		var scrollTopValue = document.body.scrollTop;
		window.onscroll = function()
		{
			document.body.scrollTop = scrollTopValue;
		}
	}
	else if(document.documentElement.scrollTop)
	{
		var scrollTopValue = document.documentElement.scrollTop;
		window.onscroll = function()
		{
			document.documentElement.scrollTop = scrollTopValue;
		}
	}
	$.layer(
	{
	    type: 2,
	    title: "详情",
	    iframe: {src: "detailecDetail.action?md5=" + md5},
	    area : ['820px' , '600px'],
	    success : function()
	    {
	        layer.shift('top', 400);	
	    }
	});
}

function imgDetail(imgId)
{	
	if(document.body.scrollTop)
	{
		var scrollTopValue = document.body.scrollTop;
		window.onscroll = function()
		{
			document.body.scrollTop = scrollTopValue;
		}
	}
	else if(document.documentElement.scrollTop)
	{
		var scrollTopValue = document.documentElement.scrollTop;
		window.onscroll = function()
		{
			document.documentElement.scrollTop = scrollTopValue;
		}
	}
	$.ajax(
	{
	    type: "GET",
	    url: "json_detail_imgDetail.action?imgId=" + imgId,
	    success : function(data)
	    {
	    	var imgObj = data.img;
	        var divNode = document.createElement("div");
	        divNode.id = "img_show";
	        divNode.style.cssText = "display:block;z-index:99999;position:fixed;top:0;left:0;width:100%;height:100%;background-color:rgba(33,33,33,0.5);text-align:center;";
	        divNode.innerHTML = "<img src='" + imgObj.imgSrc + "' id='append_img' style='position:relative;top:30%'/>";
	        document.body.appendChild(divNode);
	        var append_img = document.getElementById("append_img");
	        append_img.onclick = function()
	        {
	        	var img_show = document.getElementById("img_show");
	        	document.body.removeChild(img_show);
	        }
	    }
	});
}

function edetailFromComment(id)
{	
	var scrollTopValue = document.body.scrollTop;
	window.onscroll = function()
	{
		document.body.scrollTop = scrollTopValue;
	}
	$.layer(
	{
	    type: 2,
	    title: "详情",
	    iframe: {src: "detailecDetailFromComment.action?id=" + id},
	    area : ['820px' , '600px'],
	    success : function()
	    {
	        layer.shift('top', 400);	
	    }
	});
}

function goOnReading(type, id)
{	
/*
	$.layer(
	{
	    type: 2,
	    title: "相关详情",
	    iframe: {src: "detailgoOnReading.action?type=" + type + "&id=" + id},
	    area : ['820px' , '800px'],
	    success : function()
	    {
	    	parent.layer.shift('top', 400);		
	    }
	});
*/
//	window.location.href = "detailgoOnReading.action?type=" + type + "&id=" + id;
	
	parent.layer.NewIframe("detailgoOnReading.action?type=" + type + "&id=" + id);
}

function addInfoCollection(type, id, bnId)
{	
	$.get("json_operation_addInfoCollection.action?mediaType=" + type + "&infoId=" + id, function(data)
	{
		if(data.isOk == 1)
		{
			alert("收藏成功");
			$("#" + bnId).html("已收藏");
			$("#" + bnId).attr("onclick", "alert('已收藏')");
		}
		else
		{
			alert("收藏失败");
		}
	});
}


function addReportMaterial(type, id, bnId)
{	
	$.get("json_operation_addReportMaterial.action?mediaType=" + type + "&infoId=" + id, function(data)
	{
		if(data.isOk == 1)
		{
			alert("添加成功");
			$("#" + bnId).html("已添加");
			$("#" + bnId).attr("onclick", "alert('已添加')");
		}
		else
		{
			alert("添加失败");
		}
	});	
}
/**
	订阅
 */
function subscript(t,title, type, url, searchCondition, querystr)
{
	var param =
	{
		title : title,
		type : type,
		url : url,
		searchCondition : searchCondition,
		querystr : querystr
	};
	$.post("json_ucSubscription_add.action", param, function(data)
	{
		if(data.ok==null){
			alert("您没有订阅情报的权限！");
		}
		else if (data.ok == 1){
			$(t).html("已订阅");
			alert("订阅成功");
		}
		else if(data.ok==0)
			alert("订阅失败");
		else if(data.ok==-1)
			alert("已订阅过当前频道");
	});
	
}

//空值检测，eg: nullCheck(value, meg, value1, meg2......);
function nullCheck()
{
	for(var i = 0; i < arguments.length; i += 2)
	{
		var value = arguments[i];
		var meg = arguments[i + 1];
		if(value == null || value == "")
		{
			alert(meg);
			return false;
		}
	}
	return true;
}



/***********
 * 全局统计数字
 */
function reversedemo(str)
{
	var str2 = "";
	for ( var i = 0; i < str.length; i++)
	{
		str2 += str.charAt(str.length - i);
	}
	str2 += str.charAt(0);
	return str2;
}

function numstring(num)
{
	num = reversedemo(String(num));
	var len = String(num).length;
	var newnumstring = "";
	for ( var i = 0; i < len; i++)
	{
		if (i % 4 == 3)
		{
			if (i == len - 1)
			{
				newnumstring = newnumstring + num.charAt(i);
			}
			else
			{
				if (i % 8 == 7)
				{
					newnumstring = newnumstring + num.charAt(i) + ".";
				}
				else
				{
					newnumstring = newnumstring + num.charAt(i) + ",";
				}
				
			}
		}
		else
		{
			newnumstring = newnumstring + num.charAt(i);
		}
		if (i == len - 1)
		{
			return reversedemo(newnumstring);
		}
	}
}

function shownum(obg, x)
{
	var num = x;
	var numlen = String(num).length;
	for ( var i = 0; i < numlen; i++)
	{
		var obg2;
		if ($("." + obg + " i").length <= i)
		{
			obg2 = $("<i></i>").appendTo("." + obg);
		}
		obg2 = $("." + obg + " i:eq(" + i + ")");			
		var nownum = String(num).charAt(i);
		var y;
		if (nownum == "%")
		{
			
			y = -10 * 15;
			obg2.addClass("num100");
		}
		else if (nownum == ",")
		{
			y = -184;
			obg2.css("width", "13px");
		}
		else if (nownum == ".")
		{
			y = -11 * 15;
			obg2.css("width", "13px");
		}
		else
		{
			y = -parseInt(nownum) * 15;
		}
		
		obg2.stop();

		obg2.animate({backgroundPosition :'(-230px '+String(y)+'px)' }, 'slow','swing');
	}
}

function randomIncrease(num, digits)
{
	var rd = Math.floor(Math.random() * digits);
	return num + rd;
}

function setHeaderNum(urlFragment)
{

	//加载数据
	$.get("json_index_dataCount.action?urlFragment=" + urlFragment, function(data)
	{
		var updateTime = 5000;//刷新时间
		var dataCountMap = data.dataCountMap;
		for(var key in dataCountMap)
		{
			$("#" + key).css("display", "inline-block");
			shownum(key, numstring(dataCountMap[key]));
		}

		var num_today = dataCountMap['num_today'];//用于随机增长
		var num_total = dataCountMap['num_total'];
		
		function updater()
		{
/*
			//真增长
			$.get("json_index_dataCount.action?urlFragment=" + urlFragment, function(data)
			{
				var updateTime = 5000;//刷新时间
				var dataCountMap = data.dataCountMap;
				for(var key in dataCountMap)
				{
					$("#" + key).css("display", "inline-block");
					shownum(key, numstring(dataCountMap[key]));
				}
			}
*/
			
			//假增长
			var delta = randomIncrease(num_today, 5) - num_today; //保持增量相同
			if(urlFragment!=0)
				delta=1;
			num_today += delta;
			num_total += delta;
			shownum('num_total', numstring(num_total));
			shownum('num_today', numstring(num_today));
		}
		setInterval(updater, updateTime);
	});
}









