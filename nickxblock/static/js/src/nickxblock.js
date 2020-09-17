/* Javascript for NikitaXBlock. */
function NikitaXBlock(runtime, element) {

    function showAlert(result) {
        alert(result);
    }

    var handlerUrl = runtime.handlerUrl(element, 'check');

    $('button', element).click(function(event) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"some": "data"}),
            success: showAlert
        });
    })

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
