$('#myTab active').on('click', function (e) {
e.preventDefault()
$(this).tab('show')})
$('#myTab a[href="#ug"]').tab('show')
$('#myTab a[href="#pg"]').tab('show')
$('#myTab a[href="#other"]').tab('show')

$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    e.target // newly activated tab
    e.relatedTarget // previous active tab
})