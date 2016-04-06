/* 获取系统时间 */
function getdates()
{
	var week_array	= new Array("星期天","星期一","星期二","星期三","星期四","星期五","星期六");
	var now 	= new Date();
	//var next = new Date();
	//next.setDate(next.getDate() + 1);

	var year 	= now.getFullYear();
	var month 	= now.getMonth()+1;
	var day 	= now.getDate();
	var week 	= now.getDay();
	var hour 	= now.getHours();
	var minutes = now.getMinutes();
	var seconds = now.getSeconds();

	//var next_year 	= next.getFullYear();
	//var next_month 	= next.getMonth()+1;
	//var next_day 	= next.getDate();

	if(month < 10) 		month 	= "0" + month
	if(day < 10) 		day 	= "0" + day
	if(hour < 10) 		hour 	= "0" + hour
	if(minutes < 10) 	minutes = "0" + minutes
	if(seconds < 10) 	seconds = "0" + seconds

	//if(next_month < 10) 		next_month 	= "0" + next_month
	//if(next_day < 10) 		next_day 	= "0" + next_day

	var shows="<span>" + year + "-" + month + "-" + day + "  " + hour + ":" + minutes +  ":" + seconds + "  " + week_array[week] + "</span>";
	//var starttime= year + "-" + month + "-" + day ;
	//var endtime= next_year + "-" + next_month + "-" + next_day ;

	document.getElementById("date").innerHTML=shows;
	//document.getElementById("starttime_id").value=starttime;
	//document.getElementById("endtime_id").value=endtime;
	setTimeout("getdates()",1000);
}
