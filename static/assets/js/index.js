
/*Data Table */
$('#recentorders').DataTable({
	"order": [[1, "asc"]],
	"language": {
		searchPlaceholder: 'Search...',
		sSearch: '',
	}
});
//______Select2 
$('.select2').select2({
	minimumResultsForSearch: Infinity
});