$(document).ready(function () {
    // add row
    $('#addrow').on('click', function () {
        addrow()
    })
    // add column
    $('#addcol').on('click', function () {
        addcol()
    })

})

function addrow() {
    $("#srdtable tr:last").after("<tr></tr>");
    $("#srdtable tr:nth-child(1) td").each(function () {
        $("#srdtable tr:last").append('<td><input type="text" value="Value"></td>')
    });
}

function addcol() {
    $("#srdtable thead tr").append("<th><input type='text' value='Column'></th>")

    $("#srdtable tbody tr").each(function () {
        $(this).append('<td><input type="text" value="Value"></td>');
    })

}