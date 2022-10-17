$(function(e) {
	'use strict'
	//______File-Export Data Table 2
	var table = $('#file-datatablesea').DataTable({
		buttons: [ 'copy', 'excel', 'pdf', 'colvis' ],
		responsive: true,
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
		}
	});
	table.buttons().container()
	.appendTo( '#file-datatablesea_wrapper .col-md-6:eq(0)' );	

	//______Select2 
	$('.select2').select2({
		minimumResultsForSearch: Infinity
	});
	

	$('.select2-no-search').select2({
		minimumResultsForSearch: Infinity,
		placeholder: 'All categories',
		 width: '100%'
	});

	$('#form-input-datatable').on('draw.dt', function() {
		$('.select2-no-search').select2({
			minimumResultsForSearch: Infinity,
			placeholder: 'Choose one'
		});
	});

});

