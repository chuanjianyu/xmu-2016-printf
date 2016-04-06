/* tables */

/* 后台管理界面 */
$(document).ready( function () {
    $('#table_listUser').DataTable({
		ordering:false
	});
});

$(document).ready( function () {
    $('#table_listRoleFunction').DataTable({
		ordering:false
	});
});

$(document).ready( function () {
    $('#table_listFunction').DataTable({
		ordering:false
	});
});

$(document).ready( function () {
    $('#table_listRoleType').DataTable({
		ordering:false
	});
});

$(document).ready( function () {
    $('#table_listUserAuthor').DataTable({
		ordering:false
	});
});

/* 查询中心table  */
/* 查询中心table 历史数据查询 */
$(document).ready( function () {
	$('.Quato_table_class').DataTable({
		ordering:false
	});
});

$(document).ready( function () {
	$('.Variable_table_class').DataTable({
		ordering:false
	});
});

/* 查询中心table 水司之间对比 */
$(document).ready( function () {
	$('.Quato_SC_class').DataTable({
		ordering:false
	});
});

$(document).ready( function () {
	$('.Variable_SC_class').DataTable({
		ordering:false
	});
});

/* 查询中心select：水司之间对比 multiSelect */
$(document).ready(function() {
	$('.multi_YearClass').multiselect();
});

$(document).ready(function() {
	$('.single_Class').multiselect();
});

/* Comprehensive analyse table*/
$(document).ready(function() {
	$('.ComAna_table_class').DataTable({
		ordering:false
	});
});




